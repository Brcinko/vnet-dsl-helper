import datetime

PATH_TO_REQ = '/home/brcinko/projects/dsl-xml-generator/requests/'
ISP_CODE = 'VN'
AO_CODE = 21
YEAR = str(datetime.date.today().year)
scenario_type = {}

product_type = {

}

REQ_FILE_NAME = 'REQ_' + ISP_CODE + '_' + str(AO_CODE) + '_' + datetime.datetime.today().strftime('%Y%m%d') + '000000_'