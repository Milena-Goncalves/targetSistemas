const readline = require('readline-sync');


function verificaFibonacci(num) {
    if (num === 0 || num === 1) return true;

    let a = 0;
    let b = 1;
    while (b < num) {
        let next = a + b;
        a = b;
        b = next;
    }
    return b === num;
}

let numero = readline.question('Digite um número para verificar se está na sequência de Fibonacci: ');
numero = parseInt(numero);

if (isNaN(numero)) {
    console.log('Por favor, digite um número válido.');
} else {
    if (verificaFibonacci(numero)) {
        console.log(`O número ${numero} pertence à sequência de Fibonacci.`);
    } else {
        console.log(`O número ${numero} não pertence à sequência de Fibonacci.`);
    }
}
