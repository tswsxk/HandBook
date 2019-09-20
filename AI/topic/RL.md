# 强化学习

## 参考资料
1. [深度增强学习（DRL）漫谈 - 从DQN到AlphaGo](https://blog.csdn.net/jinzhuojun/article/details/52752561)

## 环境
### Gym
Gym is a toolkit for developing and comparing reinforcement learning algorithms. It supports teaching agents everything from walking to playing games like Pong or Pinball.[[Official website]](https://gym.openai.com/)

# A New Gym Env
#### Important Interface

using the following code to register a new gym environment
```python
from gym.envs.registration import register

register(
    id='VirtualTB-v0',
    entry_point='virtualTB.envs:VirtualTB',
)
```