let num1;
let num2;
let total;

function entrada(){
     //armazena nas variáveis os valores de input
     num1 = Number(document.getElementById("n1").value);// a outra forma é colocar number(doc...);
     num2 = Number(document.getElementById("n2").value);
    //outra forma de transformar formato string em number
    //conversão
    // num1 = parseFloat(num1);
    // num2 = parseFloat(num2);
}

function result(){
    total = document.getElementById("resultado");
}

function somar(){
    entrada();
    // calcular e exibir na tela
    result();
    total.innerHTML = num1 + num2;
}

function subtrair(){
    entrada();
    // calcular e exibir na tela
    result();
    total.innerHTML = num1 - num2;
}

function multiplicar(){
    entrada();
    // calcular e exibir na tela
    result();
    total.innerHTML = num1 * num2;
}

function dividir(){
    entrada();
    // calcular e exibir na tela
    result();
    total.innerHTML = num1 / num2;
}

function limpar(){
    total = document.getElementById("resultado");
    total.innerHTML = " ";
    //Limpando os input
    document.getElementById("n1").value = " ";
    document.getElementById("n2").value = " ";
}
