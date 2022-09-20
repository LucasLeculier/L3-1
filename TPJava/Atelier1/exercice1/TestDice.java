package exercice1;

public class TestDice {

    public static void main(String[] args) {

        Dice dice1 = new Dice();
        Dice dice2 = new Dice("Hello");
        Dice dice3 = new Dice(12);

        System.out.println("Dice throw : " + dice3.throwDice());
    }
}
