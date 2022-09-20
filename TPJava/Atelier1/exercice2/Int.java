package exercice2;

public class Int {

    protected int value;
    protected final int min;
    protected final int max;

    /**
     * Constructor
     * @param value
     * @param min
     * @param max
     */
    public Int(int value, int min, int max){
        this.min = min;
        this.max = max;
        this.value = value;
    }

    /**
     * Constructor, value defaults to 0
     * @param min
     * @param max
     */
    public Int(int min, int max){
        this(0, min, max);
    }

    public void increment(){
        if(value != max){
            value++;
        }
    }

    /**
     * Increment instance's value by n if possible otherwise does nothing.
     * @param n
     */
    public void increment(int n){
        if( (value + n) < max){
            value++;
        }
    }

    // Getters
    public int[] getLimit(){
        return new int[]{min, max};
    }

    public int getValue(){
        return value;
    }

    // Setters
    public void setValue(int value){

        if(value >= min && value <= max){
            this.value = value;
        }
    }

    public String toString(){
        return String.format("value : %d, minimum value : %d, maximum value : %d", value, min, max);
    }

    public Boolean equals(Int anInt){

        return (this.value == anInt.value && this.min == anInt.min && this.max == anInt.max);
    }
}
