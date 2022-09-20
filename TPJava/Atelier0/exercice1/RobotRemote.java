package exercice1;

public class RobotRemote {

    public static void main(String[] args) {

        Robot myRobotToto = new Robot("Toto", 10, 20, Robot.SOUTH);

        Robot myRobotTiti = new Robot("Titi", 0, 0, Robot.NORTH);

        // Movement of Toto
        myRobotToto.move();
        myRobotToto.changeOrientation(Robot.WEST);
        myRobotToto.move();

        // Movement of Titi
        myRobotTiti.move();
        myRobotTiti.changeOrientation(Robot.WEST);
        myRobotTiti.move();

        System.out.println(myRobotToto);
        System.out.println(myRobotTiti);
    }
}
