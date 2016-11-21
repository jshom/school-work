public class DiceMain {
  public static void main (String[] args) {
    /*Dice myDie = new Dice();
    for (int i = 0; i < 5; i++) {
      myDie.roll();
      System.out.println(myDie.getNum());
    }*/

    Dice die1 = new Dice();
    Dice die2 = new Dice();

    int numOfRolls = 0;

    while (die1.getNum() + die2.getNum() != 2) {
      numOfRolls++;
      die1.roll();
      die2.roll();
      System.out.println("FIRST: " + die1.getNum() + " | SECOND: " + die2.getNum() + " | ROLLS: " + numOfRolls);
    }
  }
}
