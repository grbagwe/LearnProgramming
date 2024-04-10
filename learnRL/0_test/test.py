# test the gym installation

import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="rgb_array") # load an env

obs , info = env.reset(seed=42)

for _ in range(1000):
  action = env.action_space.sample() # taking random actions
  obs , reward, terminated, truncated, info = env.step(action)
  env.render() 
  print(action, reward)
  if terminated or truncated:
    obs, info = env.reset()
env.close()

