package main

import "fmt"

func pivotInteger(n int) int {
	sumBeforePivot, sumAfterPivot, pivot := 0, n, n

	for i := 1; i <= n; i++ {
		if sumBeforePivot == sumAfterPivot && i == pivot {
			fmt.Println(sumAfterPivot)
			fmt.Println(sumBeforePivot)
			return pivot
		} else if sumBeforePivot < sumAfterPivot {
			sumBeforePivot += i

		} else {
			fmt.Println("Before================")
			fmt.Println(i)
			fmt.Println(sumBeforePivot)
			fmt.Println(sumAfterPivot)
			fmt.Println(pivot)
			pivot -= 1
			sumBeforePivot += i
			sumAfterPivot += pivot
			fmt.Println("After====================")
			fmt.Println(i)
			fmt.Println(sumBeforePivot)
			fmt.Println(sumAfterPivot)
			fmt.Println(pivot)
		}
	}
	return -1
}

func main() {
	fmt.Println(pivotInteger(8))
}
