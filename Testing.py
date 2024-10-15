import os
import xml.etree.ElementTree as ET

# Function to filter XML files based on <body>, <title>, and <correct> tags
def filter_xml(file_path):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Extract content only from <body> and <title> tags
        filtered_content = []
        for elem in root.iter():
            if elem.tag in ("body", "title"):
                filtered_content.append(ET.tostring(elem, encoding='unicode', method='xml'))

        # Join filtered content
        new_content = "".join(filtered_content)
        
        # Remove text inside <correct> tags
        # Parse the new content as XML and remove <correct> elements
        new_root = ET.fromstring(f"<root>{new_content}</root>")  # Wrap in a dummy root tag
        for correct in new_root.findall(".//correct"):
            correct.clear()  # Clear the content of <correct> tags
        
        # Write the filtered XML content back to file or process further
        filtered_xml = ET.tostring(new_root, encoding='unicode', method='xml')
        with open(file_path, 'w') as f:
            f.write(filtered_xml)
        print(f"Filtered and saved {file_path}")
        
    except ET.ParseError as e:
        print(f"Error parsing {file_path}: {e}")

# Directory traversal to apply the filter
def process_directory(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".xml"):
                file_path = os.path.join(foldername, filename)
                filter_xml(file_path)

# Replace 'root_folder' with the top-level directory containing your XML files
root_folder = 'C:/Users/LucasSilverioGums/Desktop/VSCode/AderenciaAoTopico/dataExtracted/data'
process_directory(root_folder)
