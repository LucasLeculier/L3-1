package exercice3;

public class TestAPI {

    public static void main(String[] args) {

        System.out.println(Math.PI);
        System.out.println(Math.random());
        System.out.println(Math.floor(Math.random() * (3 - 1 + 1) + 1));

        int x1 = 6, x2 = 3;

        System.out.println(Math.max(x1, x2));

        String str1 = "Azerty", str2 = "Qwerty";

        int comparison = str1.compareTo(str2);

        if (comparison < 0){
            System.out.println(str1);
        } else {
            System.out.println(str2);
        }

    }

}