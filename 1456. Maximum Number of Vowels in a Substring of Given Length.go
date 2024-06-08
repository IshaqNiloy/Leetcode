package main

import "fmt"

func maxVowels(s string, k int) int {
	if len(s) < k {
		return 0
	}
	vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
	maxCounter := 0
	counter := 0

	for i := 0; i < k; i++ {
		if vowels[s[i]] {
			counter++
		}
	}

	if counter > maxCounter {
		maxCounter = counter
	}

	for i := k; i < len(s); i++ {
		if vowels[s[i-k]] {
			counter--
		}
		if vowels[s[i]] {
			counter++
		}
		if counter > maxCounter {
			maxCounter = counter
		}
	}

	return maxCounter
}

func main() {
	fmt.Println("Maximum number of vowels in a substring: ", maxVowels("aeiou", 2))
}
