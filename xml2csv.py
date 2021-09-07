# import xml.etree.ElementTree as ET
# import xmltodict
# import json
#
# tree = ET.parse(r"C:\Users\user\Downloads\drugbank_all_full_database.xml\full database.xml")
# xml_data = tree.getroot()
#
# xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')
#
#
# data_dict = dict(xmltodict.parse(xmlstr))
#
# print(data_dict)
#
# with open('new_data_2.json', 'w+') as json_file:
#     json.dump(data_dict, json_file, indent=4, sort_keys=True)

import xml.etree.ElementTree as ET
import xmltodict
import json


tree = ET.parse(r"C:\Users\user\Downloads\drugbank_all_full_database.xml\full database.xml")
xml_data = tree.getroot()
#here you can change the encoding type to be able to set it to the one you need
xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')

data_dict = dict(xmltodict.parse(xmlstr))
print(data_dict)