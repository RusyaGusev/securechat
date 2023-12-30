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
            async for message in websocket:
                print("Received message from client: " + {message})
                for conn in connected:
                    if conn != websocket:
                        await conn.send("Someone said: {message}" + {message})

        except websockets.exceptions.ConnectionClosed as e:
            print("A client just disconnected: "  + {e})
        finally:
            connected.remove(websocket)
            print("Remaining connected clients:", len(connected))

    start_server = websockets.serve(echo, "", PORT)

    try:
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("stopping")

if __name__ == '__main__':
    main()