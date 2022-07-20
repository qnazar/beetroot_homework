from task1 import MaxBinHeap


class PriorityQueue:
    def __init__(self):
        self.queue = MaxBinHeap()

    def enqueue(self, item):
        self.queue.insert(item)

    def dequeue(self):
        return self.queue.del_max()

    def __repr__(self):
        return f'<-- {self.queue.heap_list[1:]} <--'


if __name__ == '__main__':
    pq = PriorityQueue()
    print(pq)
    pq.enqueue(20)
    pq.enqueue(10)
    pq.enqueue(31)
    print(pq)
    print(pq.dequeue())
    print(pq)
