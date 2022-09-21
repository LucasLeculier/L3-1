package exercice1;

public class LoadedDice extends Dice {

    private final int MINIMUM_VALUE;

    public LoadedDice(int MINIMUM_VALUE, int faces, String name){
        super(name, faces);

        if(MINIMUM_VALUE < faces && MINIMUM_VALUE > 0){
            this.MINIMUM_VALUE = MINIMUM_VALUE;
        } else {
            this.MINIMUM_VALUE = 1;
        }
    }

    /**
     * Throws the dice and returns a value between the minimum value and the faces value
     * @return
     */
    public int throwDice(){

        int dice = r.nextInt(this.faces + 1) + MINIMUM_VALUE;

        return Math.min(dice, this.faces);
    }
}
