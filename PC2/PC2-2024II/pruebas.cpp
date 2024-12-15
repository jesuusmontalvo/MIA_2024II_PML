#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

string suma_numeros_hexadecimales(int n, string primer_numero, int m, string segundo_numero)
{
    unordered_map<char, int> tabla;
    const char* arreglo_primer_numero = primer_numero.c_str();
    const char* arreglo_segundo_numero = segundo_numero.c_str();
    int numero_equivalente = 10;

    for (char letra = 'A'; letra <= 'F'; ++letra){
        tabla[letra] = numero_equivalente;
        ++numero_equivalente;
    }

    for (int i = n - 1; i>= 0; --i){

    }
}
int main()
{   
    string primer_numero;
    string segundo_numero;
    int n;
    int m;
    
    cout << "Ingrese el primer numero haxademcimal:\n";
    cin >> primer_numero;
    n = primer_numero.size();
    cout << "Ingrese el segundo numero hexadecimal:\n";
    cin >> segundo_numero;
    m = segundo_numero.size();
    if (n - m > 0){
        suma_numeros_hexadecimales(n, primer_numero, m, segundo_numero);
    }else{
        suma_numeros_hexadecimales(m, segundo_numero, n, primer_numero);   
    }
}