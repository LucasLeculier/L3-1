package exercice1;

public class StringDice extends Dice {

    private String[] options;

    /**
     * Constructor
     * @param name
     * @param options
     */
    public StringDice(String name, String[] options){
        super(name, options.length);
        this.options = options.clone();
    }

    /**
     * Returns a random string in options
     * @return
     */
    public String throwDiceString(){

        return options[throwDice()];
    }
}
