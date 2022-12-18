class BinarySearch:
    def binary_search(self, list_container, first, last, target):
        if last < first:
            return f'{target} not found.'
        
        mid_index = ( first + last )  // 2
        if list_container[mid_index] == target:
            return f'{target} found at position {mid_index}.'
        if list_container[mid_index] > target:
            return self.binary_search(list_container, first, mid_index - 1, target)
        return self.binary_search(list_container, mid_index + 1, last, target)


if __name__ == '__main__':
    list_container = [1, 2, 3, 4, 55, 66, 78, 445]
    targets = [67, 66, 55, 445, 1, 2, 3, 4, 76, 0]
    first = 0
    last = len(list_container) - 1

    bs = BinarySearch()

    for target in targets:
        print(bs.binary_search(list_container, first, last, target))
