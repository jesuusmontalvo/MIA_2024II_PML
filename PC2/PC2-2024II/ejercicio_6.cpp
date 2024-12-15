#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

string suma_numeros_hexadecimales(int n, string primer_numero_hexadecimal, int m, string segundo_numero_hexadecimal)
{
    unordered_map<int, int> tabla;
    unordered_map<int, char> caracteres;
    const char* arreglo_primer_numero = primer_numero_hexadecimal.c_str();
    const char* arreglo_segundo_numero = segundo_numero_hexadecimal.c_str();
    int numero_equivalente_letras = 10;
    int numero_equivalente_ascii = 0;
    int primer_numero;
    int segundo_numero;
    int acarreo = 0;
    int residuo;
    string output;
    for (int codigo_ascii=48; codigo_ascii<=57; ++codigo_ascii){
        tabla[codigo_ascii] = numero_equivalente_ascii;
        caracteres[numero_equivalente_ascii] = static_cast<char>(codigo_ascii);
        ++numero_equivalente_ascii;
    }
    for (char letra = 'A'; letra <= 'F'; ++letra){
        tabla[static_cast<int>(letra)] = numero_equivalente_letras;
        caracteres[numero_equivalente_letras] = letra;
        ++numero_equivalente_letras;
    }
    for (int i=0; i<n; ++i){
        primer_numero = tabla[static_cast<int>(arreglo_primer_numero[n-1-i])];
        segundo_numero = 0;
        if (i<m){
            segundo_numero = tabla[static_cast<int>(arreglo_segundo_numero[m-i-1])];
        }
        residuo = (primer_numero + segundo_numero + acarreo) % 16;
        acarreo = (primer_numero + segundo_numero + acarreo) / 16;
        output = caracteres[residuo] + output;
    }
    if(acarreo !=0){
        output = caracteres[acarreo] + output;
    }
    return output;
}
int main()
{   
    string primer_numero_hexadecimal;
    string segundo_numero_hexadecimal;
    int n;
    int m;
    cout << "Ingrese el primer numero haxademcimal:\n";
    cin >> primer_numero_hexadecimal;
    n = primer_numero_hexadecimal.size();
    cout << "Ingrese el segundo numero hexadecimal:\n";
    cin >> segundo_numero_hexadecimal;
    m = segundo_numero_hexadecimal.size();
    if (n - m > 0){
        cout << suma_numeros_hexadecimales(n, primer_numero_hexadecimal, m, segundo_numero_hexadecimal);
    }else{
        cout << suma_numeros_hexadecimales(m, segundo_numero_hexadecimal, n, primer_numero_hexadecimal);   
    }
}