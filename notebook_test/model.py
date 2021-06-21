import torch
import torch.nn as nn


class TestModule(nn.Module):

    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(nn.Conv2D(1, 1, 1))


    def forward(self, x):
        return torch.sigmoid(self.net(x))
