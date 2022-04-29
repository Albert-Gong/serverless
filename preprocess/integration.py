import numpy as np
import pandas as pd

'''
    a class used by discretization
'''


class DiscreteByEntropy:
    def __init__(self, group, threshold):
        self.maxGroup = group  # 最大分组数
        self.minInfoThreshold = threshold  # 停止划分的最小熵
        self.result = dict()

    # 计算按照数据指定数据分组后的Shannon熵
    def calEntropy(self, data):
        numData = len(data)
        labelCounts = {}
        for feature in data:
            # 获得标签,这里只有0或者1
            oneLabel = feature[-1]
            # 设置字典中，标签的默认值
            if labelCounts.get(oneLabel, -1) == -1:
                labelCounts[oneLabel] = 0
            # 统计同类标签的数量
            labelCounts[oneLabel] += 1
        shannoEnt = 0.0
        for key in labelCounts:
            # 同类标签出现的概率,某一标签出现的次数除以所有标签的数量
            prob = float(labelCounts[key]) / numData
            # 求熵，以2为底，取对数
            shannoEnt -= prob * np.log2(prob)
        return shannoEnt

    # 按照调和信息熵最小化原则分割数据集
    def split(self, data):
        # inf为正无穷
        minEntropy = np.inf
        # 记录最终分割的索引
        index = -1
        # 按照第一列对数据进行排序
        sortData = data[np.argsort(data[:, 0])]
        # print(sortData)
        # 初始化最终分割数据后的熵
        lastE1, lastE2 = -1, -1
        # 返回的数据区间，包括数据和对应的熵
        S1 = dict()
        S2 = dict()
        for i in range(len(data)):
            splitData1, splitData2 = sortData[:i + 1], sortData[i + 1:]
            # 计算信息熵
            entropy1, entropy2 = (
                self.calEntropy(splitData1),
                self.calEntropy(splitData2)
            )
            # 计算调和平均熵
            entropy = entropy1 * len(splitData1) / len(sortData) + entropy2 * len(splitData2) / len(sortData)
            if entropy < minEntropy:
                minEntropy = entropy
                index = i
                lastE1 = entropy1
                lastE2 = entropy2
        S1["entropy"] = lastE1
        S1["data"] = sortData[:index + 1]
        S2["entropy"] = lastE2
        S2["data"] = sortData[index + 1:]
        return S1, S2, entropy

    def train(self, data):
        # 需要遍历的key
        needSplitKey = [0]

        self.result.setdefault(0, {})
        self.result[0]["entropy"] = np.inf
        self.result[0]["data"] = data

        group = 1
        for key in needSplitKey:
            S1, S2, entropy = self.split(self.result[key]["data"])
            if entropy > self.minInfoThreshold and group < self.maxGroup:
                self.result[key] = S1
                newKey = max(self.result.keys()) + 1
                self.result[newKey] = S2
                needSplitKey.extend([key])
                needSplitKey.extend([newKey])
                group += 1
            else:
                break


'''
    normalize 
'''


def normalize(array=None, params=None):
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
        for j in range(data_rows):
            t[j, i] = (array[j, i] - avg) / std_deviation
    return t


'''
    find missing
'''


def ismissing(data=None, params=None):
    row, col = data.shape
    result = np.zeros((row, col))
    for i in range(0, row):
        for j in range(0, col):
            if np.isnan(data[i][j]):
                result[i][j] = 1
    return result.astype(int)


'''
    remove missing items
'''


def rmmissing(data=None, params=None):
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
    return result.round(6)


'''
    fill missing with mean
'''


def fillmissing(data=None, params=None):
    row, col = data.shape
    result = np.copy(data)
    for i in range(0, row):
        for j in range(0, col):
            if np.isnan(data[i][j]):
                result[i][j] = np.nanmean(np.transpose(data)[j])
    return result.round(6)


'''
    find outliers
'''


def isoutliers(data=None, params=None):
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


'''
    substitute outliers for mean
'''


def filloutliers(data=None, params=None):
    row, col = data.shape
    result = np.copy(data)
    flag = np.zeros((row, col))
    for i in range(0, row):
        for j in range(0, col):
            Q1 = pd.DataFrame(np.transpose(data)[j]).quantile(0.25)
            Q3 = pd.DataFrame(np.transpose(data)[j]).quantile(0.75)
            IQR = Q3 - Q1
            if ((data[i][j] < float(Q1 - 1.5 * IQR)) | (data[i][j] > float(Q3 + 1.5 * IQR))):
                flag[i][j] = 1
    for i in range(0, col):
        sum = 0
        num = 0
        for j in range(0, row):
            if flag[j][i] == 0:
                sum += data[j][i]
                num += 1
        for j in range(0, row):
            if flag[j][i] == 1:
                print(sum)
                print(num)
                result[j][i] = sum / num
    return result.round(6)


'''
    remove outliers
'''


def rmoutliers(data=None, params=None):
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
    return result.round(6)


'''
    move median with deviation
'''


def movmad(data=None, params=None):
    windowSize = int(params[0])
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
    return result.round(6)


'''
    move mean
'''


def movmean(data=None, params=None):
    windowSize = int(params[0])
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
    return result.round(6)


'''
    move median 
'''


