function isValid(s: string): boolean {
  try {
    const stack: string[] = [];
    const map: Record<string, string> = {
      "(": ")",
      "{": "}",
      "[": "]",
    };

    for (const char of s) {
      // Opening parentheses
      if (map[char]) {
        stack.push(char);
      }
      // Closing parentheses
      else {
        const popedElement = stack.pop();
        if (!popedElement || map[popedElement] !== char) return false;
      }
    }

    return stack.length === 0;
  } catch (error) {
    throw error;
  }
}

function main() {
  console.log(isValid("([)]"));
}

main();
