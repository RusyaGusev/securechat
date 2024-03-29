
import asyncio
import websockets

async def send_and_receive_messages():
    url = "ws://146.235.198.127:7890"

    try:
        async with websockets.connect(url, timeout=10) as ws:
            print("You have been connected")
            while True:
                message = input("Enter a message to send (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    break
                await ws.send(message)

                response = await ws.recv()
                print(f"Received from server: {response}")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection to the server closed: {e}")

def main():
    asyncio.get_event_loop().run_until_complete(send_and_receive_messages())

if __name__ == "__main__":
    main()



# as 146.235.198.127
# as 101.98.20.149
