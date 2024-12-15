#include <iostream>
#include <string>
#include <vector>
using namespace std;


void cantidad_de_vocales_diferentes_en_palabra(string palabra)
{
    vector<char> vocales {'a', 'e', 'i', 'o', 'u'};
    vector<string> nuevas_palabras;

    for (auto& vocal: vocales)
        if(palabra.find(vocal)){
            int posicion_de_vocal = palabra.find(vocal);
            palabra.erase(posicion_de_vocal, 1);
            nuevas_palabras.push_back(palabra);
            cout << palabra;
        }
}
int main()
{
    cantidad_de_vocales_diferentes_en_palabra("Hola");
}