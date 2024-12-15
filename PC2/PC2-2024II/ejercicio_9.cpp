#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <map>

using namespace std;

vector<int> encontrarPG(vector<int> &X, int &razon)
{
    vector<int> maxPG;
    int n = X.size();

    unordered_set<int> X_set(X.begin(), X.end());

    for (int i = 0; i < n; i++)
    {

        for (int j = i + 1; j < n; j++)
        {
            if (X[i] == 0 || X[j] == 0)
                continue;
            if (X[j] % X[i] != 0)
                continue;
            int r = X[j] / X[i];
            if (r > 1)
            {
                vector<int> PG;

                PG.push_back(X[i]);
                PG.push_back(X[j]);

                int last = X[j];
                while (true)
                {
                    int nextTerm = last * r;
                    cout << " nextTerm: " << last;
                    if (X_set.find(nextTerm) != X_set.end())
                    {
                        PG.push_back(nextTerm);
                        last = nextTerm;
                    }
                    else
                    {
                        break;
                    }
                }

                if (PG.size() > maxPG.size() || (PG.size() == maxPG.size() && r > razon))
                {
                    maxPG = PG;
                    razon = r;
                }
            }
        }
    }

    return maxPG;
}

vector<int> encontrarPA(vector<int> &X, int &diferencia)
{
    vector<int> maxPA;
    int n = X.size();
    cout << " n: " << n;
    unordered_set<int> X_set(X.begin(), X.end());

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            int d = X[j] - X[i];
            if (d > 0)
            {
                vector<int> PA;
                PA.push_back(X[i]);
                PA.push_back(X[j]);

                int last = X[j];
                while (true)
                {
                    int nextTerm = last + d;
                    if (X_set.find(nextTerm) != X_set.end())
                    {
                        PA.push_back(nextTerm);
                        last = nextTerm;
                    }
                    else
                    {
                        break;
                    }
                }

                if (PA.size() > maxPA.size() || (PA.size() == maxPA.size() && d > diferencia))
                {
                    maxPA = PA;
                    diferencia = d;
                }
            }
            else
            {
                maxPA = X;
            }
        }
    }
    if (n == 1)
    {
        maxPA = X;
    }
    return maxPA;
}

void imprimirProgresiones(vector<int> &X, int &n)
{
    cout << "Ingrese los " << n << " elementos del arreglo X:" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> X[i];
    }
    sort(X.begin(), X.end());
    int diferencia = 0;
    int razon = 0;

    vector<int> PG = encontrarPG(X, razon);

    unordered_set<int> usadosPG(PG.begin(), PG.end());
    map<int, int> conteo;

    for (int num : X)
    {
        conteo[num]++;
    }

    vector<int> noUsados;

    for (int num : X)
    {

        if ((usadosPG.find(num) == usadosPG.end() || conteo[num] > 1) )
        {
            noUsados.push_back(num);
            conteo[num]--;
        }
    }

    vector<int> PA = encontrarPA(noUsados, diferencia);

    cout << "Progresion Aritmetica (diferencia " << diferencia << "): ";
    for (int num : PA)
    {
        cout << num << " ";
    }
    cout << endl;

    cout << "Progresion Geometrica (razon " << razon << "): ";
    for (int num : PG)
    {
        cout << num << " ";
    }
    cout << endl;
}

int main()
{
    int n;

    cout << "Ingrese la cantidad de elementos en el arreglo: ";
    cin >> n;

    vector<int> X(n);
    imprimirProgresiones(X, n);

    return 0;
}
