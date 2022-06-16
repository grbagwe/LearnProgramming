from stable_baselines3 import SAC
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import VecNormalize, VecFrameStack

env = make_vec_env('CarRacing-v0', n_envs=10)
# The following does not work:
# env = VecNormalize(env)
# env = VecFrameStack(env, 4)

# But this works:
print(env.observation_space.sample().shape)
print(env.reset())

#env = VecFrameStack(env, 4)
#print(env.observation_space.sample().shape, env.reset().shape)


#env = VecNormalize(env)
#print(env.observation_space.sample().shape, env.reset().shape)

#model = SAC('MlpPolicy', env, verbose=1)
#model.learn(10000)
