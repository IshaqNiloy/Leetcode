package main

import "fmt"

func findDuplicate(nums []int) int {
	//{0, 5, 9, 6, 4, 3, 8, 4, 7, 1}
	slow := nums[0]
	fast := nums[0]
	fmt.Println(slow)
	fmt.Println(fast)
	fmt.Println("-----------------------")
	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		fmt.Println("slow", slow)
		fmt.Println("fast", fast)

		if slow == fast {
			break
		}
	}
	slow = nums[0]
	var cnt = 0
	for nums[slow] != nums[fast] {
		cnt++
		//fmt.Println("slow: ", slow, " fast: ", fast)
		slow = nums[slow]
		fast = nums[fast]
	}
	//fmt.Println(cnt)
	return fast
}

func main() {
	nums := []int{1, 5, 9, 6, 2, 3, 8, 4, 7, 0}
	result := findDuplicate(nums)
	fmt.Println(result)
}
