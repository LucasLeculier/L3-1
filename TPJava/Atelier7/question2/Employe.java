package question2;

import question1.Personne;

import java.time.LocalDate;
import java.time.Period;
import java.util.GregorianCalendar;

public class Employe extends Personne {

    protected static double salaire = 0.0;

    protected GregorianCalendar dateEmbauche = null;

    /**
     * Constructeur
     * @param leNom
     * @param lePrenom
     * @param j
     * @param m
     * @param a
     * @param numero
     * @param rue
     * @param code_postal
     * @param ville
     */
    protected Employe(String leNom, String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
        super(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville);
        dateEmbauche = new GregorianCalendar(a, m, j);
    }

    /**
     * Crée un employé si son age est supérieur à 18 ans et inférieur à 65
     * @param leNom
     * @param lePrenom
     * @param j
     * @param m
     * @param a
     * @param numero
     * @param rue
     * @param code_postal
     * @param ville
     * @return
     */

    /**
     * Augmente le salaire de tous le employés par un pourcentage donné qui ne peut pas etre négatif
     * @param leNom
     * @param lePrenom
     * @param j
     * @param m
     * @param a
     * @param numero
     * @param rue
     * @param code_postal
     * @param ville
     * @return
     */
    public static Employe createEmploye(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){

        Employe employe;

        int age = Period.between(LocalDate.of(a, m, j), LocalDate.now()).getYears();

        if(age > 16 && age < 65){
            employe = new Employe(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville);
        } else {
            employe = null;
        }

        return employe;
    }

    public static void augmenterSalaire(double pourcentage){
        if(pourcentage >= 0){
            salaire = salaire + (salaire * (pourcentage/100));
        }
    }

    /*public int calculAnnuite(){

    }*/

}
