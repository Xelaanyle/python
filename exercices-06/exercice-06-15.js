// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION : ne pas utiliser la fonction list.index()
// ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

// réponse 6.15

// my_list.length
// my_list[0].length

let index = null;
let valeur = "";
let longueur = 0;

// for (let i = 0; i < my_list.length; i++) {
//     // console.log(i);
//     // console.log(my_list[i]);
//     // console.log(my_list[i].length);
//     if (my_list[i].length > longueur) {
//         // mise à jour, c'est à dire stockage de la plus grande longueur rencontrée jusque maintenant
//         longueur = my_list[i].length;
//         // stockage des autres informations demandées
//         valeur = my_list[i]
//         index = i
//     };
// };

// console.log(index, valeur, longueur)

// boucle foreach qui permet de récupérer les valeurs mais pas l'index

// initialisation de l'index
let i = 0;

// reset des données (nécessaire parce qu'on a déjà le même algo en haut)

index = null;
valeur = "";
longueur = 0;

for (let word of my_list) {
    // a)
    // console.log(i, word, word.length);
    // b)
    if (word.length > longueur) {
        // mise à jour, c'est à dire stockage de la plus grande longueur rencontrée jusque maintenant
        longueur = word.length;
        // stockage des autres informations demandées
        valeur = word;
        index = i;
    }
    // c)
    // incrément de l'index
    i++;
}

console.log(index, valeur, longueur);