import torch
import torch.nn as nn
import numpy as np
from utils.getdataset import getdataset
import matplotlib.pyplot as plt
import os

b_size, D_in, D_hid, D_out = 1000, 16*16, 100, 10

x,y = getdataset()

# Shuffle up our data
s = np.arange(x.shape[0])
np.random.shuffle(s)

x = x[s]
y = y[s]

x = torch.from_numpy(x).to(torch.float)
y = torch.from_numpy(y).to(torch.float)

x_train, x_test = x[:1000], x[:-593]
y_train, y_test = y[:1000], x[:-593]

model = nn.Sequential(
    nn.Linear(D_in, D_hid),
    nn.ReLU(),
    nn.Linear(D_hid, D_out)
)

learn = 0.001
epoch = 1000
loss_fn = nn.MSELoss(size_average=False)
optimizer = torch.optim.Adam(model.parameters(), lr=learn)

# training mode
model.train()

# train model
for e in range(epoch):
    # get our predictions
    y_pred = model(x_train)

    # calc loss
    loss = loss_fn(y_pred, y_train)
    print(f"e{e+1} loss: {loss.item()}")

    # model.zero_grad()
    optimizer.zero_grad()
    loss.backward()

    # with torch.no_grad():
    #     for param in model.parameters():
    #         param -= learn * param.grad
    optimizer.step()

# switch to testing mode
model.eval()
# test model
y_pred = model(x_test)

print(np.argmax(y_pred[0].detach().numpy()))
img = x_test[0].numpy().reshape((16,16))
plt.imsave(os.getcwd() + "\\test.png", img, cmap='binary')