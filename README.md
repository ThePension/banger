# grp02_Banger_Abele-Aubert

# Banger

## Requirements

### Packages

- `matplotlib`
- `functools`
- `ply`
- `pydot`
- `os`

### External apps

- `Graphviz`

## Use

Afin de lancer (interpréter) votre programme (`my_prog.banger`) implémenté en Banger, il suffit de lancer la commande suivante :

```sh
python itInterpreter.py my_prog.banger
```

Les sorties seront alors affichées dans la console.

## Description

### Features

Les fonctionnalités de base de notre compilateur incluent :

- Déclaration de variables : Les utilisateurs peuvent déclarer des variables de
différents types (entiers, chaînes de caractères, etc.) et les initialiser avec des
valeurs.
- Affectation de variables : Les utilisateurs peuvent affecter des valeurs à des
- variables existantes.
- 
- Expressions arithmétiques : Notre compilateur prend en charge les opérations arithmétiques de base telles que l'addition, la soustraction, la multiplication et la division.
- Structures de contrôle : Notre compilateur prend en charge les structures de contrôle de base telles que les boucles (for, while) et les conditions (if).
- Fonctions : Les utilisateurs peuvent définir des fonctions avec des arguments et les appeler à différents endroits dans leur code.
- Impression : Les utilisateurs peuvent utiliser la fonction "print" pour afficher des valeurs et des chaînes de caractères dans la console.
- Commentaires : Notre compilateur prend en charge les commentaires dans le code source, qui sont ignorés lors de la compilation.


Le compilateur est capable de compiler des programmes simples utilisant des structures
de contrôle de base, des variables, des fonctions et des opérations arithmétiques.


# Code samples

Ces exemples de code montrent comment les fonctionnalités de base de notre compilateur peuvent être utilisées. Ces fichiers, ainsi que d'autres fichiers d'exemples, sont disponibles dans le dossier `./src/`.

<table>
<tr>
<th>Input</th>
<th>Ouput</th>
</tr>
<tr>
<td>

<pre>
function fibo(n) {
    n1 = 0
    n2 = 1
    nextTerm = 0

    for (i = 0; i < n; i = i + 1) {
        print(n1)
        nextTerm = n1 + n2
        n1 = n2
        n2 = nextTerm
    }
}

print("Fibonacci Series (10): ")

fibo(10)

print("End of Program")
</pre>

</td>
<td>

<pre>
Fibonacci Series (10):
0
1
1
2
3
5
8
13
21
34
End of Program
</pre>

</td>
</tr>


<tr>
<td>

<pre>
function multiply(a, b)
{
    print(a * b)
}

function multiplicationTable(a)
{
    for(b = 0; b <= 12; b = b + 1)
    {
        multiply(a, b)
    }
}

multiplicationTable(3)
</pre>

</td>
<td>

<pre>
0
3
6
9
12
15
18
21
24
27
30
33
36
</pre>

</td>
</tr>

<tr>
<td>

<pre>
my_variable = 5

while my_variable < 10 {
    print(my_variable)
    my_variable = my_variable + 1
}
</pre>

</td>
<td>

<pre>
5
6
7
8
9
</pre>

</td>
</tr>

<tr>
<td>

<pre>
my_variable = 3

if my_variable < 10 {
    print("my_variable is less than 10")
    if 0 == 0 {
        print("0 is equal to 0")
    }
}

if my_variable % 2 == 1 {
    print("my_variable is even")
}
</pre>

</td>
<td>

<pre>
my_variable is less than 10
0 is equal to 0
my_variable is even
</pre>

</td>
</tr>

</table>

