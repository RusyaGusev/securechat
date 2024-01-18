import websockets
import asyncio


async def main():
    PORT = 7890
    print("Server listening on Port " + str(PORT))

    connected = set()

    async def echo(websocket, path):
        print("A client just connected")
        connected.add(websocket)

        try:
            async for message in websocket:
                print("Received message from client: " + message)
                for conn in connected:
                    if conn != websocket:
                        await conn.send("Someone said:" + message + message)

        except websockets.exceptions.ConnectionClosed as e:
            print("A client just disconnected: " + str(e))
        finally:
            connected.remove(websocket)
            print("Remaining connected clients:", len(connected))

            if len(connected) == 0:
                print("No active clients, stopping server.")
                asyncio.get_event_loop().stop()

    start_server = await websockets.serve(echo, "", PORT)

    try:
        while True:
            await asyncio.sleep(1)  # Add a short sleep to avoid 100% CPU usage
    except KeyboardInterrupt:
        print("Stopping")


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().close()


#146.235.198.127