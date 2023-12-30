import websockets
import asyncio

def main():
    PORT = 7890

    print("Server Listening on port " + str(PORT))

    async  def echo(websocket, path):
        print("A client just connected")
        async for message in websocket:
            print("recieved message from client " + message)
            await websocket.send("Pong " + message)

    start_server = websockets.serve(echo, "localhost", PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()
