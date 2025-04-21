import xml.etree.ElementTree as ET

data_repo = '../../data_repo/'

tree = ET.parse(f'{data_repo}/data.xml')
root = tree.getroot()
print(root.tag)

for child in root:  # get the attributes of an element
    print('attrib:', child.attrib)  # print the attribute dictionary
print('---------------------')

for child in root:  # get the text of an element
    print(child.text)  # Print the text if it exists or an empty string
print('---------------------')

for child in root.findall('person'):  # find an element by tag name
    print(child.find('name').text)  # Find the name and print the value
print('---------------------')

for child in root.findall('person'):
    if int(child.find('age').text) > 30:
        print(child.find('name').text)

# Modify the XML file, add a new person
new_person = ET.Element('person')
person_details = ET.Element('name')
person_details.text = 'Anna'
new_person.append(person_details)
root.append(new_person)

# modify an element
for child in root.findall(".//*[name='John Smith']"):
    child.attrib = {'modified': 'Modified Person Text'}

# remove an element
for child in root.findall(".//*[name='Jane Doe']"):
    root.remove(child)

# write the modified XML data to a file
tree.write(f'{data_repo}/data_modified.xml')

# write the modified XML data to a string
xml_string = ET.tostring(root)
print(xml_string)
