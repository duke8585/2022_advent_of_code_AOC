from pprint import pprint as p
import re

aoc_6 = open("./AOC_door_6.txt", "r").read().splitlines()[0]
# aoc_6 = aoc_6[10:]
# aoc_5 = aoc_5[:3]


class Queue(list):
    def __init__(self, length):
        self.length = length

    @property
    def len(self):
        return len(self)

    @property
    def uniqs(self):
        return len(set(self))

    def put(self, enqueued):
        self.append(enqueued)

    def get(self):
        dequeued = self.pop(0)
        return dequeued

    def show(self):
        print(self)

    def cycle(self, enqueued):
        self.put(enqueued)
        if self.len > self.length:
            dequeued = self.get()  # not returned


def q_test():
    q = Queue(4)

    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    q.show()

    q = Queue(4)

    q.cycle(1)
    q.show()
    q.cycle(2)
    q.show()
    q.cycle(3)
    q.show()
    q.cycle(4)
    q.show()
    q.cycle(5)
    q.show()


##
##
##

q = Queue(14)  # part 2

# aoc_6 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

for i, char in enumerate(aoc_6):
    q.cycle(char)
    # p(q.uniqs)
    if q.uniqs == 14:
        print(i + 1)
        break
