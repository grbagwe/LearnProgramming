import torch

# random torch
x = torch.rand(3,4)
print(x)

# torch with zeros
x = torch.zeros(3,4)

print(x)

# ones

x = torch.ones(3,4)
print(x)

# size

print(x.size)

# random
x = torch.rand(3,4)
x_reshape = x.view(2,6)
print(x_reshape)

# access each elemet
print(x[1])
print(x[1,2])
print(x[:,1]) # all rows and first column
print(x[1,:]) # all columns and first row

# to numpy
y = x.numpy()
print(y)




