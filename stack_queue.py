# def create_stack():
#     stack = []
#     return stack

# def push(stack, item):
#     stack.append(item)
#     print("pushed item: " + item)

# def pop(stack):
#     if (len(stack)) < 1:
#         return "stack is empty"
#     return stack.pop()
# print("Name: Navdeep    Student_id: 21582009")
# stack = create_stack()
# push(stack, str(2))
# push(stack, str(1))
# push(stack, str(5))
# push(stack, str(8))
# push(stack, str(2))
# push(stack, str(0))
# push(stack, str(0))
# push(stack, str(9))
# print(stack)
# pop(stack)
# pop(stack)
# pop(stack)
# pop(stack)
# pop(stack)
# pop(stack)
# pop(stack)
# pop(stack)
# print(stack)

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)
### print("Name: Navdeep    Student_id: 21582009")
q = Queue()
q.enqueue(2)
q.enqueue(1)
q.enqueue(5)
q.enqueue(8)
q.enqueue(2)
q.enqueue(0)
q.enqueue(0)
q.enqueue(9)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()