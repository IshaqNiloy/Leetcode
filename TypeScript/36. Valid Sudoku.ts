function isValidSudoku(board: string[][]): boolean {
  try {
    let numberFrequencyMapping: any = {};

    // Check if rows are valid
    for (const row of board) {
      for (const num of row) {
        if (num in numberFrequencyMapping) {
          numberFrequencyMapping[num] += 1;
        } else {
          numberFrequencyMapping[num] = 1;
        }
      }
      /*
      There can be multiple dots that represent empty spaces.
      So we need to ignore them.
      */
      delete numberFrequencyMapping["."];
      // Check if the the row has any duplicate number
      if (
        Object.values(numberFrequencyMapping).some((count: any) => count > 1)
      ) {
        return false;
      }
      numberFrequencyMapping = {};
    }

    // Check if columns are valid
    for (let column = 0; column < board.length; column++) {
      for (let row = 0; row < board.length; row++) {
        if (board[row][column] in numberFrequencyMapping) {
          numberFrequencyMapping[board[row][column]] += 1;
        } else {
          numberFrequencyMapping[board[row][column]] = 1;
        }
      }
      // Check if the the column has any duplicate number
      delete numberFrequencyMapping["."];
      if (
        Object.values(numberFrequencyMapping).some((count: any) => count > 1)
      ) {
        return false;
      }
      numberFrequencyMapping = {};
    }
    return true;
  } catch (error) {
    console.log(error);
  }
}

function main() {
  const result = isValidSudoku([
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
  ]);
  console.log(result);
}

main();
