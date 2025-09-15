function canBeTypedWords(text: string, brokenLetters: string): number {
  const brokenChars = [...brokenLetters];
  const words = text.split(" ");
  let initialCount = words.length;

  for (const word of words) {
    for (const brokenChar of brokenChars) {
      if (word.includes(brokenChar)) {
        initialCount -= 1;
        break;
      }
    }
  }

  return initialCount;
}

function main() {
  const result = canBeTypedWords("hello world", "ad");
  console.log(result);
}

main();
