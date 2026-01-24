import numpy as np
import random
import matplotlib.pyplot as plt

# Grid World Kurulumu
grid_size = 5
start_position = (0, 0) # Sol üst köşe
goal_position = (4, 4)  # Sağ alt köşe

# Eylem Alanı: 0-Yukarı, 1-Aşağı, 2-Sol, 3-Sağ
actions = [0, 1, 2, 3]

# Ödül Yapısı
goal_reward = 10
step_reward = -1 

# Q-Tablosunun Başlatılması: 5x5 grid ve her durum için 4 eylem
q_table = np.zeros((grid_size, grid_size, len(actions)))

# Hiperparametreler
learning_rate = 0.1      # Öğrenme oranı (alpha)
discount_factor = 0.9    # İndirim faktörü (gamma)
epsilon = 0.2            # Keşif (exploration) oranı: %20 rastgele, %80 en iyi eylem
episodes = 1000          # Eğitim döngüsü sayısı

# Yardımcı Fonksiyonlar
def get_next_state(state, action):
    """Mevcut durum ve eyleme göre bir sonraki durumu hesaplar."""
    row, col = state
    if action == 0:   # Yukarı
        return max(row - 1, 0), col
    elif action == 1: # Aşağı
        return min(row + 1, grid_size - 1), col
    elif action == 2: # Sol
        return row, max(col - 1, 0)
    elif action == 3: # Sağ
        return row, min(col + 1, grid_size - 1)

def get_reward(state):
    """Duruma göre ödül döndürür."""
    if state == goal_position:
        return goal_reward
    else:
        return step_reward

def choose_action(state):
    """Epsilon-greedy stratejisine göre eylem seçer."""
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions) 
    else:
        return np.argmax(q_table[state[0], state[1]]) 

# Eğitim Döngüsü
for episode in range(episodes):
    state = start_position
    done = False
    
    while not done:
        action = choose_action(state)
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)
        
        next_max = np.max(q_table[next_state[0], next_state[1]])
        
        q_table[state[0], state[1], action] = q_table[state[0], state[1], action] + \
            learning_rate * (reward + discount_factor * next_max - q_table[state[0], state[1], action])
        
        state = next_state
        
        if state == goal_position:
            done = True
            
    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}/{episodes}")

state = start_position
path = [state]
steps = 0

while state != goal_position:
    action = np.argmax(q_table[state[0], state[1]]) 
    state = get_next_state(state, action)
    path.append(state)
    steps += 1

print(f"Hedefe {steps} adımda ulaşıldı!")

grid = np.zeros((grid_size, grid_size))
grid[goal_position] = 2 

for (x, y) in path:
    grid[x, y] = 1 

plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap="coolwarm", interpolation="nearest")
plt.title("Ajanın Hedefe Giden Yolu")
plt.colorbar()

for i, (x, y) in enumerate(path):
    plt.text(y, x, str(i), color="black", ha="center", va="center", fontsize=8)

plt.text(start_position[1], start_position[0], 'Başlangıç', color='white', ha='center', va='center', fontsize=10)
plt.text(goal_position[1], goal_position[0], 'Hedef', color='white', ha='center', va='center', fontsize=10)

plt.show()