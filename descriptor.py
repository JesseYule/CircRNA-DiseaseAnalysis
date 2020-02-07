import numpy as np
import pandas as pd

# 读取数据

similarity1 = pd.read_csv('output/similarity1.csv', header=0, encoding='gb18030').values
similarity2 = pd.read_csv('output/similarity2.csv', header=0, encoding='gb18030').values
similarity1 = np.mat(similarity1)
similarity2 = np.mat(similarity2)

# 原始数据会有一行一列是序号，所以要删除，之前读数据的时候已经通过header=0删除了第一行，现在删除第一列，其他类似的操作也是一样目的
similarity1 = np.delete(similarity1, 0, axis=1)
similarity2 = np.delete(similarity2, 0, axis=1)

# print(similarity1.shape)
# 矩阵尺寸为4818行4818列

disease_GaussianSimilarity = pd.read_csv('output/disease_GaussianSimilarity.csv', header=0, encoding='gb18030').values
disease_GaussianSimilarity = np.mat(disease_GaussianSimilarity)
disease_GaussianSimilarity = np.delete(disease_GaussianSimilarity, 0, axis=1)


meshdisname = pd.read_csv('data/Mesh_disease.csv', header=0, encoding='gb18030')
targetdisease = pd.read_csv('data/uniqueDisease.csv', header=0, encoding='gb18030').values

# 构建descriptor
descriptor = disease_GaussianSimilarity  # 先用circrnadisease计算的相似度作为descriptor，如果两个疾病在MeSH中出现就用MeSh计算的相似度代替

# 开始构建descriptor

for m in range(len(targetdisease)):
    for n in range(len(targetdisease)):
        mesh_m = meshdisname[(meshdisname.C1 == str(targetdisease[m]))].index.tolist()
        mesh_n = meshdisname[(meshdisname.C1 == str(targetdisease[n]))].index.tolist()
        if mesh_m:
            if mesh_n:
                descriptor[m, n] = (similarity1[mesh_m, mesh_n] + similarity2[mesh_m, mesh_n])*0.5
                print("替换成功")  # 事实证明，两个数据库可能因为命名不统一，根本找不到相同的病

        if m == n:
            descriptor[m, n] = 1


# 保存结果

result = pd.DataFrame(descriptor)
result.to_csv('output/descriptor.csv')
# 注意，这样保存之后会多了一行一列行号序号，需要删除


