import gym

env = gym.make('SpaceInvaders-v0', render_mode='human')
env.reset()

is_done = False

while not is_done:
    action = env.action_space.sample()
    state_, reward, is_done, info = env.step(action)
    print(info)
