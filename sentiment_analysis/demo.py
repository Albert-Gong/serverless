# coding: utf-8

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from model.vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from obs import *


# from my_tqdm import tqdm

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


if __name__ == '__main__':
    # bucketName, objName = getObjInfoFromObsEvent(event)
    # print(f"bucket name {bucketName} obj name {objName}")

    # sentence = event["queryStringParameters"]["sentence"]

    objName = 'sentence.txt'
    sentence = 'I am a powerful superman'
    print(f"sentence {sentence}")
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(sentence.strip())
    print(f'sentence {sentence} vs {vs}')

    ak = ""
    sk = ""
    server = "obs.cn-north-4.myhuaweicloud.com"

    downloadBucket = "*"
    uploadBucket = "*""

    objectKey = objName
    localFile = "./tmp/" + objectKey

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

    with open(localFile,'w') as writer:
        writer.write(str(vs))

    print("Upload file".center(50, "="))
    uploadFile(params=config)
