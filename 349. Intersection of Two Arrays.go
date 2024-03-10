package main

import "fmt"

func intersection(nums1 []int, nums2 []int) []int {
	encountered := make(map[int]bool)
	result := []int{}

	for _, num := range nums1 {
		if encountered[num] == false {
			encountered[num] = true
		}
	}

	for _, num := range nums2 {
		if encountered[num] == true {
			result = append(result, num)
			encountered[num] = false
		}
	}
	return result
}

func main() {
	nums1 := []int{4, 9, 5}
	nums2 := []int{9, 4, 9, 8, 4}

	fmt.Println(intersection(nums1, nums2))
}
