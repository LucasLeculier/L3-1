package exercice1;

public class MemoryDice extends Dice {

    private int lastThrow = 0;

    /**
     * Constructor
     * @param name
     * @param faces
     */
    public MemoryDice(String name, int faces){
        super(name, faces);
    }

    /**
     * Prevents the dice from returning the same value twice
     * @return
     */
    public int throwDice(){

        int dice = super.throwDice();

        while (dice == lastThrow){
            dice = super.throwDice();
        }

        lastThrow = dice;

        return dice;
    }
}
