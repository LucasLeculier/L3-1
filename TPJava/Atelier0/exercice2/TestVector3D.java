package exercice2;

public class TestVector3D {

    public static void main(String[] args) {
        Vector3D v1 = new Vector3D(3.0, 2.0, 5.0);

        System.out.println(v1.getNorm());

        Vector3D v2 = new Vector3D(1.0, 2.0, 3.0);

        System.out.println(v2.getNorm());

        System.out.println(Vector3D.sum(v1, v2));
    }
}
