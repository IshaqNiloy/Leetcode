function maxFreqSum(s: string): number {
  try {
    const vowels = ["a", "e", "i", "o", "u"];
    const letterFrequencyMapping = new Map();

    // 1. Create the map
    for (const letter of s) {
      if (letter in letterFrequencyMapping) {
        letterFrequencyMapping[letter] += 1;
      } else {
        letterFrequencyMapping[letter] = 1;
      }
    }

    // 2. Find vowel and consonant with maximum frequency
    let vowelWithMaxFrequency = 0;
    let consonantWithMaxFrequency = 0;

    for (const key in letterFrequencyMapping) {
      if (vowels.includes(key)) {
        if (vowelWithMaxFrequency < letterFrequencyMapping[key]) {
          vowelWithMaxFrequency = letterFrequencyMapping[key];
        }
      } else {
        if (consonantWithMaxFrequency < letterFrequencyMapping[key]) {
          consonantWithMaxFrequency = letterFrequencyMapping[key];
        }
      }
    }

    // 3. Return the sum
    return vowelWithMaxFrequency + consonantWithMaxFrequency;
  } catch (error) {
    throw error;
  }
}

function main() {
  const result = maxFreqSum("aeiaeia");
  console.log(result);
}

main();
