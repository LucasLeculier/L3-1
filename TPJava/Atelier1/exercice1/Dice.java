package exercice1;

import java.util.*;

public class Dice {

    private static Random r = new Random();
    private String name;

    private int faces;

    /**
     * Default constructor
     */
    public Dice(){
        this.name = "Dice";
        this.faces = 6;
    }

    /**
     * Constructor
     * @param faces
     */
    public Dice(int faces){
        this.name = "Dice";
        this.faces = faces;
    }

    /**
     * Constructor
     * @param name
     */
    public Dice(String name){
        this.name = name;
        this.faces = 6;
    }

    /**
     * Throws the dice and returns a random integer between 0 and the number of faces
     * @return
     */
    public int throwDice(){

        return r.nextInt(this.faces + 1);
    }


    // Getters

    public String getName() {
        return name;
    }

    public int getFaces(){
        return faces;
    }

    // Setters

    public void setFaces(int faces){
        this.faces = faces;
    }
}
