import xml.etree.ElementTree as ET

tree = ET.parse("ult4657u130.xml")
root = tree.getroot()

# Acessa a tag <body>
body = root.find('body')
title = root.find('title').text.strip()

texto = []

texto.append(body.text.strip())

for elem in body:
    if elem.tag == 'wrong':
        texto.append(' ' + elem.text.strip())
    if elem.tail:
        texto.append(elem.tail.strip())

final = ''.join(texto)

linhas = []

for linha in final.splitlines():
    linha.strip()
    linhas.append(linha.strip())

finalcerto = '\n\n'.join(linhas)



with open("redacao.txt",'w') as arquivo:
    arquivo.write(f'Título: {title}\n\n' + finalcerto)