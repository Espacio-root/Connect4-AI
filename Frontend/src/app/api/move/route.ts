
export async function POST(req: any, res: Response) {
    const url = 'https://3v3fm5ejnwmqed7e6ilov26pou0awubn.lambda-url.eu-north-1.on.aws/move';
    const data = await req.json();
    const board = await JSON.stringify(data.board)

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: board,
    });

    const text = await response.text();

    return new Response(text);
}
