class Reverse:
    # =========================================================================
    # Iterator for looping over a sequence backwards.
    # =========================================================================

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


for line in open('dataset_usa_cobb-douglas.zip'):
    print(line, end='')


rev = Reverse('alexander')
iter(rev)
for char in rev:
    print(char)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('ahmadtea'):
    print(char)
