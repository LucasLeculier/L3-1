package exercice1;

public class RobotRemote {

    public static void main(String[] args) {


        final int NORTH = 1;
        final int EAST = 2;
        final int SOUTH = 3;
        final int WEST = 4;

        Robot myRobotToto = new Robot("Toto", 10, 20, SOUTH);

        Robot myRobotTiti = new Robot("Titi", 0, 0, NORTH);

        // Movement of Toto
        myRobotToto.move();
        myRobotToto.changeOrientation(WEST);
        myRobotToto.move();

        // Movement of Titi
        myRobotTiti.move();
        myRobotTiti.changeOrientation(WEST);
        myRobotTiti.move();

        System.out.println(myRobotToto);
        System.out.println(myRobotTiti);
    }
}
