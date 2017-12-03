import settings
import file_helper
import dicttoxml
import json
import pprint

test_dict = {}
test_dict['Product'] = 'ADSL Partner Naked L'
test_dict['Contact'] = {}
test_dict['Contact']['PhoneNumber'] = '0902123456'
test_dict['Contact']['LastName'] = 'Andrejovic'
test_dict['Contact']['FirstName'] = 'Andrej'
test_dict['Address'] = None


def add_list_to_request(list_obj, req):
    for item in req:
        pprint.pprint(item['name'])
        if item['type'] == 'list':
            new_req = list_obj[item['name']]
            print str(new_req)
            add_list_to_request(new_req, item['value'])
            req.append(new_req)
            # return req
        if item['type'] == 'value':
            req[item['name']] = item['value']
    return req


def create_new_xml():
    template = settings.NEW_REQ_DEF
    # pprint.pprint(template)

    json_request = {}
    json_request = add_list_to_request(json_request, template)
    # pprint.pprint(json_request)


# obj = json.dumps(test_dict)
# xml = dicttoxml.dicttoxml(test_dict, custom_root='Request', attr_type=False , )

# print xml
create_new_xml()
