from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def add(a, b):
    return a + b


server = SimpleJSONRPCServer(("localhost", 8000))
server.register_function(pow)
server.register_function(add)
server.register_function(lambda x, y: x*y, "mul")
server.serve_forever()
