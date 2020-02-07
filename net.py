import torch.nn as nn


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.fc1 = nn.Linear(776, 1400)
        self.fc2 = nn.Linear(1400, 2000)
        self.fc3 = nn.Linear(2000, 500)
        self.fc4 = nn.Linear(500, 2)
        self.relu = nn.ReLU()

    def forward(self, x):

        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        out = self.relu(out)
        out = self.fc4(out)
        return out
