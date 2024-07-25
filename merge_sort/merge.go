func merge(nums []int, left int, mid int, right int) {

	leftLength := mid - left + 1
	rightLength := right - mid

	tempLeftArray := []int{}
	tempRightArray := []int{}

	// fill in the temp arrays

	for i := 0; i < leftLength; i++ {
		tempLeftArray = append(tempLeftArray, nums[left+i])
	}

	for i := 0; i < rightLength; i++ {
		tempRightArray = append(tempRightArray, nums[mid+1+i])
	}

	// merging the array

	leftIndex := 0
	rightIndex := 0
	mergedIndex := left

	for {
		if leftIndex >= leftLength || rightIndex >= rightLength {
			break
		}

		// checking and merging :D
		if tempLeftArray[leftIndex] <= tempRightArray[rightIndex] {
			nums[mergedIndex] = tempLeftArray[leftIndex]
			leftIndex += 1
		} else {
			nums[mergedIndex] = tempRightArray[rightIndex]
			rightIndex += 1
		}

		mergedIndex += 1
	}

	// merging the remaining left sub array
	for i := leftIndex; i < leftLength; i++ {
		nums[mergedIndex] = tempLeftArray[leftIndex]
		leftIndex += 1
		mergedIndex += 1
	}

	// merging the remaining right sub array
	for i := rightIndex; i < rightLength; i++ {
		nums[mergedIndex] = tempRightArray[rightIndex]
		rightIndex += 1
		mergedIndex += 1
	}
}

func mergeSort(nums []int, left int, right int) {
	if left >= right {
		return
	}

	mid := (left + right) / 2
	mergeSort(nums, left, mid)    // left part of the array
	mergeSort(nums, mid+1, right) // right part of the array

	merge(nums, left, mid, right)
}

func sortArray(nums []int) []int {
	mergeSort(nums, 0, len(nums)-1)
	return nums
}