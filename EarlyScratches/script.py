import xml.etree.ElementTree as ET
import os

found_xml = 'False'

def main():
    print(essayPromptConv(input("Enter repository to be compiled into a list of tuples <use '/'>: ")))
#C:/Users/lsg20/Downloads/dataPROJETO/data
def essayPromptConv(dir):
    l = []
    for pasta, subpasta, arquivos in os.walk(dir):
        for arquivo in arquivos:
            if arquivo == 'prompt.xml':
                path = os.path.join(pasta, arquivo)  # Full path to 'prompt.xml'
                tree = ET.parse(path)
                root = tree.getroot()
                title = root.find('title').text.strip()
                text = root.find('body').text.strip()
                
                #print(f"Title: {title}")
                #print(f"Text: {text}")
                l.append((title, text))
    #print(l)
    return l



#REGISTRY: IGNORE-------------------------------------------------------------------------------
    '''for pasta, subpasta, xml in os.walk(dir):
        for arquivo in os.walk(pasta):
            print(arquivo)
            if arquivo == 'prompt.xml':
                tree = ET.parse('prompt.xml')
                root = tree.getroot()
                title = root.find('title').text.strip()
                text = root.find('body').text.strip()

                print(text)'''
 

#redacoes('C:\\Users\\Bernardo\\Desktop\\data)

'''def redacoes2(dir):
    for pasta in os.walk(dir):
        print(pasta)

        if arquivo == 'prompt.xml':
            tree = ET.parse('prompt.xml')
            root = tree.getroot()
            title = root.find('title').text.strip()
            text = root.find('body').text.strip()'''

if __name__ == '__main__':
    main()