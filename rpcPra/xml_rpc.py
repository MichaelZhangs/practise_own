from xmlrpc.server import SimpleXMLRPCServer

class Calculater:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return abs(x - y)
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y

c = Calculater()
server = SimpleXMLRPCServer(("localhost", 8088))
server.register_instance(c)
print("开始监听8088 端口")
server.serve_forever()