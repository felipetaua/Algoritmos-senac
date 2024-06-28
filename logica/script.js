//variáveis
let numero = 5; //tipo inteiro
let nome = "Alfredo"; //tipo string(texto)
let peso = 69.5; //tipo decimal
let sistemaAtivo = false; //tipo boleano (true ou false)(verdadeiro ou falso)

//impressões (formas de receber um feedback)
console.log("o nome é: " + nome);
alert("o nome é: " + nome);

/*----------------------------------------*/

//estruturas condicionais
/*tipos de comparação:
> maior
< menor
>= maior igual
<= menor igual
=== igualdade(estritamente igual até mesmo tipo)
!== diferente */
/* se número for maior que 10*/
if (numero > 10) {
  alert("Número maior que 10!");
} else {
  /*se não for maior que 10 */
  alert("Número menor que 10!");
}
/* se o if for falso e irá para o else*/

if (nome === "Alfredo") {
  console.log("O cliente Alfredo está com conta atrasada! ");
}

/* ---------------------------------------- */

let contador = 0;

//estrutura de repetição
//enquanto
while(contador < 5){
    console.log("O número é:" + contador);          /* estrutura de loop */
    contador = contador + 1;
}

// trabalhando com lista
let nomes = ['Julius','Marcos','Lucas','Felipe','Amanda','Daniel','Pedro','Maria','João','Luis'];

console.log("nome: "+ nomes[1]);

//nomes.lenght = tamanho da lista = 10

//inicio          condição de continuação   incrementador +1
for(contador = 0; contador<nomes.length; contador++){
  console.log("Imprimindo nomes: "+ nomes[contador]);// se for falso ele para a lista 
}

//objeto
var pessoa = {idade:10, nome: 'Nivaldo', altura:1.72};
  console.log(pessoa.nome);