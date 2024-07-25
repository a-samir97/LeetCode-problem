class Solution:
    def merge(self, nums, left, mid, right):
        left_list_length = mid - left + 1
        right_list_length = right - mid

        left_list = [0] * left_list_length
        right_list = [0] * right_list_length

        # fill in left list 
        for i in range(left_list_length):
            left_list[i] = nums[left + i]

        # fill in right list
        for i in range(right_list_length):
            right_list[i] = nums[mid + 1 + i]

        # merging the array
        left_list_index = 0
        right_list_index = 0
        original_list_index = left

        while left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                nums[original_list_index] = left_list[left_list_index]
                left_list_index += 1
            else:
                nums[original_list_index] = right_list[right_list_index]
                right_list_index += 1
            original_list_index += 1
    
        # put the remaining elements in left array
        while left_list_index < left_list_length:
            nums[original_list_index] = left_list[left_list_index]
            left_list_index += 1
            original_list_index += 1

        # put the remaining elements in right array
        while right_list_index < right_list_length:
            nums[original_list_index] = right_list[right_list_index]
            right_list_index += 1
            original_list_index += 1

    def merge_sort(self, nums, left, right):
        # base case
        if left >= right:
            return

        # splitting array 
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums