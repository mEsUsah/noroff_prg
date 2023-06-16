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

class SuperQueue(Queue):
    def __init__(self):
        super().__init__()

    
    def isempty(self):
        if len(self.queue) > 0:
            return False

        return True


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")