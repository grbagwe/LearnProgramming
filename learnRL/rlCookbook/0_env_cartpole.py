import gym
env = gym.make('CartPole-v0')
# videoDir = './savedvideo/cartpole/'
# env = gym.wrappers.Monitor(env, videoDir)

'''save the video monitor has removed from gym '''

is_done = False



env.reset()
total_rewards  = 0
while not is_done:
    action = env.action_space.sample()
    state_, reward , is_done, info = env.step(action)
    env.render()
    total_rewards += reward
print(total_rewards)

