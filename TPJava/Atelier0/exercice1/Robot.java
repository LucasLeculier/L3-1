package exercice1;

public class Robot {

    static final int NORTH = 1;
    static final int EAST = 2;
    static final int SOUTH = 3;
    static final int WEST = 4;

    public static int robotCreatedAmount = 0;

    public String reference;
    public String name;

    public int x, y;

    public int orientation;

    /**
     * Non default constructor.
     * @param name
     * @param xStart
     * @param yStart
     * @param orientationStart
     */
    public Robot(String name, int xStart, int yStart, int orientationStart){

        robotCreatedAmount++;

        this.name = name;

        this.x = xStart;
        this.y = yStart;
        this.orientation = orientationStart;

        this.reference = "ROB" + robotCreatedAmount;
    }

    /**
     * Constructor with default values other than the name.
     * @param name
     */
    public Robot(String name){

        this(name, 0, 0, 1);
    }

    /**
     * Changes the robot's orientation to newOrientation.
     * @param newOrientation
     */
    public void changeOrientation(int newOrientation){

        this.orientation = newOrientation;

    }

    /**
     * Moves the robot 1 unit depending on its current orientation, a robot cannot
     * have negative coordinates.
     */
    public void move(){

        switch(this.orientation) {
            case NORTH: // NORTH
                this.y += 1;
                break;

            case EAST: // EAST
                this.x += 1;
                break;

            case SOUTH: // SOUTH
                if(this.y > 0){
                    this.y -= 1;
                } else {
                    System.out.println("Cannot move to position.\n");
                }
                break;

            case WEST: // WEST
                if(this.x > 0){
                    this.x -= 1;
                } else {
                    System.out.println("Cannot move to position.\n");
                }
                break;
            default:
                System.out.println("Orientation is not valid, robot wasn't moved.\n");
        }

        //System.out.format("%s is currently at coordinates x:%d and y:%d.\n", this.reference, this.x, this.y);
    }

    /**
     * Prints the details of the robot instance
     */
    public void displayDetails(){
        System.out.format("My name is %s, my reference is %s, my current coordinates are x:%d, y:%d and my direction is %d\n",
                this.name,
                this.reference,
                this.x,
                this.y,
                this.orientation
                );
    }

    public String toString(){

        return String.format("My name is %s, my reference is %s, my current coordinates are x:%d, y:%d and my direction is %d\n",
                this.name,
                this.reference,
                this.x,
                this.y,
                this.orientation);
    }
}
