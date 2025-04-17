# 🎮 Ultimate Tic Tac Toe Showdown 🧠

Welcome to the most **ruthless** game of Tic Tac Toe you've ever played.

This isn't your grandma's Tic Tac Toe. This is a battle-hardened, brain-flexing AI challenge designed to humiliate any human who dares to face it. Built with Python, this game doesn't just play — it **thinks**.

---

## 💡 Why This Project Is Different

Most Tic Tac Toe projects are either:
- ✅ too basic (hard-coded AI with no brains),
- ❌ beatable (predictable, dumb logic),
- 💤 or just boring (no modes, no fun).

**But not this one.**

This one comes loaded with:
- 🔁 Multiple game modes (Human vs Human, Human vs AI, Human vs RandomBot)
- 🧠 A super-smart AI powered by the Minimax algorithm
- 🎲 A random bot for chaos-lovers
- 🎯 Clean command-line visuals
- 🔄 AI self-play mode for testing performance
- 💥 Game results with stats

---

## 🧠 How the Minimax Algorithm works

This AI doesn't play — it *calculates*. The `SmartComputerPlayer` uses the **Minimax algorithm**, making it unbeatable.

### 🌀 What Minimax Does:
1. **Recursively simulate** all valid moves.
2. Assign a score to each final game state.
3. **Backtrack and choose** the move that leads to the best score.

### ⚙️ Tiny Optimization:
- If it's the first move of the game (all squares empty), AI skips thinking and picks randomly — because all options are equal.

---

### 🌀 Visualizing the AI’s Thought Process

Here’s how the Smart AI thinks after **6 moves (i.e., 3 by each player)**:
![Flowchart](https://github.com/user-attachments/assets/c98054b4-e409-4392-be3c-ae51ee3817e6)



- Each branch represents a possible move the AI could make.
- The leaves of the tree (bottom nodes) show the **outcome scores**:
  - `+1` if AI wins
  - `-1` if AI loses
  - `0` if it’s a draw
- The AI **backtracks from the bottom**, selecting the move that **guarantees the best possible outcome**, even against a perfect opponent.
---

## 🏆 Efficiency: AI Performance Results

We put the Smart AI to the test.  
And let's just say... it's built different.

### 🤖 SmartAI vs SmartAI (1000 games)
```
X wins: 0
O wins: 0
Ties: 1000
```
The AI plays so perfectly, neither side can win. Pure strategy equilibrium. You can’t beat it — you can only **tie**.

---

### 🤖 SmartAI vs RandomBot (1000 games)
```
X (SmartAI) wins: 960
O (RandomBot) wins: 0
Ties: 40
```
🎯 The SmartAI *destroys* the random bot, 96% win rate. That’s efficiency you can trust.

---

## 👾 How to Play

### 1. Clone the repo  
   ```bash
   https://github.com/lokesha01hp/Undefeated-tic-tac-toe_minimax_algo.git
   cd tic-tac-toe-ai
```

### 2. Run the game
 ```bash
 python game.py
```
