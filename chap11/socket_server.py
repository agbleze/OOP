#%%
import contextlib
import socket

def main_1() -> None:
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM
                           )
    server.bind(("localhost", 2401))
    server.listen(1)
    with contextlib.closing(server):
        while True:
            client, addr = server.accept()
            dice_response(client)
            client.close()
            
            
def dice_response(client: socket.socket) -> None:
    request = client.recv(1024)
    try:
        response = dice.dice_roller(request)
    except (ValueError, KeyError) as ex:
        response = repr(ex).encode('utf-8')
    client.send(response)
    
    
import random

def dice_roller(request: bytes) -> bytes:
    request_text = request.decode('utf-8')
    numbers = [random.randint(1, 6) for _ in range(6)]
    response = f"{request_text} = {numbers}"
    return response.encode("utf-8")




    