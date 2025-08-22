from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT  # 马里奥游戏接口
from gym.wrappers import GrayScaleObservation, ResizeObservation  # 把彩色图像转为灰度图像,并且进行图片压缩，加速训练
from utils.SkipFrameWrapper import SkipFrameWrapper  # 跳帧，加速训练
from stable_baselines3.common.monitor import Monitor  # 进行监控记录


def make_env():
    env = gym_super_mario_bros.make('SuperMarioBros-v2')
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    env = SkipFrameWrapper(env, skip=4)
    env = GrayScaleObservation(env, keep_dim=True)
    env = ResizeObservation(env, shape=(128, 128))
    env = Monitor(env)
    return env


