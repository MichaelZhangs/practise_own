from xmlrpc import client

server = client.ServerProxy("http://localhost:8088")
print(server.add(1,2))