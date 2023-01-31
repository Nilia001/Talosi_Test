class ThreeStack:
    def init(self):
        self.stacks = [[] for _ in range(3)]

    def push(self, num, obj):
        if num < 1 or num > 3:
            raise Exception("Invalid stack number")
        self.stacks[stack-1].append(obj)

    def pop(self, stack):
        if stack < 1 or stack > 3:
            raise Exception("Invalid stack number")
        if not self.stacks[stack-1]:
            raise Exception("Stack is empty")
        return self.stacks[stack-1].pop()
