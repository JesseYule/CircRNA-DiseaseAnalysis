import torch.optim as optim
import torch.nn as nn
import torch
from net import Net
import numpy as np
import pandas as pd
import random

# 读取数据
data = pd.read_csv('output/transformed_trainset.csv', header=0, encoding='gb18030')
data = np.mat(data)
data = np.delete(data, 0, axis=1)

traindata = torch.from_numpy(np.delete(data, -1, axis=1)).type('torch.DoubleTensor')
label = torch.from_numpy(data[:, -1]).type('torch.DoubleTensor')

NN = Net().double()
optimizer = optim.Adam(NN.parameters(), lr=1e-2)
loss_fn = nn.MSELoss()


for i in range(10000):
    train_acc = 0
    train_loss = 0
    min_loss = 1e5

    optimizer.zero_grad()

    idx = random.randint(0, 1469)

    input = traindata[idx]

    preds = NN(input)
    train_loss = loss_fn(preds, label[idx])

    if i % 100 == 0:
        print('train loss: ', train_loss)

    train_loss.backward()
    optimizer.step()
