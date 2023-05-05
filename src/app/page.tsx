import { FC } from "react";
import Image from "next/image";
import Link from "next/link";

interface pageProps {}

const page: FC<pageProps> = ({}) => {
  return (
    <div className="flex flex-col items-center justify-between font-poppins h-screen w-screen text-white py-10">
      
      <Image src="/images/Logo.png" height="300" width="300" alt="Logo" />

      <div className="flex flex-col justify-center items-center -mt-20">

        <h1 className="text-7xl font-extrabold mb-20">Welcome to Connect 4!</h1>
        <h2 className="text-3xl font-bold mb-4">Please select a game mode:</h2>

        <div className="flex flex-row gap-8 justify-center items-center">
          <Link
            href="/game?opponent=computer"
            className="uppercase inline-flex items-center font-poppins text-5xl px-6 py-3 font-bold tracking-wider  bg-black text-slate-200 bg-opacity-60 hover:bg-slate-200 hover:text-black hover:border-4 hover:border-black rounded-full transition-colors duration-200 ease-in"
          >
            <h3 className="text-2xl font-bold uppercase">Player VS Computer</h3>
          </Link>
          <Link
            href="/game?opponent=player"
            className="uppercase inline-flex items-center font-poppins text-5xl px-6 py-3 font-bold tracking-wider  bg-black text-slate-200 bg-opacity-60 hover:bg-slate-200 hover:text-black hover:border-4 hover:border-black rounded-full transition-colors duration-200 ease-in"
          >
            <h3 className="text-2xl font-bold uppercase">Player VS Player</h3>
          </Link>
        </div>
      </div>

      <footer>
        <p className="text-2xl text-white">
          Made with &hearts; by{" "}
          <a href="https://github.com/Espacio-root">Espacio</a>
        </p>
      </footer>
      
    </div>
  );
};

export default page;
