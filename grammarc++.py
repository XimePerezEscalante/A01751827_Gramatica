import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

# Define a context-free grammar

grammar = CFG.fromstring("""
A -> C Pa P AP Pr K PT Pc Ke E

P -> Eu

Eu -> Elem OpC Et

Et -> Elem Em

Em -> Op Elem | 

Ex -> Elem Op Elem

Elem -> var | N

AP -> OpL Eu | 

PT -> var OpE Et

E -> 'else' Ep | 

Ep -> K PT Pc Ke

C -> 'if'

Op -> '+' | '-' | '/' | '%' | '*'

OpC -> '<' | '>' | '<=' | '>=' | '=='

OpE -> '=' | '+=' | '-='

OpL -> 'AND' | 'OR'

Pa -> '('

Pr -> ')'

K  -> '{'

Ke -> '}'

Pc -> ';'

N -> Np Npc

Np -> num

Npc -> num | 

var -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'

num -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

""")


# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentences to be parsed
sentences = [
    "if (a == b + 9) {a = b;}",
    "if (a < 1) {a = b * 5;}",
    "if (a < 7 AND a > 3) {a = a + 5;}",
    "if (i < j) {j += 7;} else {i += 5;}",
    "if (m > 9 OR n < 1) {a = b ;} else {c = d;}",
    "if (x < y) {a = b ;}",
    "if (i == j % 3) {k = k + 1;}",
    "if (x < 2 AND y > 1) {z = y;} else {y = z;}",
    "if (a == 4 5) {b = c;} else {d = e;}"

]

print("Bienvenid@! Te gustaría probar las oraciones predeterminadas o ingresar las tuyas?")
opcion = int(input("1. Predeterminadas\n2. Ingresar mi propia oración\n> "))

while opcion != 1 and opcion != 2:
  print("Selecciona una de las siguientes opciones")
  opcion = int(input("1. Predeterminadas\n2. Ingresar mi propia oración\n> "))

if opcion == 1:
  print("Las oraciones no validas no generan un arbol")
  for sentence in sentences:
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    parsedTokens = list(parser.parse(tokens))
    if parsedTokens:
      print("La oración: " + sentence + " es válida")
      for tree in parsedTokens:
        tree.pretty_print()
    else:
      print("La oración " + sentence + " NO es válida")
else:
  sentenceInput = input("Ingresa la oración:\n> ")
  tokens = nltk.word_tokenize(sentenceInput)
  # Parsear la oracion
  for tree in parser.parse(tokens):
    tree.pretty_print()
