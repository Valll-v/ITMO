from typing import Optional

PAGES = [9, 24, 19, 3, 21, 1, 11, 15, 11, 4, 5, 7, 20, 4,
         20, 5, 19, 10, 3, 17, 9, 16, 24, 7, 2, 13, 23, 4,
         3, 15, 24, 22, 19, 3, 4, 13, 18, 5, 7, 11, 23, 22, 6]

MEMORY_SIZE = 19


class PageWorker:
    def __init__(self, size):
        self.size = size
        self.values_set = set()
        self.queue = []

    def _print_queue(self) -> None:
        print(f'Queue: {self.queue}')

    def _pop(self, index: int) -> Optional[int]:
        value = self.queue[index]
        self.queue.pop(index)
        self.values_set.remove(value)
        return value

    def _append(self, value: int) -> None:
        self.queue.append(value)
        self.values_set.add(value)

    def _put(self, value: int) -> Optional[int]:
        raise NotImplemented

    def run(self) -> None:
        raise NotImplemented


class OptimalPageWorker(PageWorker):

    def get_last_index_usage(self, pointer: int) -> int:
        max_index = -1
        max_index_in_queue = 0
        for i, page in enumerate(self.queue):
            try:
                page_index = PAGES.index(page, pointer)
            except ValueError:
                page_index = 100
            if page_index > max_index:
                max_index = page_index
                max_index_in_queue = i
        return max_index_in_queue

    def _put(self, value: int, pointer=0) -> Optional[int]:
        popped = None
        if value in self.values_set:
            return
        if len(self.queue) == self.size:
            index = self.get_last_index_usage(pointer)
            popped = self._pop(index)
        self._append(value)
        return popped

    def run(self) -> None:
        page_swipes = 0
        print(f'Execution Optimal')
        print(f'Count of frames: {self.size}')
        print()
        for i, page in enumerate(PAGES):
            print(f'Using page: {page}')
            popped = self._put(page, i)
            if popped is not None:
                print(f'Removed page: {popped}')
                page_swipes += 1
            self._print_queue()
            print()
        print(f'Page swaps: {page_swipes}')
        print(f'Finish Optimal with count of frames: {self.size}')


class FIFOPageWorker(PageWorker):

    def _put(self, value: int) -> Optional[int]:
        popped = None
        if value in self.values_set:
            return
        if len(self.queue) == self.size:
            popped = self._pop(0)
        self._append(value)
        return popped

    def run(self) -> None:
        page_swipes = 0
        print(f'Execution FIFO')
        print(f'Count of frames: {self.size}')
        print()
        for page in PAGES:
            print(f'Using page: {page}')
            popped = self._put(page)
            if popped is not None:
                print(f'Removed page: {popped}')
                page_swipes += 1
            self._print_queue()
            print()
        print(f'Page swaps: {page_swipes}')
        print(f'Finish FIFO with count of frames: {self.size}')


class LRUPageWorker(PageWorker):

    def slice_list(self, value: int) -> None:
        index = self.queue.index(value)
        self.queue.pop(index)
        self._append(value)

    def _put(self, value: int) -> Optional[int]:
        popped = None
        if value in self.values_set:
            self.slice_list(value)
            return
        if len(self.queue) == self.size:
            popped = self._pop(0)
        self._append(value)
        return popped

    def run(self) -> None:
        page_swipes = 0
        print(f'Execution LRU')
        print(f'Count of frames: {self.size}')
        print()
        for page in PAGES:
            print(f'Using page: {page}')
            popped = self._put(page)
            if popped is not None:
                print(f'Removed page: {popped}')
                page_swipes += 1
            self._print_queue()
            print()
        print(f'Page swaps: {page_swipes}')
        print(f'Finish LRU with count of frames: {self.size}')


def main():
    size = MEMORY_SIZE
    FIFOPageWorker(size).run()
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    LRUPageWorker(size).run()
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    OptimalPageWorker(size).run()


if __name__ == '__main__':
    main()
