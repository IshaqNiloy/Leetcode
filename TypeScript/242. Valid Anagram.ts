function isAnagram(s: string, t: string): boolean {
  try {
    if (s.length !== t.length) {
      return false;
    }

    const characterFrequencyMapping: Record<string, number> = {};

    for (const char of t) {
      if (char in characterFrequencyMapping) {
        characterFrequencyMapping[char] += 1;
      } else {
        characterFrequencyMapping[char] = 1;
      }
    }

    for (const char of s) {
      if (
        characterFrequencyMapping[char] === undefined ||
        characterFrequencyMapping[char] === 0
      ) {
        return false;
      }
      characterFrequencyMapping[char] -= 1;
    }
    return true;
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(isAnagram("rat", "car"));
}

main();
