class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack is overflow")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"New item is added in the stack: {item}")

    def pop(self):
        if self.top == -1:
            print("Stack is underflow")
        else:
            removed = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"Item that was removed is: {removed}")

    def peek(self):
        if self.top == -1:
            print("Stack is underflow")
        else:
            print(f"Top item of stack is: {self.stack[self.top]}")

    def display(self):
        if self.top == -1:
            print("Stack is underflow")
        else:
            print("Current stack:")
            for i in range(self.top, -1, -1):
                print(f"{self.stack[i]}")


def menu():
    size = int(input("Enter the size of the stack: "))
    s = Stack(size)
    
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        opt = input("Select one (1-5): ")

        if opt == '1':
            value = int(input("Enter the value to push: "))
            s.push(value)
        elif opt == '2':
            s.pop()
        elif opt == '3': 
            s.peek()
        elif opt == '4':
            s.display()
        elif opt == '5':
            print("Exiting.............")
            break
        else:
            print("Please provide an option between 1-5.")

menu()
