from ray.rllib.agents.ppo import PPOTrainer

config = {
    # this is a dict
    "env" : "CartPole-v0",
    "num_workers": 4,
    "framework" : "torch",
    "num_gpus" : 1 ,
    "model" : {

        "fcnet_hiddens" : [64, 64 ],
        "fcnet_activation" : "relu",

    },
    "evaluation_num_workers": 1,
    # Only for evaluation runs, render the env.
    "evaluation_config": {
        "render_env": True,
    }

}


# this is a basic rrllib trainer
# trainer = PPOTrainer(config= config)
# for _ in range(10):
#     print(trainer.train())

# or train this with tune
from ray import tune
tune.run(PPOTrainer, config=config)
# trainer.evaluate()
