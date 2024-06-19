from typing import List


class MinHeap:
    def __init__(self, arr: List[int]) -> None:
        self.heap = self.build(arr)

    def get_left_child(self, index: int) -> int:
        return (index * 2)

    def get_right_child(self, index: int) -> int:
        return (index * 2) + 1

    def get_parent(self, index: int) -> int:
        return (index // 2) - 1

    def swap(self, i: int, j: int, arr: List[int]) -> None:
        arr[i], arr[j] = arr[j], arr[i]

    def build(self, arr: List[int]) -> List[int]:
        """
        Builds a heap from the given array.

        Args:
            arr (List[int]): The input array to be converted into a heap.

        Returns:
            List[int]: The input array converted into a heap.

        This function takes an array `arr` as input and converts it into a heap.
        It does this by iterating through the array in reverse order, starting from the last index.
        For each element, it compares the element with its parent and swaps them if the element is smaller than
        the parent. This process continues until the entire array is in the form of a heap.
        """
        last_index = len(arr) - 1

        while arr[last_index] < arr[self.get_parent(last_index)] and last_index != 0:
            parent_index = self.get_parent(last_index)
            self.swap(last_index, parent_index, arr)
            last_index = parent_index

        return arr


if __name__ == "__main__":
    minHeap = MinHeap([2, 5, 4, 8, 13, 6, 1])
    print(minHeap.heap)
