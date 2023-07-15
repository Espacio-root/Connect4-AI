#Full Stack Connect4 Game
##Welcome to the Connect4 game AI backend repository! This project is part of a full-stack implementation of the classic Connect4 game, where you can challenge an intelligent AI opponent.

##Table of Contents
*Introduction
*Features
*Algorithm Overview
*Project Structure
*Getting Started
*Contributing
*License
*Introduction

This repository contains the backend implementation of the Connect4 game's AI. Connect4 is a two-player board game where players take turns dropping colored discs from the top into a vertically suspended grid. The objective is to connect four of one's own discs in a row, either horizontally, vertically, or diagonally, before the opponent does.

The AI backend powers the intelligent opponent that users can challenge when playing the Connect4 game. The AI utilizes the [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax) to make strategic decisions and choose the best possible move.

##Features
Intelligent AI Opponent: The AI backend uses the Minimax algorithm to provide a challenging and strategic Connect4 opponent.
Scoring System: The backend employs a scoring system to evaluate potential moves and make informed decisions.
Efficient Pruning: The Minimax algorithm is optimized using alpha-beta pruning, reducing the search space and improving performance.

##Algorithm Overview
The backend AI uses the [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax), a decision-making technique widely used in two-player turn-based games. It operates on a game tree, evaluating the outcomes of possible moves to find the optimal move for the AI player. The algorithm recursively explores the game tree up to a specified depth and assigns a score to each terminal node (end of the game). The AI then makes decisions based on these scores, aiming to maximize its chances of winning while minimizing the opponent's.

To improve performance, the Minimax algorithm employs alpha-beta pruning, which prunes branches in the game tree that are unlikely to lead to a better move for the AI. This optimization significantly reduces the search space, making the AI more efficient without compromising its strategic decision-making abilities.

##Project Structure
The Connect4 AI backend project is organized as follows:

backend/
    ├── connect4_ai.py    # Connect4 AI class implementing the Minimax algorithm
    ├── api.py           # API
frontend/
    ...                   # Frontend code and assets (separate repository)
Getting Started
To run the Connect4 game with the AI backend, follow these steps:

Clone this repository: git clone https://github.com/Espacio-Root/Connect4-AI.git
Navigate to the backend directory: cd backend
Please note that the frontend of the Connect4 game is hosted separately in the frontend repository. Make sure to integrate this backend with the frontend for a complete and interactive user experience.