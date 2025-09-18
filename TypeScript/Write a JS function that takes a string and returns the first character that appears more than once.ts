function findCharacterThatAppearsMoreThanOnce(text: string): string {
  try {
    const characterFrequencyMapping = {};
    for (const char of text) {
      if (char in characterFrequencyMapping) {
        characterFrequencyMapping[char] += 1;
      } else {
        characterFrequencyMapping[char] = 1;
      }
      if (characterFrequencyMapping[char] > 1) {
        return char;
      }
    }
    return "No repeated character";
  } catch (error) {
    console.error(error);
    throw error;
  }
}

function main() {
  const result = findCharacterThatAppearsMoreThanOnce("Ahammed");
  console.log(result);
}

main();


