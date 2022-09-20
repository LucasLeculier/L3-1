package exercice2;

import java.util.Random;

public class CrazyInt extends Int {

    private Random r = new Random();

    private int craziness;

    /**
     * Constructor
     * @param value
     * @param min
     * @param max
     */
    public CrazyInt(int value, int min, int max, int craziness){
        super(value, min, max);
        this.craziness = craziness;
    }

    /**
     * Increments the CrazyInt by a value between 0 and its craziness amount.
     */
    public void increment(){

        int n = r.nextInt(craziness + 1);

        if( (value + n) < max){
            value += n;
        }
    }
}
