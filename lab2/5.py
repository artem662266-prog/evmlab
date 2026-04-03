class MyCircularQueue:
    def __init__(self, k):
        # создаём массив фиксированного размера k для хранения элементов
        self.queue = [0] * k
        self.k = k  # размер очереди
        self.front = 0  # индекс первого элемента
        self.rear = 0   # индекс следующей позиции для вставки
        self.count = 0  # количество элементов в очереди

    def enQueue(self, value):
        # если очередь полна, вставить нельзя
        if self.count == self.k:
            return False
        # записываем значение в текущую позицию rear
        self.queue[self.rear] = value
        # двигаем rear по кругу (если дошли до конца, возвращаемся в начало)
        self.rear = (self.rear + 1) % self.k
        # увеличиваем количество элементов
        self.count += 1
        return True

    def deQueue(self):
        # если очередь пуста, удалить нельзя
        if self.count == 0:
            return False
        # двигаем front по кругу, фактически удаляя элемент
        self.front = (self.front + 1) % self.k
        # уменьшаем количество элементов
        self.count -= 1
        return True

    def Front(self):
        # если очередь пуста, вернуть -1
        if self.count == 0:
            return -1
        # возвращаем первый элемент
        return self.queue[self.front]

    def Rear(self):
        # если очередь пуста, вернуть -1
        if self.count == 0:
            return -1
        # возвращаем последний элемент (rear указывает на следующую пустую позицию, поэтому -1)
        return self.queue[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self):
        # очередь пуста, если count == 0
        return self.count == 0

    def isFull(self):
        # очередь полна, если count == размер очереди
        return self.count == self.k
