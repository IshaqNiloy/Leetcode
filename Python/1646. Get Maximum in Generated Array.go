package main

import (
	"fmt"
)

func getMaximumGenerated(n int) int {
	// edge cases
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 1
	}

	arr := []int{}
	arr = append(arr, 0)
	arr = append(arr, 1)

	i := 1
	for ; i <= (n-1)/2; i++ {
		arr = append(arr, arr[i])
		arr = append(arr, arr[i]+arr[i+1])
	}

	if n%2 == 0 {
		arr = append(arr, arr[i])
	}

	maxValue := 0

	for i := 0; i < len(arr); i++ {
		if arr[i] > maxValue {
			maxValue = arr[i]
		}
	}

	return maxValue
}

func main() {
	n := 8
	result := getMaximumGenerated(n)
	fmt.Println(result)
}
