import json
import socket

data = {
    "method": "HelloService.Hello",
    "params": ["哈哈哈"],
    "id": 9
}
client = socket.create_connection(("localhost", 5555))
client.sendall(json.dumps(data).encode())

# 获取服务器返回的数据
resp = client.recv(1024)
rsp = json.loads(resp.decode())
print(rsp)


