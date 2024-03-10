package main

import "fmt"

func getCommon(nums1 []int, nums2 []int) int {
	for _, num1 := range nums1 {
		for _, num2 := range nums2 {
			if num1 == num2 {
				return num1
			}
			// no need to go further since the two slices are sorted
			if num2 > num1 {
				break
			}
		}
	}
	return -1
}

func main() {
	nums1, nums2 := []int{2, 4}, []int{1, 2}

	fmt.Println(getCommon(nums1, nums2))
}
