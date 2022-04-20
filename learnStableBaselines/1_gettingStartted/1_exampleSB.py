import gym # gym contains all the env
from stable_baselines3 import A2C # importing actor critic algorithm

env = gym.make('CartPole-v1')
model = A2C('MlpPolicy', env, verbose=2)

model.learn(total_timesteps=1e4)


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
#save the model
model.save('./1_exampleSBModel')

