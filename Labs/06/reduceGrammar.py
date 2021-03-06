#!/usr/bin/env python
#Testing Grammar For Calculator - Adler Zamora A01630908
grammarText = "S -> F | I | ID, F -> floatdcl id,I -> intdcl id,ID -> id ASSIGN, ASSIGN -> assign VALUE| assign VALUE OPERATION VALUE,VALUE-> fnum | inum | id, OPERATION -> plus | minus | times | divided by"

grammar = {}

productions = grammarText.split(",")  # Separates productions

for production in productions:  # Separates the left side of the produccion as as key and the rightside as the products
    key = production.split("->")[0].strip()
    products = production.split("->")[1]
    grammar[key] = []
    for product in products.split("|"):
        grammar[key].append(product)

#print(grammar)

actual = "S"
queue = [actual]

cantDerive = []
visited = {}
cantDerive = []

while len(queue) != 0:
    actual = queue.pop()
    productions = grammar[actual] 
    if not actual in visited:
        for production in productions:
            for char in production.split():
                if char in grammar:
                    queue.append(char)
                    if char == actual:
                        cantDerive.append(actual)
        visited[actual] = True

notVisited = []

for key in grammar:
    if not key in visited:
        notVisited.append(key)

print("Nonterminals that cannot be reached from a CFG's goal symbol")
print(str(notVisited))

print("Nonterminals that cannot derive any terminal stringin a CFG")
print(str(cantDerive))