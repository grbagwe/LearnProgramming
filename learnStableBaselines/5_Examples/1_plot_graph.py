import os.path

from stable_baselines3 import A2C

model = A2C('MlpPolicy', 'CartPole-v1', verbose=1, tensorboard_log="./a2c_cartpole_tensorboard/")

for i in range(1,300):
    model.learn(total_timesteps=10_000, tb_log_name=f"{i * 10000} run", reset_num_timesteps=False)
    model.save(os.path.join('./a2c_cartpole_tensorboard/', f'checkpoint{i*10000}'))
# Pass reset_num_timesteps=False to continue the training curve in tensorboard
# By default, it will create a new curve
# model.learn(total_timesteps=10_000, tb_log_name="second_run", reset_num_timesteps=False)
# model.learn(total_timesteps=10_000, tb_log_name="third_run", reset_num_timesteps=False)