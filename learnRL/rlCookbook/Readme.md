# Recipies from PyTorch 1.x Reinforcement LearningCookbook


## install pytorch , torchvision 
check if cuda is avaible 
torch.cuda.is_available()

>>> x = torch.empty(3,4)
>>> print(x)
tensor([[1.7204e-21, 4.5765e-41, 1.7204e-21, 4.5765e-41],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]])
## install gym
pip install gym

for atari envs
pip install gym[atari]
Alternatively, if you used the second approach in the previous recipe to install
gym , you can run the following command instead:
pip install -e '.[atari]'


