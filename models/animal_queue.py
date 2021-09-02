import time

from models.animal import Animal
from models.cat import Cat
from models.dog import Dog
from models.queue import Queue
from models.stack import Stack

DOG = 1
CAT = 2


class AnimalQueue():
    def __init__(self):
        self._cats_queue = Queue()
        self._cats_queue2 = Queue()
        self._dogs_queue = Queue()
        self._dogs_queue2 = Queue()
        self._any_queue = Queue()
        self._any_load_stack = Stack()

    def enqueue(self, animal: Animal):
        if animal is Dog:
            self._dogs_queue.enqueue(animal)
            self._any_queue.enqueue(DOG)
        else:
            self._cats_queue.enqueue(animal)
            self._any_queue.enqueue(CAT)

    def enqueue2(self, animal: Animal):
        if animal is Dog:
            self._dogs_queue2.enqueue((time.time(), animal))
        else:
            self._cats_queue2.enqueue((time.time(), animal))

    def dequeue_any(self) -> Animal:
        kind = self._any_queue.dequeue()
        if kind is DOG:
            return self._dogs_queue.dequeue()
        else:
            return self._cats_queue.dequeue()

    def dequeue_any2(self):
        if self._dogs_queue2.is_empty():
            return self._cats_queue2.dequeue()[1]
        elif self._cats_queue2.is_empty():
            return self._dogs_queue2.dequeue()[1]
        else:
            dog_time = self._dogs_queue2.peek()[0]
            cat_time = self._cats_queue2.peek()[0]
            return self._dogs_queue2.dequeue()[1] if dog_time > cat_time else self._cats_queue2.dequeue()[1]

    def dequeue_cat(self) -> Cat:
        return self._dequeue_animal(self._cats_queue, CAT)

    def dequeue_dog(self) -> Dog:
        return self._dequeue_animal(self._dogs_queue, DOG)

    def _dequeue_animal(self, animal_queue: Queue, kind: int):
        animal = animal_queue.dequeue()
        self._load_any_stack_until_kind(kind)
        self._any_queue.dequeue()
        self._unload_any_stack()
        return animal

    def _load_any_stack_until_kind(self, kind: int):
        while self._any_queue.peek() != kind:
            self._any_load_stack.push(self._any_queue.dequeue())

    def _unload_any_stack(self):
        while not self._any_load_stack.is_empty():
            self._any_queue.enqueue(self._any_load_stack.pop())
