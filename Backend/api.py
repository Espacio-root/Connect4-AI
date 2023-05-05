from fastapi import FastAPI
import math
from typing import List
from connect4 import Connect4Ai

app = FastAPI()

@app.post("/move")
def move(board: List[List[int]], player_piece: int, ai_piece: int) -> List[List[int]]:
    ai = Connect4Ai(6, 7, player_piece, ai_piece)
    return ai.minimax(board, 5, -math.inf, math.inf, True)