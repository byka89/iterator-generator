list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIterator:

    def __init__(self, new_list):
        self.new_list = [object for item in list_of_lists_1 for object in item]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]

if __name__ == '__main__':

    for element in FlatIterator(list_of_lists_1):
        print(element)

    flat_list = [item for item in FlatIterator(list_of_lists_1)]
    print(flat_list)


def flat_generator(new_list):
    for item in new_list:
        for elem in item:
            yield elem


for item_1 in flat_generator(list_of_lists_1):
        print(item_1)