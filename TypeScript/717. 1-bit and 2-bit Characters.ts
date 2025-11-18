function isOneBitCharacter(bits: number[]): boolean {
  try {
    // If the length of the array is one
    if (bits.length === 1 && bits[0] === 0) {
      return true;
    } else if (bits.length === 1 && bits[0] === 1) {
      return false;
    }

    // IF the last bit is 1 then it is always a two bit character
    if (bits[bits.length - 1] === 1) {
      return false;
    }

    let i: number = 0;

    while (i < bits.length) {
      // The array always ends with 0. So no need to check that.
      // If the last bit can be read then it means that the last bit represents a one bit character. Otherwise, a two bit character.
      if (i === bits.length - 1) {
        return true;
      }

      // If the bit is 0 then continue by only increasing i by 1 since it represents a one bit character.
      if (bits[i] === 0) {
        i += 1;
        continue;
      }
      // If the bit is 1 then take the next bit and increase i by 2 since it represents a two bit character.
      else if (bits[i] === 1 && i !== bits.length - 1) {
        i += 2;
      }
    }

    return false;
  } catch (error) {
    throw error;
  }
}

console.log(isOneBitCharacter([0, 1, 0]));
