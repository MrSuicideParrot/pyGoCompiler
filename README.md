# pyGoCompiler
## Compiladores - 2017
Compilador em python3 de Go language para MIPS.
### Sobre o compilador
O compilador encontra-se preparado para um subset da liguagem <a href="https://golang.org/">Go</a>. Que é seguinte apresentado.

* Qualquer programa só pode ter uma função defenida pelo utilizador que é a main e no cabeçalho deve defenir o Package e o import.

```Go
package main

import "fmt"

func main() {
  //Intruções
}

```
* Da biblioteca fmt podem ser utilizados a função *Scan* e *Print* para a interação com o utilizador.

* Os tipos defenidos no trabalham foram Inteiros, Floats e valores Booleanos.

* Ás variavies só podem ser atribuidos valores numéricos.

* Todas as atribuições devem ser seguidas de um ";".

* As declaração de variavies é efetuada da seguinte forma:
```Go
  i := 2;
```
* A atribuição de váriaveis pode ser feitas das seguinte formas:
```Go
  i = 2;
  ++i;
  --i;
  i++;
  i--;
```

### Uso
### Dependências
* ply
* treelib
* argparse
