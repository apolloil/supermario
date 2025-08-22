from stable_baselines3 import PPO  # 算法框架
from make_env import make_env  # 创建环境
from stable_baselines3.common.vec_env import SubprocVecEnv, VecFrameStack
from stable_baselines3.common.callbacks import EvalCallback
import torch

if __name__ == "__main__":
    n_envs = 18
    env = SubprocVecEnv([make_env for _ in range(n_envs)])
    env = VecFrameStack(env, n_stack=4)

    best_model_path = "best_model/best_model.zip"
    eval_callback = EvalCallback(
        env,
        best_model_save_path="best_model",
        eval_freq=80_000//n_envs,
        n_eval_episodes=10,
        log_path="logs",
    )
    model_params = {
        "learning_rate": lambda remaining_progress: 3e-4 * remaining_progress,
        "device": "cuda",
        "verbose": 1,
        "tensorboard_log": "logs",
        "batch_size": 4096,
        "n_steps": 1024,
        "n_epochs": 10,
        "ent_coef": 0.05,
        "vf_coef": 0.5,
        "target_kl": 0.15,
        "max_grad_norm": 0.5,
        "gamma": 0.93,
        "policy_kwargs": {
            "optimizer_class": torch.optim.AdamW,
            "optimizer_kwargs": {"weight_decay": 1e-5}
        }
    }

    # 第一轮训练
    # model = PPO("CnnPolicy", env, **model_params)
    # 后面的训练在前面模型的基础上进行继续训练
    model = PPO.load(best_model_path, env, **model_params)
    model.learn(total_timesteps=10_000_000, callback=eval_callback)