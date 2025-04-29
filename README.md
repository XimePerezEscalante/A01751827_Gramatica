# A01751827_Gramatica
## Descripción
<br>
Una gramática es un sistema que define una serie de reglas para generar cadenas de texto válidas dentro de un lenguaje, ya que con ella se pueden construir oraciones sintácticamente correctas.
<br>
Tomando en cuenta esta definición, el objetivo de esta evidencia es presentar una gramática. Para ello, se comenzó con la selección de un lenguaje, en este caso se trata del lenguaje de programación C++, específicamente las sentencias if … else. A continuación se presenta la estructura de las mismas:
<br>
**Condiciones:** se comparan mínimo dos variables usando operadores de comparación y para agregar más, se usan operadores lógicos.
<br>
**Operaciones:** incluyen operaciones matemáticas que se llevan a cabo si se cumple la condición.
<br>
**Operadores de comparación:** >, <, >=, <=, ==, !=
  <br>
**Operadores lógicos:** ||, &&, !
  <br>
**Operadores aritméticos:** ++, --, +=, -=, +, -, /, //, %, =
  <br>
**Variables:** a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
  <br>
**Números:** 0,1,2,3,4,5,6,7,8,9
  <br>
```
if (condición) {
operación
}
else {
operación
}
```
<br>
### Gramática que reconoce el lenguaje
  <br>
A continuación se presenta una gramática que representa la sintaxis básica del lenguaje:
  <br>
A ::= if ( condicion ) { operacion ;  } E
  <br>
E ::= else A | else { operacion ; }
  <br>
condicion ::= elem  operador elem  | operadorlog condicion | condicion
  <br>
operacion ::=  elem  operadorarit | operacion |  elem
  <br>
operadorcomp ::=  > | < | == | != | <= | >=
  <br>
operadorlog ::=  || | && | !
  <br>
operadorarit ::= ++ | -- | += | -= | + | - | / | // | % | =  
  <br>
elem ::= var | num
  <br>
var ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
  <br>
num ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9



