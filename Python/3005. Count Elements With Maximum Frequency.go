package main

import "fmt"

func maxFrequencyElements(nums []int) int {
	numberOccurrenceMapping := constructNumberOccurrenceMapping(nums)
	maxValue, maxValueOccurrence := -1, 0

	for _, value := range numberOccurrenceMapping {
		if value > maxValue {
			maxValue = value
			maxValueOccurrence = 0
		}
		if value == maxValue {
			maxValueOccurrence += maxValue
		}
	}
	return maxValueOccurrence
}

func constructNumberOccurrenceMapping(num []int) map[int]int {
	var numberOccurrenceMapping = make(map[int]int)

	for _, num := range num {
		if _, exists := numberOccurrenceMapping[num]; exists {
			numberOccurrenceMapping[num] += 1
		} else {
			numberOccurrenceMapping[num] = 1
		}
	}

	return numberOccurrenceMapping
}

func main() {
	var nums = []int{1, 2, 2, 3, 1, 4}
	fmt.Println(maxFrequencyElements(nums))
}
