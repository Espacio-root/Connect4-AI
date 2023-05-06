from fastapi import FastAPI, Response
from fastapi import FastAPI
from typing import List
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from connect4 import Connect4Ai
from mangum import Mangum
import math
import json

app = FastAPI()
handler = Mangum(app)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/move")
async def move(board: List[List[int]]) -> JSONResponse:
    board = np.array(board)
    ai = Connect4Ai(6, 7, 1, 2)
    col, _ = ai.minimax(board, 3, -math.inf, math.inf, 2)
    
    try:
        result = ai.drop_piece(board, ai.get_next_open_row(board, col), col, 2).tolist()
        return JSONResponse(content=result, headers={"Access-Control-Allow-Origin": "*", 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500, headers={"Access-Control-Allow-Origin": "*"})