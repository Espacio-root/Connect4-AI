"use client";
import { useEffect, useState } from "react";
import Image from "next/image";
import axios from "axios";

export default function Connect({
  searchParams,
}: {
  searchParams: { opponent: string };
}) {
  const [board, setBoard] = useState(
    [...Array(6)].map((e) => Array(7).fill(0))
  );
  const [player, setPlayer] = useState(1);
  const [winner, setWinner] = useState(null);
  const [timer, setTimer] = useState(30);
  const [pause, setPause] = useState(false);
  const [hasMounted, setHasMounted] = useState(false);

  const computer = searchParams.opponent === "computer";

  const handleClick = ({ col }: { col: number }) => {
    if (winner) return;
    if (computer && player === 2) return;
    let newBoard = [...board];

    for (let i = 5; i >= 0; i--) {
      if (newBoard[i][col] === 0) {
        newBoard[i][col] = player;
        setBoard(newBoard);
        return;
      }
    }
  };

  const makeMove = async (board: number[][]) => {
    if (winner) return;
    if (computer && player === 1) return;
    if (!computer) return;

    const url = 'api/move';

    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify({ board: board }),
    });

    const text = await response.text();

    setBoard(JSON.parse(text));
    return;
  };

  const handleRestart = () => {
    setTimer(30);
    setPlayer(1);
    setWinner(null);
    setBoard([...Array(6)].map((e) => Array(7).fill(0)));
  };

  useEffect(() => {
    if (hasMounted) {
      checkWinner();
      setPlayer(player === 1 ? 2 : 1);
      setTimer(30);
    } else {
      setHasMounted(true);
    }
  }, [board]);

  useEffect(() => {
    if (computer && player === 2) {
      makeMove(board);
    }
  }, [player, computer]);

  useEffect(() => {
    if (!pause && !winner) {
      const interval = setTimeout(() => {
        setTimer((time) => time - 1);
      }, 1000);

      return () => clearTimeout(interval);
    }
  }, [timer, pause]);

  const checkWinner = () => {
    // Check horizontal
    for (let i = 0; i < 6; i++) {
      for (let j = 0; j < 4; j++) {
        if (
          board[i][j] !== 0 &&
          board[i][j] === board[i][j + 1] &&
          board[i][j + 1] === board[i][j + 2] &&
          board[i][j + 2] === board[i][j + 3]
        ) {
          setWinner(board[i][j]);
          return;
        }
      }
    }

    // Check vertical
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 6; j++) {
        if (
          board[i][j] !== 0 &&
          board[i][j] === board[i + 1][j] &&
          board[i + 1][j] === board[i + 2][j] &&
          board[i + 2][j] === board[i + 3][j]
        ) {
          setWinner(board[i][j]);
          return;
        }
      }
    }

    // Check Anti-diagonal
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 4; j++) {
        if (
          board[i][j] !== 0 &&
          board[i][j] === board[i + 1][j + 1] &&
          board[i + 1][j + 1] === board[i + 2][j + 2] &&
          board[i + 2][j + 2] === board[i + 3][j + 3]
        ) {
          setWinner(board[i][j]);
          return;
        }
      }
    }

    // Check diagonal
    for (let i = 3; i < 6; i++) {
      for (let j = 0; j < 4; j++) {
        if (
          board[i][j] !== 0 &&
          board[i][j] === board[i - 1][j + 1] &&
          board[i - 1][j + 1] === board[i - 2][j + 2] &&
          board[i - 2][j + 2] === board[i - 3][j + 3]
        ) {
          setWinner(board[i][j]);
          return;
        }
      }
    }
  };

  if (timer === 0) {
    setPlayer(player === 1 ? 2 : 1);
    setTimer(30);
  }

  return (
    <div className="h-full w-full flex flex-col overflow-x-hidden">
      <div className="relative">
        <div className="mx-auto mt-12 h-auto max-w-[800px] w-[85%] grid place-items-center gap-12">
          <nav className="grid grid-cols-3 w-full mt-12 place-items-center">
            <button
              className="uppercase inline-flex items-center font-poppins text-5xl px-6 py-3 font-bold tracking-wider  bg-black text-slate-200 bg-opacity-60 hover:bg-slate-200 hover:text-black hover:border-4 hover:border-black rounded-full transition-colors duration-200 ease-in"
              onClick={() => setPause(!pause)}
            >
              {pause ? "Resume" : "Pause"}
            </button>
            <Image src="/images/Logo.png" width="100" height="100" alt="Logo" />
            <button
              className="uppercase inline-flex items-center font-poppins text-5xl px-6 py-3 font-bold tracking-wider  bg-black text-slate-200 bg-opacity-60 hover:bg-slate-200 hover:text-black hover:border-4 hover:border-black rounded-full transition-colors duration-200 ease-in"
              onClick={handleRestart}
            >
              Restart
            </button>
          </nav>
          <div className="bg-black rounded-3xl w-full h-auto p-3">
            <div className="bg-slate-200 w-full rounded-3xl grid grid-cols-7 grid-row-6 place-self-start pb-12 pt-4 mb-6">
              {board.map((row, rowIndex) =>
                row.map((col, colIndex) => (
                  <div
                    key={`${rowIndex}-${colIndex}`}
                    className={`${col === 0 ? "bg-black" : "bg-black bg-opacity-70"} rounded-full w-auto m-[5px] aspect-square relative overflow-clip border-8 border-black`}
                    onClick={() => handleClick({ col: colIndex })}
                  >
                    <div className={`${col === 0 ? "bg-[#7A45FF]" : col === 1 ? "bg-[#FC6587]" : "bg-[#FECE65]"} ${col === 0 ? "lg:top-6 md:top-4 top-3" : "top-2"} rounded-full absolute w-full h-full`}></div>
                  </div>
                ))
              )}
            </div>
            <div className={`absolute w-full bottom-0 left-0 h-[300px] ${winner === null ? "bg-[#5C2CD5]" : winner === 1 ? "bg-[#FC6587]" : "bg-[#FECE65]"} rounded-t-[50px] -z-10`}>
            </div>
          </div>

          <div className={`pentagon font-poppins text-white font-bold ${player === 1 ? "bg-[#FE6686]" : "bg-[#FECE65]"} grid place-items-center pt-16 pb-5 px-3 -mt-28 relative h-auto w-auto border-4 border-b-[14px] border-t-0 rounded-[20px] border-black`}>
            <p className="uppercase tracking-tight text-2xl pb-2">
              Player {player}'s Turn
            </p>
            <p className="text-7xl">{timer}s</p>
          </div>
        </div>
      </div>
    </div>
  );
}
