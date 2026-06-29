class PriorityQueue:
    def __init__(self):
        self.heap = []  # list of (priority, item)

    def push(self, item, priority):
        self.heap.append((priority, item))
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        priority, item = self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return item, priority

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            left, right, smallest = 2*i+1, 2*i+2, i
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0
    
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("B", 5)
    pq.push("A", 2)
    pq.push("C", 8)
    print(pq.pop())  # should print ('A', 2) — lowest priority first
    print(pq.pop())  # should print ('B', 5)