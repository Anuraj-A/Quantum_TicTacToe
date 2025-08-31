# 🎲 Quantum Tic-Tac-Toe

A fun twist on the classic Tic-Tac-Toe game — powered by **Quantum Mechanics** ⚛️.  
Instead of just placing `X` or `O`, every move is a **quantum superposition** that collapses into `X` or `O` upon measurement.  

This project demonstrates **quantum concepts** like **superposition**, **measurement**, and **random collapse** using a simple and familiar game.

---

## 🚀 Features
- 🎲 **Quantum Moves** – Select two cells; the quantum circuit puts the move in superposition.  
- ⚡ **Quantum Collapse** – When committed, the move collapses into either X or O randomly.  
- 🏆 **Classical Winning Rules** – First to get 3 in a row (X or O) wins.  
- 🤖 **AI Opponent** – Optional simple AI for single-player mode.  
- 🎨 **Interactive UI** – Built with Streamlit for a smooth web interface.  

---

## 🔮 How It Works

### 🎲 Step 1: Quantum Move (Superposition)
When a player selects two cells, the move enters a **superposition**:

\[
|ψ⟩ = \frac{|Cell1⟩ + |Cell2⟩}{\sqrt{2}}
\]

Meaning: the move exists in both cells simultaneously until measured.

---

### ⚡ Step 2: Quantum Collapse (Measurement)
Using **Qiskit + AerSimulator**, the move is measured:  
- With 50% chance it collapses into Cell1  
- With 50% chance it collapses into Cell2  

---

### 🏆 Step 3: Winning
The board fills with collapsed moves.  
Normal Tic-Tac-Toe winning rules apply: **3 in a row** wins.  

---

## 📊 Visual Concept

Player X selects cell (0,4) ───► |ψ⟩ = (|0⟩ + |4⟩)/√2 ───► Measurement ───► Collapses into 0 or 4



Think of it like a **quantum coin toss**:  
- Before collapse → the coin is both heads and tails.  
- After collapse → it becomes one definite value.  

---

## 🖼️ Demo Screenshot
assets/img_1.png
---
assets/img_2.png
---
assets/img_3.png

---

## 🛠️ Installation & Running

### 1️⃣ Clone the repo
```bash
git clone https://github.com/Anuraj-A/Quantum_TicTacToe.git
cd quantum-tic-tac-toe
2️⃣ Create virtual environment (recommended)
bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
pip install -r requirements.txt
4️⃣ Run the game
bash
streamlit run improved_quantum_tic_tac_toe_app.py
📚 Rules of Quantum Tic-Tac-Toe
Each move starts as a quantum superposition between two cells.

The move collapses randomly to one of the two cells.

A player may end up occupying the opponent’s intended cell due to collapse.

Game continues until someone gets 3 in a row, or it’s a draw.

🎓 Learning Outcomes
Understand superposition and measurement in quantum mechanics.

See how randomness emerges naturally in quantum systems.

Experience how classical games can be reimagined with quantum rules.

🌐 Tech Stack
⚛️ Qiskit – Quantum simulation

🐍 Python – Core logic

🎨 Streamlit – Web-based interactive UI

📢 Author
👨‍💻 Developed by Anuraj
🔗 Connect on LinkedIn https://www.linkedlin.com/in/a-anuraj

🧠 Fun Thought
"In classical Tic-Tac-Toe, strategy wins.
In Quantum Tic-Tac-Toe, the universe rolls the dice." 🌌