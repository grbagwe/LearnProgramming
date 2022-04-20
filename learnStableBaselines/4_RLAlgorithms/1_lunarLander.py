import gym
import wandb
from wandb.integration.sb3 import WandbCallback  # to save the logs
from stable_baselines3 import PPO

# print(gym.envs.registry.all())

# create the env
env = gym.make("LunarLander-v2")
env.reset()

# create the model
model = PPO('MlpPolicy', env, verbose=0)
# logging using weigths and biases


# config = {
#     "policy_type": "MlpPolicy",
#     "total_timesteps": 1e5,
#     "env_name": "LunarLander-v2",
# }
# run = wandb.init(
#     project="4_1_lunarlander",
#     config=config,
#     sync_tensorboard=True,  # auto-upload sb3's tensorboard metrics
#     monitor_gym=True,  # auto-upload the videos of agents playing the game
#     save_code=True,  # optional
# )

# train the model
model.learn(total_timesteps=1e6)  # callbacks saves all logs like tensorboard
# save the model
model.save("./1_modelLunarLanderPPO")
# delete model
del model
# load the model
model.load("1_modelLunarLanderPPO")
obs = env.reset()
done = False
# run prediction or testing

while not done:  # while the episode has not ended
    action, _ = model.predict(obs)  # take action from the current observation for the trained policy
    obs_, reward, done, _ = env.step(action)  # execute that action
    env.render()  # render the env
