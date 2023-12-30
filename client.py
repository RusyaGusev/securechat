
import websockets
import asyncio
def main():
    async def listen():
        url = "ws://146.235.198.127:7980"

        async with websockets.connect(url) as ws:
            await ws.send("Hello Server!")
            while True:
                msg = await ws.recv()
                print(msg)

    asyncio.get_event_loop().run_until_complete(listen())

if __name__ == '__main__':
    main()
