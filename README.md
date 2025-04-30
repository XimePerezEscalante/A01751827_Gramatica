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

A continuación, se presenta una gramática que representa la sintaxis básica del lenguaje:

```ebnf
A ::= if ( condicion ) { operacion ; } E

E ::= else A | else { operacion ; }

condicion ::= elem operador elem
            | operadorlog condicion
            | condicion

operacion ::= elem operadorarit
            | operacion
            | elem

operadorcomp ::= > | < | == | != | <= | >=

operadorlog ::= || | && | !

operadorarit ::= ++ | -- | += | -= | + | - | / | % | =

elem ::= var | num

var ::= a | b | c | d | e | f | g | h | i | j | k | l | m
      | n | o | p | q | r | s | t | u | v | w | x | y | z

num ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

## Eliminar recursión izquierda
- **condicion:** se llama a sí mismo.
- **operación:** se llama a sí mismo.
