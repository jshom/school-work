import java.util.Random;
public class Dice {
  // -- Value inits
  private int rolls;
  private int sides;
  private int result;
  private Random r;

  // -- Init Class
  public Dice () {
    this.rolls = 0;
    this.sides = 6;
    this.r = new Random();
  }

  public Dice (int sides) {
    this.rolls  = 0;
    this.sides  = sides;
    this.r      = new Random();
  }

  // -- Init Methods

  public void roll () {
    this.result = r.nextInt(sides) + 1;
    //return result;
  }

  public int getNum () {
    return result;
  }

  public int getSides () {
    return sides;
  }

  public void setSides (int numOfSides) {
    this.sides = numOfSides;
  }
}
