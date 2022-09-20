package exercice1;

public class TestDice {

    public static void main(String[] args) {

        Dice dice1 = new Dice();
        Dice dice2 = new Dice("");
        Dice dice3 = new Dice(12);

        // System.out.println("Dice throw : " + dice3.throwDice());
        // System.out.println(dice2.getName());
        // System.out.println("Current number of dices created : " + Dice.getNumberOfDices());

        // System.out.println(dice3.throwDice(10));

        // System.out.println(dice3);

        // LoadedDice loadedDice1 = new LoadedDice(6, 10, "");

        // System.out.println(loadedDice1);

        // System.out.println(loadedDice1.throwDice());

        /*
        MemoryDice memoryDice1 = new MemoryDice("", 12);

        int n = 20;

        for(int i = 0; i < n; i++){
            System.out.println(memoryDice1.throwDice());
        }
        */

        StringDice stringDice1 = new StringDice("", new String[]{"Bravo", "C'est bien", "Bof bof"});

        System.out.println(stringDice1);

        System.out.println(stringDice1.throwDiceString());
    }
}
