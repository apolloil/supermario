import gym

class SkipFrameWrapper(gym.Wrapper):
    def __init__(self, env, skip=4):
        super().__init__(env)
        self.skip = skip

    def step(self, action):
        obs, reward, done, info = None, 0, False, None
        for _ in range(self.skip):
            obs, tem_reward, done, info = self.env.step(action)
            reward += tem_reward
            if done:
                break
        return obs, reward, done, info