def movmedian(data=None, params=None):
    windowSize = int(params[0])
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
    return result.round(6)


'''
    reduce dimension with pca
'''


def pca(data=None, params=None):
    n_components = int(params[0])
    if n_components > 0:
        num_instances, num_events = data.shape
        X_cov = np.dot(data.T, data) / float(num_instances)
        U, sigma, V = np.linalg.svd(X_cov)
        P = U[:, :n_components]
        return P
    return None

'''
    correlation
'''


def correlation(array=None, params=None):
    data_shape = array.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    t = np.corrcoef(array)
    return t


'''
    discretize
'''


def discretize(array=None, params=None):
    group = params[0]
    threshold = params[1]
    dbe = DiscreteByEntropy(group=group, threshold=threshold)
    dbe.train(array)
    return dbe.result


'''
    groupby
'''


def groupBy(array=None, params=None):
    return


#     df = pd.read_csv(localFile, encoding='GB2312')
#     name = fileName.split('.')
#     outFileName = name[0] + '-groups.txt'
#     outFilePath = "/tmp/" + outFileName
#     m, n = df.shape
#     list = df.columns.values
#     df1 = df[list]
#
#     for i in list:
#         print("下面是对属性" + i + "的统计\n")
#         with open(outFilePath, 'a') as file:
#             file.write("\n下面是对属性" + i + "的分组统计\n")
#         for name, group in df1.groupby(i):
#             print(name)
#             print("=============================\n")
#             print(group)
#             print("==================================================\n")
#             with open(outFilePath, 'a') as file:
#                 file.write(str(name))
#                 file.write("\n=============================\n")
#                 file.write(str(group))
#                 file.write("\n==================================================\n")
#
#     return outFileName, outFilePath


def groupCount(localFile, fileName):
    df = pd.read_csv(localFile, encoding='GB2312')
    name = fileName.split('.')
    outFileName = name[0] + '-groupscount.txt'
    outFilePath = "/tmp/" + outFileName
    m, n = df.shape
    list = df.columns.values
    df1 = df[list]

    for i in list:
        print("下面是对属性" + i + "的统计\n")
        countGroup = [[i, 'count']]
        for name, group in df1.groupby(i):
            n, m = group.shape
            count = n - 1
            countGroup.append([name, count])
            # print(pd.DataFrame(countGroup))
        ddd = pd.DataFrame(countGroup)
        ddd.to_csv(outFilePath, header=None, index=None, mode='a')

    return outFileName, outFilePath


def removeRedundance(data=None, params=None):
    tmp = data
    if data.duplicated().any() == True:
        print("*** 该数据集存在冗余")
        tmp = data.drop_duplicates()
        print("*** 冗余已消除！")
    else:
        print("*** 该数据集不存在冗余，无需处理！")
    return tmp


def rescale(array=None, params=None):
    rescale_max = params[0]
    rescale_min = params[1]
    maxcols = array.max(axis=0)
    mincols = array.min(axis=0)
    data_shape = array.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    t = np.empty((data_rows, data_cols))
    for i in range(data_cols):
        t[:, i] = (array[:, i] - mincols[i]) * (rescale_max - rescale_min) / (maxcols[i] - mincols[i]) + rescale_min
    return t


def create_x(size, rank):
    x = []
    for i in range(2 * size + 1):
        m = i - size
        row = [m ** j for j in range(rank)]
        x.append(row)
    x = np.mat(x)
    return x


def savgol(data, window_size, rank):
    m = (window_size - 1) // 2
    odata = data[:]
    # 处理边缘数据，首尾增加m个首尾项
    for i in range(m):
        odata = np.insert(odata, 0, odata[0])
        odata = np.insert(odata, len(odata), odata[len(odata) - 1])
    # 创建X矩阵
    x = create_x(m, rank)
    # 计算加权系数矩阵B
    b = (x * (x.T * x).I) * x.T
    a0 = b[m]
    a0 = a0.T
    # 计算平滑修正后的值
    ndata = []
    for i in range(len(data)):
        y = [odata[i + j] for j in range(window_size)]
        y1 = np.mat(y) * a0
        y1 = float(y1)
        ndata.append(y1)
    return ndata


def smooth(array=None, params=None):
    window_size = params[0]
    rank = params[1]
    t = savgol(array, window_size, rank)
    return t


def standardizing(array=None, params=None):
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
    return t


def basic(array=None, params=None):
    mx = np.max(array, axis=0)
    mn = np.min(array, axis=0)
    me = np.mean(array, axis=0)
    std = np.std(array, axis=0)
    return np.asarray([mx, mn, me, std])


func_mapper = {
    "normalize": normalize,
    "standardizing": standardizing,
    "rescale": rescale,
    "discretize": discretize,
    "groupBy": groupBy,
    "groupCount": groupCount,
    "smooth": smooth,
    "removeRedundance": removeRedundance,
    "correlation": correlation,
    "ismissing": ismissing,
    "rmmissing": rmmissing,
    "fillmissing": fillmissing,
    "isoutliers": isoutliers,
    "rmoutliers": rmoutliers,
    "filloutliers": filloutliers,
    "movmad": movmad,
    "movmean": movmean,
    "movmedian": movmedian,
    "pca": pca,
    "basic": basic,
}
