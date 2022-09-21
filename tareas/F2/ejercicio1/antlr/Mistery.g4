grammar Mistery;

prog:	(Aa)* ;

// Describe con palabras lo que acepta la regla Aa
//Aa es una variable que puede tener multiples iteraciones de ID(letra seguida de muchas letras o digitos) seguidos de un arreglo con un ID o un numero.
//acepta combinaciones de letras seguidas de numero y arreglos que poseen letras o numeros

Aa:	ID ('[' (ID | INTEGER) ']') +
    ;


ID: Letter LetterOrDigit*;
INTEGER : [0-9]+ ;

// fragment es para crear segmentos de token que solamente serán usados en este archivo, pero que no
// generan un token. Son como definiciones "locales" a este archivo.

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

fragment Letter : [a-zA-Z$_] ;