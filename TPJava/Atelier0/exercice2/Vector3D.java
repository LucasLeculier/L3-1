package exercice2;

public class Vector3D {

    private double x, y, z;

    /**
     * Non default constructor
     * @param x
     * @param y
     * @param z
     */
    public Vector3D(double x, double y, double z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    /**
     * Default constructor, x y and z default to 0
     */
    public Vector3D(){
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    /**
     * Displays coordinates
     */
    public void displayCoordinates(){
        System.out.format("<%f, %f, %f>", this.x, this.x, this.z);
    }

    public double getNorm(){

        return (Math.sqrt( (this.x * this.x) + (this.y * this.y) + (this.z * this.z)));
    }

    /**
     * Returns the dot product between this instance and vector3D
     * @param vector3D
     * @return
     */
    public double dotProduct(Vector3D vector3D){

        return ((this.x * vector3D.x) + (this.y * vector3D.y) + (this.z * vector3D.z));
    }

    /**
     * Returns the dot product between v1 and v2
     * @param v1
     * @param v2
     * @return
     */
    public static double dotProduct(Vector3D v1, Vector3D v2){

        return ((v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z));
    }

    /**
     * Returns the Vector3D corresponding of the sum between the instance and vector3D
     * @param vector3D
     * @return
     */
    public Vector3D sum(Vector3D vector3D){

        return new Vector3D(this.x + vector3D.x, this.y + vector3D.y, this.z + vector3D.z);
    }

    /**
     * Returns the Vector3D of the sum between v1 and v2
     * @param v1
     * @param v2
     * @return
     */
    public static Vector3D sum(Vector3D v1, Vector3D v2){

        return new Vector3D(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z);
    }
}
