class FreqStack:

    def __init__(self):
        self.freq = {}
        self.elements = {}
        self.max_freq = -1

    def push(self, val: int) -> None:
        if val in self.elements:
            self.elements[val] += 1
        else:
            self.elements[val] = 1
        
        get_freq = self.elements[val]

        if get_freq in self.freq:
            self.freq[get_freq].append(val)
        else:
            self.freq[get_freq] = [val]
        self.max_freq = max(self.max_freq, get_freq)

    def pop(self) -> int:
        value = 0
        if len(self.freq[self.max_freq]) == 1:
            value = self.freq[self.max_freq][0]
            del self.freq[self.max_freq]
            self.max_freq -= 1
        else:
            value = self.freq[self.max_freq].pop()

        # decrease the amount of freq in elements dict
        self.elements[value] -= 1
        if self.elements[value] <= 0:
            del self.elements[value]
        return value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()