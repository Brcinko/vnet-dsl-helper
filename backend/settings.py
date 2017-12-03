import datetime
PORT = 8080
DEBUG = True

PATH_TO_REQ = '/home/brcinko/projects/dsl-xml-generator/requests/'
ISP_CODE = 'VN'
AO_CODE = 21
YEAR = str(datetime.date.today().year)
scenario_type = {}

product_type = {

}

REQ_FILE_NAME = 'REQ_' + ISP_CODE + '_' + str(AO_CODE) + '_' + datetime.datetime.today().strftime('%Y%m%d') + '000000_'

NEW_REQ_DEF1 = {
    'Version': '1',
    'ISPcode': ISP_CODE,
    'AOcode': AO_CODE,
    'FileType': 'REQ',
    'FileChkSum': 1,
    'FileNum': 'get_file_num()'
}

NEW_REQ_DEF = [
    {
        'name': 'Version',
        'value': '1',
        'type': 'variable'
    },
    {
        'name': 'ISPcode',
        'value': ISP_CODE,
        'type': 'variable'
    },
    {
        'name': 'AOcode',
        'value': AO_CODE,
        'type': 'variable'
    },
    {
        'name': 'FileType',
        'value': 'REQ',
        'type': 'variable'
    },
    {
        'name': 'FileChkSum',
        'value': 1,
        'type': 'variable'
    },
    {
        'name': 'FileNum',
        'value': 'GET_NUM',
        'type': 'variable'
    },
    {
        'name': 'RequestBodyList',
        'type': 'list',
        'value': [
            {
                'name': 'RequestBody',
                'type': 'list',
                'value': [
                    {
                        'name': 'ScenarioID',
                        'value': 'M1.03',
                        'type': 'variable'
                    },
                    {
                        'name': 'RequestID',
                        'value': "REQ_ID",
                        'type': 'variable'
                    },
                    {
                        'name': 'ContactList',
                        'type': 'list',
                        'value': [
                            {
                                'name': 'Contact',
                                'type': 'list',
                                'value': [
                                    {
                                        'name': 'FirstName',
                                        'value': 'FIRST_NAME',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'LastName',
                                        'value': 'LAST_NAME',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'ContPhone',
                                        'value': 'CONT_PHONE',
                                        'type': 'variable'
                                    }
                                ]
                            }

                        ]
                    },
                    {
                        'name': 'AddressList',
                        'type': 'list',
                        'value': [
                            {
                                'name': 'Address',
                                'type': 'list',
                                'value': [
                                    {
                                        'name': 'StreetName',
                                        'value': 'STREET_NAME',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'AddressNum',
                                        'value': 'ADDRESS_NUM',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'ApartmentNum',
                                        'value': 'APARTMENT_NUM',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'BlockNum',
                                        'value': 'BLOCK_NUM',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'EvidencialNum',
                                        'value': 'EVIDENCIAL_NAME',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'Floor',
                                        'value': 'FLOOR',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'ZIPCode',
                                        'value': 'ZIP_CODE',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'City',
                                        'value': 'CITY',
                                        'type': 'variable'
                                    },
                                    {
                                        'name': 'Country',
                                        'value': 'COUNTRY',
                                        'type': 'variable'
                                    }
                                ]
                            }
                        ]
                    },

                ]
            }
        ]
    }
]