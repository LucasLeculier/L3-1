package exercice1;

import java.util.*;

public class LoadedDice extends Dice {

    private int minimumValue;

    public LoadedDice(int minimumValue, int faces, String name){
        super(name, faces);

        if(minimumValue < faces && minimumValue > 0){
            this.minimumValue = minimumValue;
        } else {
            this.minimumValue = 1;
        }
    }

    public int throwDice(){

        int dice = r.nextInt(this.faces + 1) + minimumValue;

        return Math.min(dice, this.faces);
    }
}
