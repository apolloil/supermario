# 🎮 Super Mario Reinforcement Learning with PPO
基于 ​​Stable-Baselines3 PPO 算法​​的超级马里奥智能体训练框架，实现自动化通关经典任天堂游戏环境。

## 🚀 项目概述
本项目利用近端策略优化（PPO）算法，在 gym-super-mario-bros环境中训练智能体学习通关策略。核心特性包括：

•
​​PPO 算法优化​​：基于stable-baseline3，结合值函数裁剪（Clip）、广义优势估计（GAE）和 KL 散度约束，确保训练稳定性。

•
​​奖励工程​​：基于gym-super-mario-bros，奖励函数（前进奖励、金币收集、敌人击杀、通关奖励）加速收敛。

•
​​训练可视化​​：基于tensorborad，实时监控奖励曲线、游戏画面和策略动作分布。

•
​​加速训练技巧：
1. 使用SuperMarioBros-v2环境，对原环境细节纹理模糊处理，有利于CNNpolicy识别训练。
2. 使用跳帧处理，将多帧并做一帧，缓解奖励稀疏问题，加快收敛速度
3. 对图片进行灰度处理和resize变换，简化图形
4. 帧叠加处理，将连续帧作为向量传递，有利于捕捉动作信息

## 📈训练过程
训练曲线：

<img width="307" height="242" alt="image" src="https://github.com/user-attachments/assets/0334aaf0-17ba-458d-9498-9f24d6729c81" />

测试曲线：

<img width="312" height="262" alt="image" src="https://github.com/user-attachments/assets/ad6ad024-d45f-4da3-ad55-9165c4f1d428" />

## 🎥 结果展示


https://github.com/user-attachments/assets/df23f2c2-adf1-403e-8ee2-fc98deca5e44

## 📂 项目结构
mario/

├── best_model/

│ ├── best_model.zip //存储最优模型

├── evaluate_model.py  //跑一遍最优模型看效果

├── make_env.py   //创建env环境

├── train_model.py   //训练模型代码

├── test/   //用于测试核心包是否能跑

│ ├── A2C_cartpole(sb3).py   //测试sb3框架算法

│ └── random_mario.py    //测试gym-super-mario-bros环境

├── utils/  //工具库（其实目前就1个）

│ ├── SkipFrameWrapper.py //跳帧类

│ └── init.py

├── .gitignore

├── README.md

└── requirements.txt

## 🔧安装提示
运行pip install requirements

