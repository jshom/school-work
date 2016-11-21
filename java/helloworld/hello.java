import java.util.Scanner;

public class hello {
  public static void main (String[] args) {

    Scanner sc = new Scanner(System.in);
    System.out.println("Input your name");
    String name;
    name = sc.nextLine();
    System.out.println("hello, " + name);

  }
}
