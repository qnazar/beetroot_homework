from typing import List


class MaxBinHeap:
    def __init__(self) -> None:
        self.heap_list: List[int] = [0]
        self.size: int = 0

    def build_heap(self, items: List[int]) -> None:
        i = len(items) // 2
        self.size = len(items)
        self.heap_list = [0] + items[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def perc_up(self, i: int) -> None:
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def perc_down(self, i: int) -> None:
        while i * 2 <= self.size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def max_child(self, i: int) -> int:
        # якщо виходимо за межі списку, повертаємо останній елемент
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap_list[i*2] > self.heap_list[i * 2 + 1]:  # ліва дитина
            return i * 2
        else:  # права дитина
            return i * 2 + 1

    def del_max(self) -> int:
        # хочемо отримати перший елем, бо він найбільший. Зберегли його в змінну
        ret_val = self.heap_list[1]
        # записуємо в перший елемент значення останнього
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        # видаляємо дублікат останнього елема
        self.heap_list.pop()
        # переміщумо перезаписаний перший елем на своє місце
        self.perc_down(1)
        return ret_val

    def insert(self, k: int) -> None:
        self.heap_list.append(k)
        self.size += 1
        self.perc_up(self.size)


if __name__ == '__main__':
    h = MaxBinHeap()
    h.build_heap([17, 3, 2, 7, 26, 1, 25, 100, 19])
    print(h.heap_list)
    h.insert(30)
    print(h.heap_list)
    print(h.del_max())
    print(h.heap_list)
