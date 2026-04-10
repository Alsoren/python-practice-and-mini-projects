# İter and Next Methods
class Counter:
    def __init__(self, max_value):
        self.current = 0
        self.max_value = max_value

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next value in the sequence."""
        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # Stop iteration when end is reached
        
my_counter = Counter(20)
for number in my_counter:
    print(number)

