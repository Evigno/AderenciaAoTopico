import xml.etree.ElementTree as ET
import os

def main():
    print(process_essays('C:/Users/lsg20/Downloads/dataPROJETO/data')) #C:/Users/lsg20/Downloads/dataPROJETO - Copy/data
    

'''def write_values(lst):
    with open("test.csv","w") as fd:
        for (essay, prompt, score) in lst:
            fd.write(f"{essay},{prompt},{score}\n")'''

def essayPromptConv(prompt_path):
    # Process the prompt.xml file and return relevant data
    try:
        tree = ET.parse(prompt_path)
        root = tree.getroot()
        
        title = root.find('title').text.strip() if root.find('title') is not None else ''
        text = root.find('body').text.strip() if root.find('body') is not None else ''
        
        return (title + " " + text)
    except ET.ParseError as e:
        print(f"Error parsing {prompt_path}: {e}")
        return ('', '')

def process_essays(dir_path):
    essays_list = []

    # Walk through each file in the directory
    for folder, subfolder, files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith('.xml') and file_name != 'prompt.xml':  # Process only essay XML files
                file_path = os.path.join(folder, file_name)

                # Determine grandparent folder and locate prompt.xml
                grandparent_folder = os.path.dirname(folder)
                prompt_path = os.path.join(grandparent_folder, 'prompt.xml')
                prompt_data = essayPromptConv(prompt_path) if os.path.exists(prompt_path) else ('', '')

                # Parse the essay XML file
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()

                    # Extract <title> with a safeguard
                    title_element = root.find('title')
                    title = title_element.text.strip() if title_element is not None and title_element.text else ''
                    
                    # Extract the second <grade> from within <skills>
                    score = ''
                    skills = root.find('skills')
                    if skills is not None:
                        # Gather all <grade> tags in order
                        grades = [skill.find('grade').text.strip() for skill in skills if skill.find('grade') is not None]
                        if len(grades) >= 2:  # Check if there is a second <grade> element
                            score = grades[1]
                    
                    # Extract <body> and initialize content
                    body = root.find('body')
                    text_content = []
                    
                    if body is not None:
                        # Initial body text outside of any tags
                        if body.text:
                            text_content.append(body.text.strip())
                        
                        # Process each child element within <body>
                        for elem in body:
                            if elem.tag == 'wrong' and elem.text:
                                text_content.append(' ' + elem.text.strip())
                            if elem.tail:
                                text_content.append(elem.tail.strip())
                        
                        # Join and format body text
                        body_text = ''.join(text_content)
                        formatted_body = '\n'.join(line.strip() for line in body_text.split('. ') if line)
                        
                        # Append title, formatted body, and prompt data to the essays list
                        essays_list.append((title + " " + formatted_body, prompt_data, score))
                except ET.ParseError as e:
                    print(f"Error parsing {file_name}: {e}")
    
    with open("test.csv", "w") as fd:
            for (essay, prompt, score) in essays_list:
                fd.write(f"{essay},{prompt},{score}\n")

    return essays_list


'''def process_essays(dir_path):
    essays_list = []

    # Walk through each file in the directory
    for folder, _, files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith('.xml'):  # Only process XML files
                file_path = os.path.join(folder, file_name)

                # Parse XML file
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    
                    # Extract <title> with a safeguard
                    title_element = root.find('title')
                    title = title_element.text.strip() if title_element is not None and title_element.text else ''
                    
                    # Extract <body> and initialize content
                    body = root.find('body')
                    text_content = []
                    
                    if body is not None:
                        # Initial body text outside of any tags
                        if body.text:
                            text_content.append(body.text.strip())
                        
                        # Process each child element within <body>
                        for elem in body:
                            if elem.tag == 'wrong' and elem.text:
                                text_content.append(' ' + elem.text.strip())
                            if elem.tail:
                                text_content.append(elem.tail.strip())
                        
                        # Join and format body text
                        body_text = ''.join(text_content)
                        formatted_body = '\n'.join(line.strip() for line in body_text.split('. ') if line)
                        
                        # Append formatted content to the essays list
                        essays_list.append((title, formatted_body, file_name))
                except ET.ParseError as e:
                    print(f"Error parsing {file_name}: {e}")
                    
    return essays_list

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
    return l'''

if __name__ == '__main__':
    main()









'''tree = ET.parse("ult4657u130.xml")
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
    arquivo.write(f'Título: {title}\n\n' + finalcerto)'''