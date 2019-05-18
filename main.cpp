#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "time.h"
 
const std::string termeSuivantConway(const std::string terme)
{
    std::string nouveauTerme;
    char c_actuel = terme[0];
    int c_compte = 0;
 
    for(int i = 0; i < terme.length(); ++i)
    {
        char c = terme[i];
 
        if(c != c_actuel)
        {
            nouveauTerme += (std::to_string(c_compte) + c_actuel);
            c_actuel = c;
            c_compte = 1;
        }
        else
        {
            c_compte += 1;
        }
    }
    nouveauTerme += (std::to_string(c_compte) + c_actuel);
 
    return nouveauTerme;
}
 
const std::string conway(const int n, const std::string premierTerme)
{
    std::string terme = premierTerme;
    std::string resultat[n];
 
    for(int i = 0; i < n; ++i)
    {
        resultat[i] = terme;
 
        terme = termeSuivantConway(terme);
 
        std::cout << i + 1 << "eme terme calcule !" << std::endl;
    }
 
    const std::string valeurs = resultat[(sizeof(resultat) / sizeof(std::string)) - 2] + "," + resultat[(sizeof(resultat) / sizeof(std::string)) - 1];
    return valeurs;
}
 
const float trouverLambda(const int n, const std::string premierTerme)
{
    time_t debut, fin;
    float duree;
    debut = time(NULL);
 
    std::string suite = conway(n, premierTerme);
 
    std::istringstream iss(suite);
    std::string terme;
    std::string LnString;
    std::string Ln1String;
 
    while(std::getline(iss, terme, ','))
    {
        if(LnString.length() == 0)
        {
            LnString = terme;
        }
        else
        {
            Ln1String = terme;
        }
    }
 
    float Ln = LnString.length();
    float Ln1 = Ln1String.length();
 
    float lambda = Ln1 / Ln;
 
    fin = time(NULL);
    duree = difftime(fin, debut);
 
    std::cout.precision(1000);
    std::cout << "Temps : " << duree << "s" << std::endl;
    std::cout << "Lambda : " << lambda << std::endl;
 
    return lambda;
}
 
int main()
{
    int n;
    std::string premierTerme = "1";
 
    std::cout << "Entrez le nombre de termes voulus : " << std::endl;
    std::cin >> n;
    std::cout << "Entrez le premier terme de la suite : " << std::endl;
    std::cin >> premierTerme;
    std::cout << std::endl;
 
    trouverLambda(n, premierTerme);
 
    return 0;
}