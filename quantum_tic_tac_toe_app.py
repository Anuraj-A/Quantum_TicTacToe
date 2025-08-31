# improved_quantum_tic_tac_toe_app.py

import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random

# Initialize simulator
simulator = AerSimulator()

# Custom CSS for better UI
st.markdown("""
<style>
div.stButton > button {
    width: 100px;
    height: 100px;
    font-size: 50px;
    border: 2px solid #ddd;
    background-color: #f9f9f9;
}
div.stButton > button:hover {
    background-color: #e0e0e0;
}
</style>
""", unsafe_allow_html=True)

# Streamlit app config
st.set_page_config(page_title="Quantum Tic-Tac-Toe", layout="centered")
st.title("🎲 Quantum Tic-Tac-Toe")
st.caption("Play Tic-Tac-Toe with Quantum Superposition & Measurement")
st.markdown("""
**Instructions**:  
- Players take turns as X or O.  
- Each move is quantum: Select two empty cells (they'll show '?') for 50/50 placement.  
- If only one cell left, select it alone for placement (degenerate quantum case).  
- Cancel selections anytime.  
- Optional: Toggle AI for single-player (random quantum moves for O).
""")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [" "] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "superpos_moves" not in st.session_state:
    st.session_state.superpos_moves = []  # Selected cells for move
if "winner" not in st.session_state:
    st.session_state.winner = None
if "ai_enabled" not in st.session_state:
    st.session_state.ai_enabled = False

# Toggle for AI opponent
st.session_state.ai_enabled = st.checkbox("Enable AI Opponent (for O)", value=st.session_state.ai_enabled)

# Helper: Check winner
def check_winner(board):
    winning_positions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

# Quantum collapse function (50/50 choice between two options)
def quantum_choice(option1, option2):
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Superposition
    qc.measure(0, 0)
    job = simulator.run(qc, shots=1)
    result = job.result().get_counts()
    outcome = max(result, key=result.get)
    return option1 if outcome == "0" else option2

# Make a quantum move
def make_quantum_move(player):
    selections = st.session_state.superpos_moves
    if len(selections) == 2:
        choice = quantum_choice(selections[0], selections[1])
    elif len(selections) == 1:
        choice = quantum_choice(selections[0], selections[0])  # Always selects the same
    else:
        st.error("Invalid selection count.")
        return
    if st.session_state.board[choice] == " ":
        st.session_state.board[choice] = player
        st.session_state.turn = "O" if player == "X" else "X"
        st.session_state.superpos_moves = []
    else:
        st.error("Selected cell is already occupied.")

# Simple AI quantum move: pick two random empty cells, then quantum choose
def ai_move():
    empty_cells = [i for i, cell in enumerate(st.session_state.board) if cell == " "]
    if len(empty_cells) >= 2:
        selections = random.sample(empty_cells, 2)
        choice = quantum_choice(selections[0], selections[1])
        st.session_state.board[choice] = "O"
        st.session_state.turn = "X"
    elif len(empty_cells) == 1:
        st.session_state.board[empty_cells[0]] = "O"
        st.session_state.turn = "X"

# Clear selections
def clear_selections():
    st.session_state.superpos_moves = []

# Draw board with visual feedback and grid lines
def draw_board(required_selections):
    row_cols = st.columns(3)
    for i in range(9):
        label = st.session_state.board[i]
        if label == " ":
            if i in st.session_state.superpos_moves:
                label = "?"
            if row_cols[i % 3].button(label, key=f"cell{i}"):
                if i in st.session_state.superpos_moves:
                    st.session_state.superpos_moves.remove(i)  # Deselect
                elif st.session_state.board[i] == " " and i not in st.session_state.superpos_moves:
                    if len(st.session_state.superpos_moves) < required_selections:
                        st.session_state.superpos_moves.append(i)
                    else:
                        st.warning(f"Max {required_selections} selections allowed.")
        else:
            color = "red" if label == "X" else "blue"
            row_cols[i % 3].markdown(f"<center style='font-size:50px; color:{color};'>{label}</center>", unsafe_allow_html=True)
        if i % 3 == 2 and i < 8:
            st.markdown("---")

# Compute empty cells and required selections
empty_cells = [i for i, cell in enumerate(st.session_state.board) if cell == " "]
empty_count = len(empty_cells)
required_selections = 2 if empty_count >= 2 else 1 if empty_count == 1 else 0

# Display current turn command (dynamic)
if not st.session_state.winner and required_selections > 0:
    if required_selections == 2:
        st.info(f"Player {st.session_state.turn}'s Turn: Select two cells for quantum move.")
    else:
        st.info(f"Player {st.session_state.turn}'s Turn: Select the last cell for placement.")
elif not st.session_state.winner:
    # If no selections possible but not full (unlikely), force check
    st.session_state.winner = "Draw"

# Show board
draw_board(required_selections)

# Move controls
col1, col2 = st.columns(2)
if len(st.session_state.superpos_moves) == required_selections:
    if col1.button("Commit Quantum Move"):
        make_quantum_move(st.session_state.turn)
if st.session_state.superpos_moves:
    if col2.button("Cancel Selection"):
        clear_selections()

# Check winner
st.session_state.winner = check_winner(st.session_state.board)
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a Draw!")
    else:
        st.success(f"🏆 Player {st.session_state.winner} wins!")
        st.balloons()  # Fun animation for win
    if st.button("Play Again"):
        st.session_state.board = [" "] * 9
        st.session_state.turn = "X"
        st.session_state.superpos_moves = []
        st.session_state.winner = None

# AI logic (after human move, if enabled and O's turn)
if st.session_state.ai_enabled and st.session_state.turn == "O" and not st.session_state.winner and empty_count > 0:
    ai_move()