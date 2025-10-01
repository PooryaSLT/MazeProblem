# 🌀 MazeSolver - Python Maze Solving Class

**MazeSolver** is a Python class that finds an optimal path through a maze while collecting coins along the way.  
The goal is to reach the last row while avoiding obstacles (value 1) and collecting coins (value 2).

---

## :pencil: Introduction
MazeSolver uses a **recursive depth-first search algorithm** to explore possible paths in a 2D maze.  
It keeps track of collected coins and identifies a valid path from the start to the finish.  
This class is designed to be **simple, easy to understand, and extendable** for custom mazes.

---

## ✨ Features
- ✅ Finds a valid path in a maze  
- 💰 Collects coins while navigating  
- 📝 Simple and easy-to-understand Python implementation  
- ⚡ Lightweight and fast  

---

## 🚀 Usage

Create a maze as a 2D list and instantiate the `MazeSolver` class:

```python
from MazeSolver import MazeSolver

maze_input = [
    [0, 1, 1, 1, 1],
    [0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 2, 0]
]

solver = MazeSolver(maze_input)
print("Valid Path:", solver.path)
print("Collected Coins:", solver.coins)
```

**Parameters:**  
- `0` – Empty space (walkable)  
- `1` – Obstacle (cannot pass)  
- `2` – Coin (collectable while navigating)  

**Attributes:**  
- `path` – The valid path found from start to finish  
- `coins` – List of collected coins along the path  

---

## 📬 Contact

<p align="center">
  <b>💡 Feel free to reach out if you have any questions or suggestions!</b>
</p>

<p align="center">
  <a href="https://t.me/LampStack">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/>
  </a>
  <a href="mailto:xialop@outlook.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
</p>

---

⭐ If you like this project, don’t forget to **star** the repo!
