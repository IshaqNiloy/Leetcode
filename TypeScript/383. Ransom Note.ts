function canConstruct(ransomNote: string, magazine: string): boolean {
  try {
    const charFrequencyMapping: Record<string, number> = {};
    for (const char of magazine) {
      if (char in charFrequencyMapping) {
        charFrequencyMapping[char] += 1;
      } else {
        charFrequencyMapping[char] = 1;
      }
    }

    for (const char of ransomNote) {
      if (
        charFrequencyMapping[char] === undefined ||
        charFrequencyMapping[char] === 0
      ) {
        return false;
      } else {
        charFrequencyMapping[char] -= 1;
      }
    }

    return true;
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(canConstruct("aa", "aab"));
}

main();
