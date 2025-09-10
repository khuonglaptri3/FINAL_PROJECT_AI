import gymnasium_snake_game as gym_snake_game
import pygame

# Tạo environment
options = {
    'fps': 10,
    'max_step': 500,
    'init_length': 4,
    'food_reward': 2.0,
    'dist_reward': 1.0,   # 👈 thay vì None
    'living_bonus': 0.0,
    'death_penalty': -1.0,
    'width': 20,
    'height': 20,
    'block_size': 20,
    'background_color': (255, 169, 89),
    'food_color': (255, 90, 90),
    'head_color': (197, 90, 255),
    'body_color': (89, 172, 255),
}
env = gym_snake_game.make('Snake-v1', render_mode='human', **options)

# Reset environment
obs, info = env.reset()

# Mapping phím -> action
# Theo thư viện thì Snake-v1 có 4 action: 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT
action_map = {
    pygame.K_UP: 0,
    pygame.K_RIGHT: 1,
    pygame.K_DOWN: 2,
    pygame.K_LEFT: 3
}

running = True
current_action = 1  # mặc định đi sang phải

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            env.close()
        elif event.type == pygame.KEYDOWN:
            if event.key in action_map:
                current_action = action_map[event.key]

    # Mỗi vòng lặp gửi action
    obs, reward, terminated, truncated, info = env.step(current_action)

    if terminated or truncated:
        print("Game Over! Reward:", reward)
        obs, info = env.reset()

env.close()
