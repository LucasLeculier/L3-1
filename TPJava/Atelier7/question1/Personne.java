package question1;

import java.util.*;


public class Personne{

    private static int nbPersonnes = 0;
    protected static final Adresse ADRESSE_INCONNUE = null;
    protected String nom;
    protected String prenom;
    protected final GregorianCalendar dateNaissance;
    protected Adresse adresse = ADRESSE_INCONNUE;

    /**
     * Constructeur de Personne
     * @param leNom le nom de la personne
     * @param lePrenom le prénom de la personne
     * @param laDate la date de naissance de la personne
     * @param lAdresse l'adresse de la personne
     */
    public Personne(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse){
        nom = leNom.toUpperCase();
        prenom=lePrenom;
        dateNaissance=laDate;
        adresse=lAdresse;
        nbPersonnes++;
    }

    /**
     * Constructeur de Personne
     * @param leNom le nom de la personne
     * @param lePrenom le prénom de la personne
     * @param j le jour de naissance
     * @param m le mois de naissance
     * @param a l'année de naissance
     * @param numero le n° de la rue
     * @param rue la rue
     * @param code_postal le code postal de l'adresse
     * @param ville la ville ou la personne habite
     */
    public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
        this(leNom, lePrenom, new GregorianCalendar(a,m,j),new Adresse(numero,rue,code_postal,ville));
    }

    /**
     * Accesseur
     * @return le nombre d'instances de personne
     */
    public static int getNbPersonnes(){
        return nbPersonnes;
    }

    /**
     * Accesseur
     * @return retourne le nom
     */
    public String getNom(){
        return nom;
    }
    /**
     * Accesseur
     * @return retourne le prénom
     */
    public String getPrenom(){
        return prenom;
    }
    /**
     * Accesseur
     * @return retourne la date de naissance
     */
    public GregorianCalendar getDateNaissance() {
        return dateNaissance;
    }
    /**
     * Accesseur
     * @return retourne l'adresse
     */
    public Adresse getAdresse() {
        return adresse;
    }
    /**
     * Modificateur
     * @param a retourne l'adresse
     */
    public void setAdresse(Adresse a) {
        adresse=a;
    }

    /**
     * Renvoie true si p1 est plus agee que p2 sinon false
     * @param p1
     * @param p2
     * @return
     */
    public static boolean plusAgee(Personne p1, Personne p2){

        return p1.dateNaissance.compareTo(p2.dateNaissance) < 0;
    }

    /**
     * Renvoie true si l'instance de Personne est plus agee que p2 sinon false
     * @param p
     * @return
     */
    public boolean plusAgee(Personne p){

        return plusAgee(this, p);
    }

    /* (non-Javadoc)
     * @see java.lang.Object#toString()
     */
    public String toString(){
        String result="\nNom : "+nom+"\n"
                +"PrŽnom : "+prenom+"\n"+
                "NŽ(e) le : "+dateNaissance.get(Calendar.DAY_OF_MONTH)+
                "-"+dateNaissance.get(Calendar.MONTH)+
                "-"+dateNaissance.get(Calendar.YEAR)+"\n"+
                "Adresse : "+
                adresse.toString();
        return result;
    }

    public boolean equals(Personne p){
        return ((this.nom.equals(p.getNom())) && (this.prenom.equals(p.getPrenom())) && (this.dateNaissance.equals(p.getDateNaissance())));
    }
}
