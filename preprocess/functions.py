# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


# 查找缺失值
def ismissing(data):
    row, col = data.shape
    result = np.zeros((row, col))
    for i in range(0, row):
        for j in range(0, col):
            if np.isnan(data[i][j]):
                result[i][j] = 1
    return result.astype(int)


# 删除缺失条目
def rmmissing(data):
    row, col = data.shape
    row_new = []
    for i in range(0, row):
        count = 0
        for j in range(0, col):
            if not np.isnan(data[i][j]):
                count += 1
            if count == col:
                row_new.append(i)
    result = np.zeros((len(row_new), col))
    for i in range(0, len(row_new)):
        for j in range(0, col):
            result[i][j] = data[row_new[i]][j]
    return result.round(4)


# 替换缺失值（均值）
def fillmissing(data):
    row, col = data.shape
    result = np.copy((row, col))
    for i in range(0, row):
        for j in range(0, col):
            if data[i][j].isnull():
                data[i][j] = np.nan
            if np.isnan(data[i][j]):
                result[i][j] = np.nanmean(np.transpose(data)[j])
    return result.round(4)


# 查找离群值
def isoutliers(data):
    row, col = data.shape
    print(row, col)
    result = np.zeros((row, col))
    for i in range(0, row):
        for j in range(0, col):
            Q1 = pd.DataFrame(np.transpose(data)[j]).quantile(0.25)
            Q3 = pd.DataFrame(np.transpose(data)[j]).quantile(0.75)
            IQR = Q3 - Q1
            if ((data[i][j] < float(Q1 - 1.5 * IQR)) | (data[i][j] > float(Q3 + 1.5 * IQR))):
                result[i][j] = 1
    return result.astype(int)


# 替换离群值（均值）
def filloutliers(data):
    row, col = data.shape
    result = np.copy(data)
    flag = isoutliers(data)
    for i in range(0, row):
        sum = 0
        num = 0
        for j in range(0, col):
            if flag[i][j] == 0:
                sum += data[i][j]
                num += 1
        for j in range(0, col):
            if flag[i][j] == 1:
                result[i][j] = sum / num
    return result.round(4)


# 删除离群值
def rmoutliers(data):
    row, col = data.shape
    row_new = []
    flag = isoutliers(data)
    for i in range(0, row):
        count = 0
        for j in range(0, col):
            if flag[i][j] == 0:
                count += 1
            if count == col:
                row_new.append(i)
    result = np.zeros((len(row_new), col))
    for i in range(0, len(row_new)):
        for j in range(0, col):
            result[i][j] = data[row_new[i]][j]
    return result.round(4)

    return result.round(4)


# 移动中位数偏差
def movmad(data, windowSize=3):
    row, col = data.shape
    result = np.zeros((row, col))
    left = int((windowSize - 1) / 2 + 1) if (windowSize % 2 == 0) else int((windowSize - 1) / 2)
    right = int((windowSize - 1) / 2)
    for j in range(0, col):
        for i in range(0, row):
            _left = (i - left) if (i - left > 0) else 0
            _right = (i + right + 1) if (i + right < row - 1) else row
            arr1 = []
            arr2 = []
            for k in range(_left, _right):
                arr1.append(data[k][j])
            for k in range(0, len(arr1)):
                arr2.append(np.abs(arr1[k] - np.median(arr1)))
            result[i][j] = np.median(arr2)
    return result.round(4)


# 移动均值
def movmean(data, windowSize=3):
    row, col = data.shape
    result = np.zeros((row, col))
    left = int((windowSize - 1) / 2 + 1) if (windowSize % 2 == 0) else int((windowSize - 1) / 2)
    right = int((windowSize - 1) / 2)
    for j in range(0, col):
        for i in range(0, row):
            _left = (i - left) if (i - left > 0) else 0
            _right = (i + right + 1) if (i + right < row - 1) else row
            sum = 0
            for k in range(_left, _right):
                sum += data[k][j]
            result[i][j] = sum / (_right - _left)
    return result.round(4)


# 移动中位数
def movmedian(data, windowSize=3):
    row, col = data.shape
    result = np.zeros((row, col))
    left = int((windowSize - 1) / 2 + 1) if (windowSize % 2 == 0) else int((windowSize - 1) / 2)
    right = int((windowSize - 1) / 2)
    for j in range(0, col):
        for i in range(0, row):
            _left = (i - left) if (i - left > 0) else 0
            _right = (i + right + 1) if (i + right < row - 1) else row
            arr = []
            for k in range(_left, _right):
                arr.append(data[k][j])
            result[i][j] = np.median(arr)
    return result.round(4)
