
import websockets
import asyncio
def main():
    async def listen():
        url = "ws://101.98.20.149:7890"

        async with websockets.connect(url) as ws:
            await ws.send("Hello Server!")
            while True:
                msg = await ws.recv()
                print(msg)

    asyncio.get_event_loop().run_until_complete(listen())

if __name__ == '__main__':
    main()
