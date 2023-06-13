console.log("Hello JS!")
let number1 = 123;
let text1 = "123";

// comparaison d'égalité
// renvoie true
console.log(text1 == number1);
console.log(number1 == text1);

//comparaison d'égalité
// renvoie false
console.log(text1 === number1);
console.log(number1 === text1);
// opérateur d'incrémentation
console.log(number1);

// number1 = number1 + 1
// number1 += 1
number1++;

// attention l'incrémentation se fait après l'affichage
console.log(number1++);

// solution : l'incrémentation se fait avant l'affichage
console.log(++number1);

// number1 = number1 - 1
// number1 -= 1
number1--;
console.log(number1);
console.log(--number1);

