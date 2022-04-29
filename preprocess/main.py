from obs import *
import numpy as np
import pandas as pd
from common import *
from integration import *


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
    print(f'control {control}')
    print(f'data \n {data}')

    func = func_mapper[control["cmd"]]
    result = func(data, control["params"])
    print(result)

    np.savetxt(localFile, result, delimiter=",", fmt='%.6f')

    print("Upload file".center(50, "="))
    uploadFile(params=config)

    # print("Normalize".center(50, "="))
    # nor_norm(localFile)
    #
    # print("Upload file".center(50, "="))
    # uploadFile(params=config)

    # objects = obsClient.listObjects(bucketName="serverless-preprocess")
    # print(objects["body"])
