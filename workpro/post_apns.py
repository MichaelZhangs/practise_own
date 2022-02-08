import threading
from pyapns2.apns2.client import APNsClient
from pyapns2.apns2.payload import Payload
from pyapns2.apns2.credentials import TokenCredentials
import collections
from ssl import SSLError
from threading import RLock
from h2.exceptions import H2Error
from hyper.http20.exceptions import HTTP20Error, StreamResetError
import time
"""
pyapns使用一段时间后出现问题
"""

class InitApns():
    def __init__(self):
        self.request_limt = 30000
        self.retry_timeout = 2
        self.lock = RLock()
        self.requests = 0
        self.client = None
        self.client_ts = 0
        self._init_client()

    def _init_client(self):
        token_credentials = TokenCredentials(auth_key_path="AuthKey_WW37W62BVM.p8",
                                             auth_key_id=auth_key_id,
                                             team_id=team_id)
        cur_client_ts = self.client_ts
        with self.lock:
            if cur_client_ts != self.client_ts:
                return
            self.requests = 29995
            new_client = APNsClient(credentials=token_credentials, use_sandbox=False)
            print("产生: ", id(self.client))
            try:
                new_client.connect()
                print("新的 ", id(self.client))
            except Exception as e:
                print(e)
            self.client = new_client
            self.client_ts = time.time_ns()


class APNS(InitApns):

    def send_a(self, token):
        print("当前线程 {} self.requests {}\n".format(threading.current_thread(), self.requests))
        if self.requests >= self.request_limt:
            print("进入初始化")
            self._init_client()

        body = "您有新的消息！{}".format(count)
        # body = ""
        data = Payload(alert=body,
                       sound="default", badge=0, title="pyapns22", category="1")
        Notification = collections.namedtuple('Notification', ['token', 'payload'])
        notifications = []
        for i in range(5):
            notifications.append(Notification(payload=data, token=token))
        s = time.time()
        with self.lock:
            push_sent = False
            try:
                try:
                    print("运行 ", id(self.client))
                    self.client.send_notification_batch(notifications=notifications, topic=bundle_id)
                    push_sent = True
                except (ConnectionError, SSLError, H2Error, HTTP20Error) as ex:
                    time.sleep(self.retry_timeout)
                    self._init_client()
                if not push_sent:
                    self.client.send_notification_batch(notifications=notifications, topic=bundle_id)
                    push_sent = True
                if push_sent:
                    self.requests += 1
            except Exception as e:
                print(e)

        print("耗时 {}".format(time.time() - s))


if __name__ == '__main__':
    token = [
        "706075e7fcaee00a8f49ac24d53b8bb0be7d3af0298e5ce9f23c604d2c7b9b39"
    ]

    apns = APNS()
    s = time.time()
    count = 0
    lst = []
    for i in range(12):
        # apns.send_a(token[0])
        thread_1 = threading.Thread(target=apns.send_a, args=(token[0], ))
        thread_1.start()
    # for i in lst:
    #     i.start()
    # time.sleep(1)
    # thread_2.start()
    # apns.handle_stream_id()
    print(time.time() - s)
