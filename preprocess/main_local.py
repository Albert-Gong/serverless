from obs import *
import numpy as np
from common import *
from integration import *
import json


if __name__ == '__main__':
    # ak = 'VFQ6DYBAKATE373J1OSX'
    # sk = 'r97RMrH2xqEbYSSoDR43OEtMgAdSu6AmuPPCMiQg'
    ak = 'TXKLMML0EK5IMB3MRGES'
    sk = 'GTRm8WLamcrpFGmuKtHiYU4YBPFiDKFvqbdTSXR4'
    server = "obs.cn-north-4.myhuaweicloud.com"

    downloadBucket = "serverless-preprocess-stage-0"
    uploadBucket = "pre-fillmissing"

    objectKey = 'nan.csv'
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
    #
    # print("Download file".center(50, "="))
    # downloadFile(params=config)
    #
    # control, data = decode_file(localFile)
    # print(f'control {control}')
    # print(f'data \n {data}')
    #
    # func = func_mapper[control["cmd"]]
    # result = func(data, control["params"])
    # print(result)
    #
    # np.savetxt(localFile, result, delimiter=",", fmt='%.6f')
    #
    # print("Upload file".center(50, "="))
    uploadFile(params=config)

