from xml.etree import ElementTree as ET


# with open('201913421.xml', 'rt') as f:
#     tree = ET.parse(f)
#     tre = ET.Element(f)
#     tr = ET.TreeBuilder(f)
#     root = tree.getroot()
#
#
# print(tree)
# print(f'{root.tag},{root.attrib}  :  {root}')
#
# for child in root:
#     print(child.tag, child.attrib)




# with open('201913421.xml', 'rt') as f:
#     tree = ElementTree.parse(f)
#
# for node in tree.iter():
#     print(node.tag)
#
# # for node in tree.getroot():
# #     print(node.tag)
#
# for path in [ './OrderId', './OrderYear ']:
#     node = tree.find(path)
#     print(f' order: {node}')
#     print(' Year:', node)




boom = ET.parse('201913421.xml')
wortel = boom.getroot()

print(wortel.tag, wortel.attrib)

# for child in wortel.iter():
#     print(child.tag, child.attrib)

a=[elem.tag for elem in wortel.iter()]
# print(a)

# print(ET.tostring(wortel, encoding='utf8').decode('utf8'))
lijst=['OrderId', 'SubOrderId', 'OrderYear', 'Name', 'Description', 'DueDate']

for omschrijving in wortel.iter('Size'):
    print(omschrijving.text)

for uitkomst in wortel.findall("./Job/"):
    print(uitkomst.text)

for paramtr in wortel.findall("./Parameter/"):
    print(paramtr.tag, paramtr.text)




