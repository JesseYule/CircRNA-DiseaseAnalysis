import math
import numpy as np
import pandas as pd

# disease = ["Meningitis, Pneumococcal", "Meningitis, Pneumococcal", "Mycetoma", "Botulism", "Botulism2", "Botulism3"]
# id = ["C01.252.200.500.600", "C08.345.654.570", "C01.252.410.040.692.606", "C01.252.410.222.151", "C01.252.410.222.151", "C03.252.410.222.151"]

print("开始读取数据")
# 读取数据
meshid = pd.read_csv('data/MeSHID.csv', header=0)
disease = meshid['disease'].tolist()
id = meshid['ID'].tolist()

meshdis = pd.read_csv('data/Mesh_disease.csv', header=0)
unique_disease = meshdis['C1'].tolist()

# 先把各个病的整个家族储存到一个list中，把所有病储存到一个fullID中

disease_list = []
fullID = []

for i in range(len(id)):

    disease_family = [disease[i], id[i]]
    fullID.append(id[i])
    if len(id[i]) > 3:
        id[i] = id[i][:-4]
        disease_family.append(id[i])
        fullID.append(id[i])
        if len(id[i]) > 3:
            id[i] = id[i][:-4]
            disease_family.append(id[i])
            fullID.append(id[i])
            if len(id[i]) > 3:
                id[i] = id[i][:-4]
                disease_family.append(id[i])
                fullID.append(id[i])
                if len(id[i]) > 3:
                    id[i] = id[i][:-4]
                    disease_family.append(id[i])
                    fullID.append(id[i])
                    if len(id[i]) > 3:
                        id[i] = id[i][:-4]
                        disease_family.append(id[i])
                        fullID.append(id[i])
                        if len(id[i]) > 3:
                            id[i] = id[i][:-4]
                            disease_family.append(id[i])
                            fullID.append(id[i])
                            if len(id[i]) > 3:
                                id[i] = id[i][:-4]
                                disease_family.append(id[i])
                                fullID.append(id[i])
                                if len(id[i]) > 3:
                                    id[i] = id[i][:-4]
                                    disease_family.append(id[i])
                                    fullID.append(id[i])

    disease_list.append(disease_family)


id = meshid['ID'].tolist()


# 计算每个病的DV，用字典形式创建list

# 计算每个病在所有病中的出现次数,构建字典

# 方法一:
# 现在有fullID，用fullID和原始ID对比，对fullID中某一个ID，看有多少个原始ID包含它
# countID = []
#
# for i in range(len(fullID)):
#     target = fullID[i]
#     count = 0
#     for j in range(len(id)):
#         if target in id[j]:
#             count += 1
#     countID.append(count)
#
# print(countID)

# 方法二
# 直接统计fullID中每个ID的出现次数，因为每个病的集合中的元素都是唯一的，所以如果一个ID出现了，就证明这个ID在这个病中，所以一个ID出现多少次就证明有多少个病包含这个ID

disease_dv = {}
countdis = len(disease)

for key in fullID:
    disease_dv[key] = round(math.log((disease_dv.get(key, 0) + 1)/countdis, 10)*(-1), 5)

# print(disease_dv)
#
# print(disease_list)
#
# print(fullID)


id = meshid['ID'].tolist()
disease = meshid['disease'].tolist()

# 初始化字典，有重复也没关系
for i in range(len(disease)):
    disease[i] = {}

# 计算每个病的DV，又重复也没关系，之后再合并

for i in range(len(disease)):

    if len(id[i]) > 3:
        disease[i][id[i]] = disease_dv[id[i]]
        id[i] = id[i][:-4]
        # print(disease[i])
        if len(id[i]) > 3:
            disease[i][id[i]] = disease_dv[id[i]]
            id[i] = id[i][:-4]
            # print(disease[i])
            if len(id[i]) > 3:
                disease[i][id[i]] = disease_dv[id[i]]
                id[i] = id[i][:-4]
                # print(disease[i])
                if len(id[i]) > 3:
                    disease[i][id[i]] = disease_dv[id[i]]
                    id[i] = id[i][:-4]
                    # print(disease[i])
                    if len(id[i]) > 3:
                        disease[i][id[i]] = disease_dv[id[i]]
                        id[i] = id[i][:-4]
                        # print(disease[i])
                        if len(id[i]) > 3:
                            disease[i][id[i]] = disease_dv[id[i]]
                            id[i] = id[i][:-4]
                            # print(disease[i])
                            if len(id[i]) > 3:
                                disease[i][id[i]] = disease_dv[id[i]]
                                id[i] = id[i][:-4]
                                # print(disease[i])
                                if len(id[i]) > 3:
                                    disease[i][id[i]] = disease_dv[id[i]]
                                    id[i] = id[i][:-4]
                                    # print(disease[i])
                                else:
                                    disease[i][id[i][:3]] = disease_dv[id[i][:3]]
                                    # print(disease[i])
                            else:
                                disease[i][id[i][:3]] = disease_dv[id[i][:3]]
                                # print(disease[i])
                        else:
                            disease[i][id[i][:3]] = disease_dv[id[i][:3]]
                            # print(disease[i])
                    else:
                        disease[i][id[i][:3]] = disease_dv[id[i][:3]]
                        # print(disease[i])
                else:
                    disease[i][id[i][:3]] = disease_dv[id[i][:3]]
                    # print(disease[i])
            else:
                disease[i][id[i][:3]] = disease_dv[id[i][:3]]
                # print(disease[i])
        else:
            disease[i][id[i][:3]] = disease_dv[id[i][:3]]
            # print(disease[i])
    else:
        disease[i][id[i][:3]] = disease_dv[id[i][:3]]
        # print(disease[i])

# print(disease)


# 合并相同的病不同ID的DV

unique_disease = meshdis['C1'].tolist()

# 这个name用来判断
disease_name = meshid['disease'].tolist()
unique_disease_name = meshdis['C1'].tolist()

for i in range(len(unique_disease)):
    unique_disease[i] = {}
    for j in range(len(disease_name)):
        if unique_disease_name[i] == disease_name[j]:
            unique_disease[i].update(disease[j])

# print(unique_disease)


similarity = np.zeros([len(unique_disease_name), len(unique_disease_name)])


for m in range(len(unique_disease_name)):
    for n in range(len(unique_disease_name)):
        denominator = sum(unique_disease[m].values()) + sum(unique_disease[n].values())
        numerator = 0
        for k, v in unique_disease[m].items():
            if k in unique_disease[n].keys():
                numerator += v + unique_disease[n].get(k)
        similarity[m, n] = round(numerator/denominator, 5)

# print(similarity)

# 保存结果

result = pd.DataFrame(similarity)
result.to_csv('output/similarity2.csv')
