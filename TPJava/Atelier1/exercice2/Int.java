package exercice2;

public class Int {

    protected int value;
    protected final int MIN;
    protected final int MAX;

    /**
     * Constructor
     * @param value
     * @param min
     * @param max
     */
    public Int(int value, int min, int max){
        this.MIN = min;
        this.MAX = max;
        if((value > min) && (value < max)){
            this.value = value;
        } else {
            this.value = min;
        }
    }

    /**
     * Constructor, value defaults to 0
     * @param min
     * @param max
     */
    public Int(int min, int max){
        this(min, min, max);
    }

    /**
     * Increments the value by one if possible
     */
    public void increment(){
        if(value != MAX){
            value++;
        }
    }

    /**
     * Increment instance's value by n if possible otherwise does nothing.
     * @param n
     */
    public void increment(int n){
        if( (value + n) < MAX){
            value += n;
        }
    }

    // Getters
    public int[] getLimit(){
        return new int[]{MIN, MAX};
    }

    public int getValue(){
        return value;
    }

    // Setters
    public void setValue(int value){

        if(value >= MIN && value <= MAX){
            this.value = value;
        }
    }

    public String toString(){
        return String.format("value : %d, minimum value : %d, maximum value : %d", value, MIN, MAX);
    }

    public Boolean equals(Int anInt){

        return ((this.value == anInt.value) && (this.MIN == anInt.MIN) && (this.MAX == anInt.MAX));
    }
}
