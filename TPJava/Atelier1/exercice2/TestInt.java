package exercice2;

public class TestInt {

    public static void main(String[] args) {

        Int myInt1 = new Int(0, 6);
        Int myInt2 = new Int(12, 0, 6);
        Int myInt3 = new Int(0,0, 6);

        //System.out.println(myInt1.equals(myInt2));
        //System.out.println(myInt1.equals(myInt3));

        CrazyInt crazyInt1 = new CrazyInt(10, 0, 250, 4);
        System.out.println(crazyInt1.getValue());
        crazyInt1.increment();
        System.out.println(crazyInt1.getValue());
    }
}
