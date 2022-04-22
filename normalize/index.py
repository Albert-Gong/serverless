from obs import *
import numpy as np

def nor_norm(localFile):

    array = np.loadtxt(open(localFile, "rb"), delimiter=",", skiprows=0)
    data_shape = array.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    t = np.empty((data_rows, data_cols))
    for i in range(data_cols):
        sum = 0
        for j in range(data_rows):
            sum += array[j, i]
        avg = sum / data_rows
        sum_sq = 0
        for j in range(data_rows):
            sq = (array[j, i] - avg) ** 2
            sum_sq += sq
        std_deviation = (sum_sq / data_rows) ** 0.5
        # 计算标准化结果
        for j in range(data_rows):
            t[j, i] = (array[j, i] - avg) / std_deviation

    np.savetxt(localFile, t, delimiter=",")

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


def handler(event, context):
    bucketName, objName = getObjInfoFromObsEvent(event)
    print(f"bucket name {bucketName} obj name {objName}")

    ak = context.getUserData("ak")
    sk = context.getUserData("sk")
    server = "obs.cn-north-4.myhuaweicloud.com"

    downloadBucket = "serverless-preprocess-stage-0"
    uploadBucket = "serverless-preprocess-stage-1"

    objectKey = objName
    localFile = "/tmp/" +  objectKey

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

    print("Normalize".center(50, "="))
    nor_norm(localFile)

    print("Upload file".center(50, "="))
    uploadFile(params=config)

    # objects = obsClient.listObjects(bucketName="serverless-preprocess")
    # print(objects["body"])
