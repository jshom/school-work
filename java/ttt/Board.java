public class Board {
  // -- Attributes
  private char[][] cells = new char[3][3];

  // -- Constructor
  public Board () {
    for (char[] column : cells) {
      for (char cell : column) {
        cell = ' ';
      }
    }
  }

  // -- Methods
  public boolean setCell (int column, int row, char mark) {
    if (cells[column][row] != ' ') {
      cells[column][row] = mark;
      return true;
    } else {
      return false;
    }
  }

  public char getCell (int column, int row) {
    return cells[column][row];
  }

  public void print () {
    System.out.println("------");
    System.out.println("[" + cells[0][2] +  "][" + cells[1][2] +  "][" + cells[2][2] +  "]");
    System.out.println("[" + cells[0][1] +  "][" + cells[1][1] +  "][" + cells[2][1] +  "]");
    System.out.println("[" + cells[0][0] +  "][" + cells[1][0] +  "][" + cells[2][0] +  "]");
    System.out.println("------");
  }

  public boolean isWinner (char p) {
    boolean hasWon = false;
    // -- Checks for latitude triple
    for (int i = 0 ; i <= 2 ; i++ ) {
      if (cells[i][0] == p && cells[i][1] == p && cells[i][2] == p) {
        hasWon = true;
      }
    }

    // -- Checks for longitude triple
    for (int i = 0 ; i <= 2 ; i++ ) {
      if (cells[0][i] == p && cells[1][i] == p && cells[2][i] == p) {
        hasWon = true;
      }
    }

    // -- Checks for diagonal cases
    //boolean diagonalCase1 = (cells[0][0] == p && cells[1][1] == p && cells[2][2] == p);
    //boolean diagonalCase2 = (cells[0][2] == p && cells[1][1] == p && cells[2][0] == p);

    if ((cells[0][0] == p && cells[1][1] == p && cells[2][2] == p) || (cells[0][2] == p && cells[1][1] == p && cells[2][0] == p)) {
      hasWon = true;
    }

    return hasWon;
  }

  public boolean isTie () {
    boolean allTaken = true;
    for (char[] column : cells) {
      for (char cell : column) {
        if (cell == ' ') {
          allTaken = false;
        }
      }
    }
    return allTaken;
  }
}
