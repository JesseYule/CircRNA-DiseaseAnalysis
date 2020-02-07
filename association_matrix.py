import numpy as np
import pandas as pd

# 读取数据

disease_df = pd.read_csv('data/disease.csv', header=0, encoding='gb18030')
disease = disease_df['disease'].tolist()

rna_df = pd.read_csv('data/rna.csv', header=0, encoding='gb18030')
rna = rna_df['RNA'].tolist()

association_df = pd.read_csv('data/association.csv', header=0, encoding='gb18030')

print(len(association_df))


uniqueRna_df = pd.read_csv('data/uniqueRna.csv', header=0, encoding='gb18030')
unique_rna = uniqueRna_df['rna'].tolist()

uniqueDisease_df = pd.read_csv('data/uniqueDisease.csv', header=0, encoding='gb18030')
unique_disease = uniqueDisease_df['disease'].tolist()

print(len(unique_rna))
print(len(unique_disease))


association_matrix = np.zeros([len(unique_rna), len(unique_disease)])

# 计算association_matrix
count = 0
for m in range(len(unique_rna)):
    for n in range(len(unique_disease)):
        if len(association_df[np.logical_and(association_df['rna'] == unique_rna[m],
                                             association_df['disease'] == unique_disease[n])]):
            association_matrix[m, n] = 1
            count += 1
print(count)
print(association_matrix[0: 10, 0: 10])


# 保存结果
# rna: 676, disease: 100
# 最后得到725个关系，比原始少了14个，因为这14个是重复的（如果单看rna和disease）

result = pd.DataFrame(association_matrix)
result.to_csv('output/association_matrix.csv')
# 注意，这样保存之后会多了一行一列行号序号，需要删除
