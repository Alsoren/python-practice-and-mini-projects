# Magic Methods (Dunder Methods)

class MyList:
    def __init__(self, items, name):
        self.items = items
        self.name = name
    def __len__(self):
        return len(self.items)
class Greet:
    def __call__(self, name):
        return f"Hello, {name}!"

newList = MyList([1, 2, 3, 4], "Alice")
greet = Greet()
print(len(newList))  # Calls __len__ method, output: 4
print(greet("Alice"))  # Calls __call__ method, output: Hello, Alice!