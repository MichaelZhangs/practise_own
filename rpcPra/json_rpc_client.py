import jsonrpclib

client = jsonrpclib.ServerProxy("http://localhost:8000")
print(client.pow(2, 3))