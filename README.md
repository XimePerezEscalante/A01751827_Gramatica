# A01751827_Gramatica
## Descripción
Una gramática es un sistema que define una serie de reglas para generar cadenas de texto válidas dentro de un lenguaje, ya que con ella se pueden construir oraciones sintácticamente correctas.
Tomando en cuenta esta definición, el objetivo de esta evidencia es presentar una gramática. Para ello, se comenzó con la selección de un lenguaje, en este caso se trata del lenguaje de programación C++, específicamente las sentencias if … else. A continuación se presenta la estructura de las mismas:
**Condiciones:** se comparan mínimo dos variables usando operadores de comparación y para agregar más, se usan operadores lógicos.
**Operaciones:** incluyen operaciones matemáticas que se llevan a cabo si se cumple la condición.
**Operadores de comparación:** >, <, >=, <=, ==, !=
**Operadores lógicos:** ||, &&, !
**Operadores aritméticos:** ++, --, +=, -=, +, -, /, //, %, =
**Variables:** a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
**Números:** 0,1,2,3,4,5,6,7,8,9
```
if (condición) {
operación
}
else {
operación
}
```

### Gramática que reconoce el lenguaje
A continuación se presenta una gramática que representa la sintaxis básica del lenguaje:
A ::= if ( condicion ) { operacion ;  } E
E ::= else A | else { operacion ; }
condicion ::= elem  operador elem  | operadorlog condicion | condicion
operacion ::=  elem  operadorarit | operacion |  elem
operadorcomp ::=  > | < | == | != | <= | >=
operadorlog ::=  || | && | !
operadorarit ::= ++ | -- | += | -= | + | - | / | // | % | =  
elem ::= var | num
var ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
num ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9



