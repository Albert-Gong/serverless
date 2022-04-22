import numpy as np


def nor_norm(localFile, fileName):
    array = np.loadtxt(open(localFile, "rb"), delimiter=",", skiprows=0)

    data_shape = array.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    t = np.empty((data_rows, data_cols))
    # 求每一列的均值和标准差，并据此将标准化结果算出
    for i in range(data_cols):
        sum = 0
        for j in range(data_rows):
            sum += array[j, i]
        avg = sum / data_rows
        # 标准差
        sum_sq = 0
        for j in range(data_rows):
            sq = (array[j, i] - avg) ** 2
            sum_sq += sq
        std_deviation = (sum_sq / data_rows) ** 0.5
        # 计算标准化结果
        for j in range(data_rows):
            t[j, i] = (array[j, i] - avg) / std_deviation

    outFilePath = "/tmp/" + fileName
    np.savetxt(outFilePath, t, delimiter=",")
