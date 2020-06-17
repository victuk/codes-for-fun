function factorial(n){
    if (n <= 1){return 1;}
    return n * factorial(n - 1)
}

function fac(n){
    if (n <= 1){return 1;}
    return n + " X " + fac(n - 1)
}

console.log("5 factorial (!5 or " + fac(5) + ") = " + factorial(5));


