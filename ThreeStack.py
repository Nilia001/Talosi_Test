class ThreeStack:
    def init(self):
        self.stacks = [[] for _ in range(3)]

    def push(self, stack_num, obj):
        if stack_num < 1 or stack_num > 3:
            raise Exception("Invalid stack number")
        self.stacks[stack_num-1].append(obj)

    def pop(self, stack_num):
        if stack_num < 1 or stack_num > 3:
            raise Exception("Invalid stack number")
        if not self.stacks[stack_num-1]:
            raise Exception("Stack is empty")
        return self.stacks[stack_num-1].pop()
