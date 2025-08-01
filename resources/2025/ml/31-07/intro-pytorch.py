import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    # PyTorch imports
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    import torch.optim as optim

    import warnings
    warnings.filterwarnings('ignore')

    # Set random seeds
    np.random.seed(42)
    torch.manual_seed(42)

    # Check if CUDA is available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    return nn, np, optim, plt, torch


@app.cell
def _():
    from tqdm import tqdm
    return (tqdm,)


@app.cell
def _(torch):
    x = torch.randn(3, 4)
    y = torch.randn(4, 2)
    z = torch.mm(x, y) # x @ y
    z
    return


@app.cell
def _(torch):
    u = torch.tensor([2.,], requires_grad=True)
    w = torch.tensor([3.,], requires_grad=True)
    v = u**2 + 3*u +1 + 3*w + 5*u*w 
    v.backward() 
    return (w,)


@app.cell
def _(w):
    w.grad
    return


@app.cell
def _(torch):
    X = torch.randn(1000, 10)
    Y = X**2 - 3*X + 2 + torch.randn(1000, 10)
    return X, Y


@app.cell
def _(X):
    X.shape
    return


@app.cell
def _(Y):
    Y.shape
    return


@app.cell
def _(nn, torch):
    class SimpleNet(nn.Module):
        def __init__(self, input_dim, hidden_dim, output_dim):
            super(SimpleNet, self).__init__()
            self.fc1 = nn.Linear(input_dim, hidden_dim)
            self.fc2 = nn.Linear(hidden_dim, output_dim)

        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = self.fc2(x)
            return x
    return (SimpleNet,)


@app.cell
def _(SimpleNet):
    det_model = SimpleNet(10, 500, 10)
    return (det_model,)


@app.cell
def _(X):
    X.squeeze().shape
    return


@app.cell
def _(X):
    X.shape
    return


@app.cell
def _(det_model, nn, optim):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(det_model.parameters(), lr=0.01)
    return criterion, optimizer


@app.cell
def _(X, Y, criterion, det_model, optimizer, tqdm):
    losses = []
    for epoch in tqdm(range(500)):
        optimizer.zero_grad()
        outputs = det_model(X)
        loss = criterion(outputs, Y)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
    
    return (losses,)


@app.cell
def _(losses, np, plt):
    plt.plot(np.arange(500), losses)
    return


@app.cell
def _(torch):
    func = lambda x: x**2 - 3*x + 2
    x_train = torch.linspace(-2, 2, 1000).reshape(-1, 1)
    y_train = func(x_train) + torch.randn(1000)
    return func, x_train, y_train


@app.cell
def _(SimpleNet):
    reglin = SimpleNet(1, 10, 1)
    return (reglin,)


@app.cell
def _(optim, reglin):
    optimizer2 = optim.Adam(reglin.parameters(), lr=0.01)
    return (optimizer2,)


@app.cell
def _(criterion, optimizer2, reglin, tqdm, x_train, y_train):
    for epoch2 in tqdm(range(500)):
        optimizer2.zero_grad()
        outputs2 = reglin(x_train)
        loss2 = criterion(outputs2, y_train)
        loss2.backward()
        optimizer2.step()
    return


@app.cell
def _(func, reglin, torch):
    x_test = torch.linspace(-4, 4, 100).reshape(-1, 1)
    y_pred = reglin(x_test)
    y_test = func(x_test)
    return x_test, y_pred, y_test


@app.cell
def _(plt, x_test, y_pred, y_test):
    plt.plot(x_test.detach().numpy(), y_pred.detach().numpy())
    plt.plot(x_test.detach().numpy(), y_test.detach().numpy())
    return


if __name__ == "__main__":
    app.run()
