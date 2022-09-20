package exercice1;

public class OtherDice extends Dice {

    private String[] options;
    private int[] optionsInt;

    /**
     * Constructor with string values
     * @param name
     * @param options
     */
    public OtherDice(String name, String[] options){
        super(name, options.length);
        this.options = options.clone();
    }

    /**
     * Constructor with int values
     * @param name
     * @param options
     */
    public OtherDice(String name, int[] options){
        super(name, options.length);
        this.optionsInt = options;
    }

    public int throwDice(){

        return r.nextInt(this.faces);
    }

    /**
     * Returns a random string in options
     * @return
     */
    public String throwOtherDice(){

        return options[throwDice()];
    }

}
