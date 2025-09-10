import os
# import gymnasium as gym
import gymnasium as gym   # dùng gymnasium thay cho gym
# import gymnasium_snake_game  as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
# from stable_baselines3.common.env_util import make_atari_env    
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold 



environment_name = "CartPole-v1"   # v0 đã deprecated, dùng v1
env = gym.make(environment_name, render_mode="human")
env = DummyVecEnv([lambda: env])
# main_path = os.path.join("Training", "Logs")
# model_path = os.path.join("Training", "Saved Models")
# model = PPO("MlpPolicy", env, verbose=1,tensorboard_log= main_path)
# model.learn(total_timesteps=20000)
# model.save(model_path)
model_path = r"D:\FINAL_FROJECT_AI\Training\Saved Models.zip"
model = PPO.load(model_path, env=env)
episodes = 5
for episode in range(1, episodes+1):
    observation = env.reset()  
    done = False 
    score = 0    
    while not done:
        env.render()
        action = model.predict(observation, deterministic=True)[0]
        observation, reward, terminated, truncated = env.step(action)
        done = terminated or truncated
        score += reward
    print(f"Episode: {episode}, Score: {score}")
env.close()