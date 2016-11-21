import java.util.Scanner;
class Roulette {
  public static void main (String[] args) {
    // -- Intro Messages
    String message = "Basic Roulette: If the roll results in 6 you're out. However, get 5 shields to protect yourself.";
    System.out.println("Enter [S] to use your shield or nothing to try your luck");
    System.out.println("Try to get the furthest");
    System.out.println(message);

    // -- Inits
    Dice roulette = new Dice();
    Scanner input = new Scanner(System.in);

    // -- Game Inits
    int luckCount = 0;
    int shieldCount = 5;

    // -- Logic
    while (true) {
      // Find out if choses to use shield
      System.out.print("> ");
      String shield = input.nextLine();
      Boolean usingShield = false;

      // If uses sheild substract it
      // and roll and throw
      roulette.roll();
      int num = roulette.getNum();
      //System.out.println(shield);

      if (shield.contains("S") || shield.contains("s") && shieldCount > 0) {
        //System.out.println("ok");
        shieldCount--;
        usingShield = true;
      } else if (shield.contains("S") || shield.contains("s") && shieldCount == 0) {
        System.out.println("sorry, out of shields");
      } else {
        //System.out.println("sure");
      }

      System.out.println("--------------------------");
      if (num == 6 && usingShield == false) {
        System.out.println("BAMBAM -- try again");
        System.out.println("***");
        System.out.println("Final Score: " + luckCount);
        System.out.println("All reset");
        System.out.println("***");
        luckCount = 0;
        shieldCount = 5;
      } else if (usingShield && num == 6) {
        System.out.println("SAVED... Congrats");
        luckCount++;
        System.out.println("Current Score: " + luckCount + " | Sheild Count: " + shieldCount);
        System.out.println("--------------------------");
      } else if (usingShield && num != 6) {
        System.out.println("Wasted a shield. Sorry bub");
        luckCount++;
        System.out.println("Current Score: " + luckCount + " | Sheild Count: " + shieldCount);
        System.out.println("--------------------------");
      } else {
        System.out.println("lucky... lucky");
        luckCount++;
        System.out.println("Current Score: " + luckCount + " | Sheild Count: " + shieldCount);
        System.out.println("--------------------------");
      }
    }
  }
}
