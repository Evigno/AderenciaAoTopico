import xml.etree.ElementTree as ET
import os

'''found_xml = 'False'

def redacoes(dir):
    for pasta,subpasta,xml in os.walk(dir):
        for arquivo in os.walk(pasta):
            print(arquivo)
            ''''''if arquivo == 'prompt.xml':
                tree = ET.parse('prompt.xml')
                root = tree.getroot()
                title = root.find('title').text.strip()
                text = root.find('body').text.strip()

                print(text)''''''
 

redacoes('C:\\Users\\Bernardo\\Desktop\\data')'''

def redacoes(dir):
    for pasta in os.walk(dir):
        print(pasta)

'''if arquivo == 'prompt.xml':
                tree = ET.parse('prompt.xml')
                root = tree.getroot()
                title = root.find('title').text.strip()
                text = root.find('body').text.strip()'''

redacoes('C:\\Users\\Bernardo\\Desktop\\data')