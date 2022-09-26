package testquestions;

import question1.Personne;
import question2.Employe;

public class TestQuestion1 {
    public static void main(String[] args) {

        Personne personne1 = new Personne("Leblanc", "Juste", 1, 4, 1990, 1, "Rue", "10000", "Paris");
        Personne personne2 = new Personne("Attends", "Charles", 1, 4, 1995, 1, "Rue", "10000", "Marseille");
        Personne personne3 = new Personne("Attends", "Charles", 1, 4, 1995, 1, "Rue", "10000", "Marseille");


        //System.out.println(Personne.getNbPersonnes());
        //System.out.println(Personne.plusAgee(personne2, personne1));
        //System.out.println(personne1.plusAgee(personne2));
        //System.out.println(personne2.equals(personne3));

        Employe employe1 = Employe.createEmploye("Leblanc", "Juste", 1, 4, 1990, 1, "Rue", "10000", "Paris");
        System.out.println(employe1);
    }
}
