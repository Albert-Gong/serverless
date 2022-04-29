from obs import *
import numpy as np
from utils import *

def newObsClient(params):
    ak = params["ak"]
    sk = params["sk"]
    server = params["server"]
    return ObsClient(access_key_id=ak, secret_access_key=sk, server=server)


def downloadFile(params):
    obsClient = params["obsClient"]
    bucket = params["downloadBucket"]
    objName = params["objName"]
    localFile = params["localDownload"]

    resp = obsClient.getObject(bucket, objName, localFile)
    if resp.status < 300:
        print('download file', objName, 'succeed')
    else:
        print('download failed, errorCode: %s, errorMessage: %s, requestId: %s' % (
            resp.errorCode, resp.errorMessage, resp.requestId))


def uploadFile(params):
    obsClient = params["obsClient"]
    bucket = params["uploadBucket"]
    objName = params["objName"]
    localFile = params["localUpload"]

    resp = obsClient.putFile(bucket, objName, localFile)
    if resp.status < 300:
        print('upload file', localFile, 'succeed')
    else:
        print('upload failed, errorCode: %s, errorMessage: %s, requestId: %s' % (
            resp.errorCode, resp.errorMessage, resp.requestId))


def getObjInfoFromObsEvent(event):
    if 's3' in event['Records'][0]:
        s3 = event['Records'][0]['s3']
        eventName = event['Records'][0]['eventName']
        bucket = s3['bucket']['name']
        objName = s3['object']['key']
    else:
        obsInfo = event['Records'][0]['obs']
        eventName = event['Records'][0]['eventName']
        bucket = obsInfo['bucket']['name']
        objName = obsInfo['object']['key']
    print("*** obsEventName: %s, srcBucketName: %s, objName: %s" % (eventName, bucket, objName))
    return bucket, objName


def decode_file(localFile):
    raw_data = []
    with open(localFile, 'r') as reader:
        for line in reader.readlines():
            line = line.strip()
            if line:
                raw_data.append(line)
    str_control = raw_data[0].strip()
    str_data = raw_data[1:]

    str_control = str_control.split(',')
    print(str_control)

    params = []
    if len(str_control[1]) > 0:
        params = list(map(lambda x: int(x), str_control[1:]))

    control = {
        'cmd': str_control[0],
        'params': params
    }

    num_data = []
    for line in str_data:
        line = list(map(lambda x: float(x), line.split(',')))
        num_data.append(line)
    num_data = np.asarray(num_data, dtype=float)
    return control, num_data


def handler(event, context):
    bucketName, objName = getObjInfoFromObsEvent(event)
    print(f"bucket name {bucketName} obj name {objName}")

    ak = context.getUserData("ak")
    sk = context.getUserData("sk")
    server = "obs.cn-north-4.myhuaweicloud.com"

    downloadBucket = "serverless-preprocess-stage-0"
    uploadBucket = "serverless-preprocess-stage-1"

    objectKey = objName
    localFile = "/tmp/" + objectKey

    config = {
        "ak": ak,
        "sk": sk,
        "server": server,
        "downloadBucket": downloadBucket,
        "uploadBucket": uploadBucket,
        "objName": objectKey,
        "localDownload": localFile,
        "localUpload": localFile
    }
    obsClient = newObsClient(params=config)

    config["obsClient"] = obsClient

    print("Download file".center(50, "="))
    downloadFile(params=config)

    control, data = decode_file(localFile)
    print(f'control \n {control}')
    print(f'data \n {data}')

    func = func_mapper[control["cmd"]]
    result = func(data, control["params"])
    print(f'result \n {result}')

    np.savetxt(localFile, result, delimiter=",", fmt='%.6f')

    print("Upload file".center(50, "="))
    uploadFile(params=config)
