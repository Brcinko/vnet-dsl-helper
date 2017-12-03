import settings
import file_helper
import dicttoxml
import json


test_dict = {}
test_dict['Product'] = 'ADSL Partner Naked L'
test_dict['Contact'] = {}
test_dict['Contact']['PhoneNumber'] = '0902123456'
test_dict['Contact']['LastName'] = 'Andrejovic'
test_dict['Contact']['FirstName'] = 'Andrej'
test_dict['Address'] = None

# obj = json.dumps(test_dict)
xml = dicttoxml.dicttoxml(test_dict, custom_root='Request', attr_type=False , )

print xml