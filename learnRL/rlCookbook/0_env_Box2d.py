import gym
env = gym.make('LunarLander-v2')
env.reset()
is_done = False
while not is_done:
    action = env.action_space.sample()
    state_, reward , is_done, info = env.step(action)
    print(reward, is_done, info)
    env.render()
