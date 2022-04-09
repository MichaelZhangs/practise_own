import zerorpc

class myRPC(object):
    def listinfo(self,message):
        return "get info : %s"%message

s = zerorpc.Server(myRPC())

s.bind("tcp://127.0.0.1:4242")
s.run()