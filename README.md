# A01751827_Gramatica
## Descripción

Una **gramática** es un sistema que define una serie de reglas para generar cadenas de texto válidas dentro de un lenguaje. Gracias a ella, se pueden construir oraciones sintácticamente correctas.

Tomando en cuenta esta definición, el objetivo de esta evidencia es **presentar una gramática**. Para ello, se comenzó con la selección de un lenguaje: en este caso, el lenguaje de programación **C++**, específicamente las sentencias `if ... else`.

### Estructura de las sentencias `if ... else`

- **Condiciones**: Se comparan al menos dos variables usando operadores de comparación. Para agregar más condiciones, se emplean operadores lógicos.
- **Operaciones**: Incluyen operaciones matemáticas que se ejecutan si se cumple la condición.

### Elementos

- **Operadores de comparación**: `>`, `<`, `>=`, `<=`, `==`, `!=`
- **Operadores lógicos**: `||`, `&&`, `!`
- **Operadores aritméticos**: `++`, `--`, `+=`, `-=`, `+`, `-`, `/`, `%`, `=`
- **Variables**: `a`–`z`
- **Números**: `0`–`9`

### Ejemplo de estructura general

```cpp
if (condición) {
  operación;
} else {
  operación;
}
```

---

## Gramática que reconoce el lenguaje

A continuación, se presenta una gramática que representa la sintaxis básica del lenguaje utilizando la notación Extended Backus-Naur Form  (EBNF):

```ebnf
A ::= AL

AL ::= Cond '(' P AP ')' '{' PT ';''}' E

P ::= P Op P | var | num

AP ::=  OpL P | ε

PT ::= var OpE P

E ::= ‘else’ '{' PT ';''}' | ‘else’ AL | ε

Cond ::= ‘if‘

Op ::= ‘+’ | ‘-’ | ‘+=’ | ‘-=’ | ‘/’ | ‘%’ | '*' | '>' | '<' | '>=' | '<='

OpE ::= ‘=’

OpL ::= ‘&&’ | ‘||’

var ::= ‘a’ | ‘b’ | ‘c’ | ‘d’ | ‘e’ | ‘f’ | ‘g’ | ‘h’ | ‘i’ | ‘j’ | ‘k’ | ‘l’ | ‘m’ | ‘n’ | ‘o’ | ‘p’ | ‘q’ | ‘r’ | ‘s’ | ‘t’ | ‘u’ | ‘v’ | ‘w’ | ‘x’ | ‘y’ | ‘z’

num ::= ‘0’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’ | ‘8’ | ‘9’ | num num
```

Epsilon: cadena vacía.

Todo lo que está entre comillas simples son los elementos terminales.

### Oraciones que se pueden construir


Con esta gramática se pueden generar sentencias tan simples como:

`if (x == 2) {x = x * 2;}`

Al igual que cosas con más variables como:

`if (b < c) {c++;} else {b++;}`

Hasta ifs anidados:

```
if (a > 0 && a < 5) {
  if (a % 2 == 0) {
    a = a * 2;
  }
  else if (a != 1) {
    a = a * 3;
  }
  else {
    a--;
  }
}
```

**¡Pero hay un problema!**

Esta gramática tiene ambigüedad y recursividad izquierda, pero necesitamos revisar nuestra gramática con un parser de tipo **LL1**.

### Parser LL(1)

Un parser realiza un análisis de sintáxis del input que reciba, con el objetivo de crear un Árbol de Sintáxis Abstracta, 
o en inglés Abstract Syntax Tree, donde se representa de manera jerárquica la estructura gramatical del código original.

El parser LL1 o Left left look ahead 1 únicamente sabe qué hay en el siguiente elemento (por eso el 1) y no usa backtracking, por lo que es determinístico. Y actualmente la gramática **no es determinística**. Es por ello que debemos:

1. Eliminar ambigüedad.
2. Eliminar recursividad izquierda.


## Eliminar ambigüedad

Para saber si una gramática es ambigüa, debemos revisar si se puede generar más de un AST para X sentencia, lo cual sí es posible 
actualmente y para demostrarlo pondré un ejemplo sencillo:

`if (a < 5) {a = a + b + c + 1;} else {a = 5;}`

