def bubble_sort(numbs):
    for i in range(len(numbs) - 1, 0, -1):
        for j in range(i):
            if numbs[j] > numbs[j + 1]:
                temp = numbs[j]
                numbs[j] = numbs[j + 1]
                numbs[j + 1] = temp


def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_pos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_pos]:
                min_pos = j

        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp


numbs = [5, 3, 8, 6, 7, 2, 1]
selection_sort(numbs)
print(numbs)
