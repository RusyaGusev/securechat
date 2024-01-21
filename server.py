import websockets
import asyncio

def main():
    PORT = 7890
    print("Server listening on Port " + str(PORT))

    connected = set()

    async def echo(websocket, path):
        print("A client just connected")
        connected.add(websocket)

        try:
            while True:
                message = await websocket.recv()
                if message is None:
                    break  # Exit the loop if the client closes the connection
                print("Received message from client:", message)

                for conn in connected:
                    if conn != websocket:
                        await conn.send("Someone said: " + message)

        except websockets.exceptions.ConnectionClosed as e:
            print("A client just disconnected:", str(e))
        finally:
            connected.remove(websocket)
            print("Remaining connected clients:", len(connected))

            if len(connected) == 0:
                print("No active clients, stopping server.")
                asyncio.get_event_loop().stop()

    start_server = websockets.serve(echo, "", PORT)

    try:
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("stopping")

if __name__ == '__main__':
    main()
#146.235.198.127