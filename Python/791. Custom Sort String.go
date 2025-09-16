package main

import "fmt"

func customSortString(order string, s string) string {
	charOrderMapping := make(map[string]int)
	position := 1
	var result, sortedString, unsortedString string

	for _, char := range order {
		charOrderMapping[string(char)] = position
		position += 1
	}

	for key, _ := range charOrderMapping {
		for _, char := range s {
			if key == string(char) {
				sortedString += key
			}
		}
		if
		unsortedString += char
	}

	return result
}

func main() {
	order := "cba"
	s := "abcd"

	fmt.Println(customSortString(order, s))

}
