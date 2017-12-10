# pyGoCompiler
## Compiladores - 2017
Compilador em Python3 de Go language para MIPS.
### Sobre o compilador
O compilador encontra-se preparado para um subset da liguagem <a href="https://golang.org/">Go</a> com as seguintes limitações:

* Qualquer programa só pode ter uma função defenida pelo utilizador que é a main e no cabeçalho deve defenir o Package e o import.

```Go
package main

import "fmt"

func main() {
  //Intruções
}
```
* Da biblioteca fmt podem ser utilizados a função *Scan* e *Print* para a interação com o utilizador.

* Os tipos definidos no trabalho são valores do tipo Inteiro, Float ou Booleano.

* Devido à ocorrência de problemas com o uso de floats em assembly MIPS, não nos foi possível implementar esta parte do trabalho na compilação do código assembly final para MIPS. 

* A declaração de varáveis só pode acontecer uma única vez.

* Às variavies só podem ser atribuidos valores numéricos.

* Todas as atribuições devem ser seguidas de um ";".

* A declaração de variáveis é efetuada da seguinte forma:
```Go
  i := 2;
```
* A atribuição de váriaveis pode ser feitas das seguinte formas:
```Go
  i = expr;
  i++;
  i--;
```
* Todos os restantes requerimentos para compilação correspondem aos da linguagem Go, da qual a documentação está referida anteriormente.

### Uso
Para perceber como utilizar o programa corretamente no terminal, pode usar a opção -h:
```txt
python3 pyGoCompiler -h
```
### Dependências
* ply
* argparse

As várias implementações foram testadas nas seguintes máquinas:
* Arch Linux, Python 3.6.3, GCC 7.2.0, PLY 3.10
* Ubuntu 16.04, Python 3.5.2, GCC 5.4.0, PLY 3.10
***
##### Trabalho realizado por:
###### [André Cirne](https://sigarra.up.pt/fcup/pt/fest_geral.cursos_list?pv_num_unico=201505860)
###### [José Rocha](https://sigarra.up.pt/fcup/pt/fest_geral.cursos_list?pv_num_unico=201503229)
