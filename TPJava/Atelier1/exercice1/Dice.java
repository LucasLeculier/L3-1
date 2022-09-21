package exercice1;

import java.util.*;

public class Dice {

    protected static int numberOfDices = 0;

    private static final int MIN_FACES = 3;
    private static final int MAX_FACES = 120;
    protected static Random r = new Random();
    protected String name;

    protected int faces;

    /**
     * Constructor with both name and faces
     * @param name
     * @param faces
     */
    public Dice(String name, int faces){

        numberOfDices += 1;

        if(name != null && !name.isBlank()){
            this.name = name;
        } else {
            this.name = "Dice n° " + numberOfDices;
        }

        if (faces < MIN_FACES) {
            this.faces = MIN_FACES;
        } else if(faces > MAX_FACES) {
            this.faces = MAX_FACES;
        } else {
            this.faces = faces;
        }
    }

    /**
     * Default constructor
     */
    public Dice(){
        this("", 6);
    }

    /**
     * Constructor
     * @param faces
     */
    public Dice(int faces){
        this("", faces);
    }

    /**
     * Constructor
     * @param name
     */
    public Dice(String name){
        this(name, 6);
    }


    /**
     * Throws the dice and returns a random integer between 1 and the number of faces
     * @return
     */
    public int throwDice(){

        return r.nextInt(this.faces + 1);
    }

    /**
     * Throws the dice n amount of times and returns the best throw
     * @param n
     * @return
     */
    public int throwDice(int n){

        int currentBest = 0;

        int[] diceThrows = new int[n];

        for(int i = 0; i < n; i++){

            int dice = r.nextInt(this.faces + 1);

            diceThrows[i] = dice;

            if(currentBest < dice){
                currentBest = dice;
            }
        }

        System.out.println(Arrays.toString(diceThrows));

        return currentBest;
    }


    // Getters

    public String getName() {
        return name;
    }

    public int getFaces(){
        return faces;
    }

    public static int getNumberOfDices(){
        return numberOfDices;
    }

    // Setters

    public void setFaces(int faces){

        if(faces >= 3 && faces <= 120){
            this.faces = faces;
        } else {
            System.err.println("Number of faces invalid, needs to be between 3 and 120.");
        }
    }

    public String toString(){
        return String.format("Name : %s, Faces : %d", name, faces);
    }
}
