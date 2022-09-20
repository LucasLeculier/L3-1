package exercice1;

public class MemoryDice extends Dice {

    private int lastThrow = 0;

    public MemoryDice(String name, int faces){
        super(name, faces);
    }

    /**
     * Prevents the dice from returning the same value twice
     * @return
     */
    public int memoryThrow(){

        int dice = throwDice();

        while (dice == lastThrow){
            dice = throwDice();
        }

        lastThrow = dice;

        return dice;
    }
}
