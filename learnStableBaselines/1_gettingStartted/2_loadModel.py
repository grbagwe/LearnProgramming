import gym # gym contains all the env
from stable_baselines3 import A2C # importing actor critic algorithm

env = gym.make('CartPole-v1')
model  = A2C.load('1_exampleSBModel')

# test the env
obs = env.reset()
score = 0
for i in range(1000):
    action, _state = model.predict(obs, deterministic=True) # predict and action from the current state
    obs, reward, done , info = env.step(action) # execute the action
    env.render()
    score +=reward # add the rewards for the score
    if done:
        obs = env.reset()
        print(f'score = {score}')
        score = 0 # reset the score for the next episode

# randoms actions not from the policy

# test the env
obs = env.reset()
score = 0
for i in range(100):
    action = env.action_space.sample() # take random action from the env
    obs, reward, done , info = env.step(action) # execute the action
    env.render()
    score +=reward # add the rewards for the score
    if done:
        obs = env.reset()
        print(f'score for random action = {score}')
        score = 0 # reset the score for the next episode

# untrained policy
model = A2C('MlpPolicy', env, verbose=2) # create a model

# test the env

obs = env.reset()
score = 0
for i in range(100):
    action, _state = model.predict(obs, deterministic=True) # predict and action from the current state
    obs, reward, done , info = env.step(action) # execute the action
    env.render()
    score +=reward # add the rewards for the score
    if done:
        obs = env.reset()
        print(f'score for untrained policy = {score}')
        score = 0 # reset the score for the next episode






