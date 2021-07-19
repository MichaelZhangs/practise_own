import requests
import socket
class Simulator():
    def get_host_ip(self):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.connect(("8.8.8.8",80))
            ip = s.getsockname()[0]
        finally:
            s.close()

        return ip

    def send_post(self, text):
        data = {
            "txt":text
        }

        flask_url = self.get_host_ip()+":8888"
        url = f"http://"+flask_url+"/tts"
        print("[AI speak] :")
        requests.post(url,json=data)


    def people_say(self):
        while True:
            print("[pls say something] : ")
            s = input()
            return s

    def send(self):
        end_words = ["再见","拜拜","goodbye","bye"]
        while True:
            s = self.people_say()
            self.send_post(s)
            if s in end_words:
                break

if __name__ == '__main__':
    simulator = Simulator()
    simulator.send()