import numpy as np
import pandas as pd

# 因为原始数据association只包含有关联的circRNA-disease对，所以要加上随机抽一些数据作为没关联的circRNA-disease对，这里已经在excel处理过

trainset = pd.read_csv('data/trainset.csv', header=0, encoding='gb18030').values


meshdisname = pd.read_csv('data/Mesh_disease.csv', header=0, encoding='gb18030')
targetdisease = pd.read_csv('data/uniqueDisease.csv', header=0, encoding='gb18030')
targetrna = pd.read_csv('data/uniqueRna.csv', header=0, encoding='gb18030')

descriptor = pd.read_csv('output/descriptor.csv', header=0, encoding='gb18030')
descriptor = np.mat(descriptor)
descriptor = np.delete(descriptor, 0, axis=1)

rnaSim = pd.read_csv('output/rna_GaussianSimilarity.csv', header=0, encoding='gb18030')
rnaSim = np.mat(rnaSim)
rnaSim = np.delete(rnaSim, 0, axis=1)

result = np.mat(np.zeros(777))

# 这里在运行的过程中发现有部分RNA是circrna-disease association数据库中没有的，初步推断是来源于没有关联的数据，因为构建数据的时候
# 是从circrna-disease association数据库中提供的所有rna随机抽取的，也就是说，这里有些rna与所有disease都没有关系，所以之前计算高斯相似度的时候
# 没有结果
for i in range(len(trainset)):
    try:
        rna_index = targetrna[(targetrna.rna == str(trainset[i][0]))].index.tolist()
        disease_index = targetdisease[(targetdisease.disease == str(trainset[i][1]))].index.tolist()
        rnaSim_tmp = rnaSim[rna_index]
        descriptor_tmp = descriptor[disease_index]
        if trainset[i][2] == 1:
            label = np.mat(np.array([1]))
        else:
            label = np.mat(np.array([0]))
        result_tmp = np.hstack((rnaSim_tmp, descriptor_tmp, label))
        result = np.vstack((result, result_tmp))
    except:
        print(rna_index)
        print(disease_index)

result = np.delete(result, 0, axis=0)

# 保存结果

result = pd.DataFrame(result)
result.to_csv('output/transformed_trainset.csv')
# 注意，这样保存之后会多了一行一列行号序号，需要删除
