class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.queue = list()

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")