A continuación muestro sólo 2 posibles ASTs para esta oración:

**AST 1**
![AST 1](https://github.com/XimePerezEscalante/A01751827_Gramatica/blob/main/AST1.png?raw=true)

**AST 2**
![AST 2](https://github.com/XimePerezEscalante/A01751827_Gramatica/blob/main/AST2.png?raw=true)

### ¿Dónde está localizada?

Se encuentra en:

`P ::= P Op P | P OpS | var | num`

Ya que puede usarse P en dos lados distintos y como se llama a sí mismo, se generan ramas de ambos lados.

**¿Cómo eliminarla?**

Debemos agregar estados intermedios para eliminar los que son equivalentes y que generan las ramas desde múltiples lados, lo que genera una precedencia.
Así que en lugar de únicamente usar P, se agrega el No terminal: **Elem** para que P ya no pueda ser var y num. 

Gramática actualizada:

```ebnf
A ::= AL

AL ::= Cond '(' P AP ')' '{' PT ';''}' E

P ::= Elem Op Elem

Elem ::= var | num

AP ::=  OpL P | ε

PT ::= var OpE P

E ::= ‘else’ '{' PT ';''}' | ‘else’ AL | ε

Cond ::= ‘if‘

Op ::= ‘+’ | ‘-’ | ‘+=’ | ‘-=’ | ‘/’ | ‘%’ | '*' | '>' | '<' | '>=' | '<='

OpE ::= ‘=’

OpS ::= ‘++’ | ‘--’

OpL ::= ‘&&’ | ‘||’

var ::= ‘a’ | ‘b’ | ‘c’ | ‘d’ | ‘e’ | ‘f’ | ‘g’ | ‘h’ | ‘i’ | ‘j’ | ‘k’ | ‘l’ | ‘m’ | ‘n’ | ‘o’ | ‘p’ | ‘q’ | ‘r’ | ‘s’ | ‘t’ | ‘u’ | ‘v’ | ‘w’ | ‘x’ | ‘y’ | ‘z’

num ::= ‘0’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’ | ‘8’ | ‘9’ | num num
```

## Eliminar recursión izquierda

La recursión izquierda puede identificarse cuando hay un No terminal que se manda llamar a sí mismo, lo que provoca problemas con el parser LL(1) ya que
se pierde en el camino, al ir leyendo de izquierda a derecha, no le es posible saber el camino para llegar.

**¿Dónde está localizada?**

`num ::= ‘0’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’ | ‘8’ | ‘9’ | num num`

Es visible que num se puede llamar a sí mismo 2 veces, en caso de que haya un número de dos dígitos.

**¿Cómo eliminarla?**

Se deben agregar dos estados: uno que sirve como intermedio y otro como terminal. En este caso son **N** y **NL**, el terminal continuará siendo _num_.

```ebnf
A ::= AL

AL ::= Cond '(' P AP ')' '{' PT ';''}' E

P ::= Elem Op Elem 

Elem ::= var | num

AP ::=  OpL P | ε

PT ::= var OpE P

E ::= ‘else’ '{' PT ';''}' | ‘else’ AL | ε

Cond ::= ‘if‘

Op ::= ‘+’ | ‘-’ | ‘+=’ | ‘-=’ | ‘/’ | ‘%’ | '*' | '>' | '<' | '>=' | '<='

OpE ::= ‘=’

OpS ::= ‘++’ | ‘--’

OpL ::= ‘&&’ | ‘||’

var ::= ‘a’ | ‘b’ | ‘c’ | ‘d’ | ‘e’ | ‘f’ | ‘g’ | ‘h’ | ‘i’ | ‘j’ | ‘k’ | ‘l’ | ‘m’ | ‘n’ | ‘o’ | ‘p’ | ‘q’ | ‘r’ | ‘s’ | ‘t’ | ‘u’ | ‘v’ | ‘w’ | ‘x’ | ‘y’ | ‘z’

N ::= NL NL

NL ::= num

num ::= ‘0’ | ‘1’ | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’ | ‘8’ | ‘9’ 
```

## Ejemplos


## Implementación


## Complejidad de la gramática


### Antes de eliminar ambigüedad y recursividad izquierda


### Después de eliminar ambigüedad y recursividad izquierda

