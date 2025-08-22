from make_env import make_env
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv,VecFrameStack
import time

if __name__ == "__main__":
    env = SubprocVecEnv([make_env for _ in range(1)])
    env = VecFrameStack(env, 4)

    model = PPO.load(".//best_model//best_model.zip", env=env)

    done = False
    obs = env.reset()
    while not done:
        obs = obs.copy()
        action, _ = model.predict(obs, deterministic=False)
        obs, reward, done, info = env.step(action)
        env.render()
        time.sleep(0.02)

