class ArrayQueue:
    
    DEFAULT_CAPACITY = 10
    
    def __init__ (self):
        
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY 
        self._size = 0
        self._front = 0
        self._back = 0
        
    def len (self):        
        
        return self._size

    def is_empty(self):
        
        return self._size == 0

    def first(self):
        
        if self.is_empty():
            raise Empty( "Queue is empty" ) 
            return self._data[self._front]

    def dequeue(self):
        
        if self.is_empty():
            raise Empty( "Queue is empty" )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) 
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def dequeue1(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None         
        self._front = self._front
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer
        
    def enqueue(self, e):
        
        if self._size == len(self._data):
            self._resize(2  * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def enqueue1(self, e):
        
        if self._size == len(self._data):
            self._resize(2 * len(self._data))     
        self._front = (self._front - 1) % len(self._data)
        avail = (self._front + self._size) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data) 
        
    def   _resize(self, cap): 
        
        old = self._data
        self._data = [None] * cap 
        walk = self._front
        for k in range(self. size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old) 
        self._front = 0
        self._back = (self._front + self._size - 1) % len(self._data)

queue = ArrayQueue()
queue.enqueue1(1)
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue._data
queue.enqueue1(2)
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue._data
queue.dequeue1()
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueue1(3)
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueue1(4)
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.dequeue1()
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueue1(5)
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.dequeue()
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueue(6)
print(f"First Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
