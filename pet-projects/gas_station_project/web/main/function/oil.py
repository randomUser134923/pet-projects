from urllib.request import Request, urlopen , urlretrieve

import xmltodict
from datetime import datetime
import xml.etree.ElementTree as ET

def save_oil_data():
    url = 'http://www.opinet.co.kr/api/detailById.do?code=F980210414&id=A0033122&out=xml' 
    filepath = '/home/ec2-user/environment/pet-projects/gas_station_project/web/main/data/'
    filename = get_now()+'.xml'
    urlretrieve(url,filepath+filename)
    urlretrieve(url,filepath+'latest.xml')

def opinet_xml_crawl():
    url = 'http://www.opinet.co.kr/api/detailById.do?code=F980210414&id=A0033122&out=xml'
    file = urlopen(url)

    data = file.read()
    file.close()
    return data

def local_xml():
    result = {}
    xmlPath = "/home/ec2-user/environment/pet-projects/gas_station_project/web/main/data/latest.xml"
    tree = ET.parse(xmlPath)
    root = tree.getroot()
    oils = root.find('OIL').findall('OIL_PRICE')
    for oil in oils:
        result[oil.find('PRODCD').text] = oil.find('PRICE').text
        update = oil.find('TRADE_DT').text
    result['yyyy'] = update[0:4]
    result['mm'] = update[4:6]
    result['dd'] = update[6:8]
    return result

def get_now():
    return datetime.now().strftime('%Y-%m-%d')
    

def test():
    temp = "20200304"
    print(temp[0:4] , temp[4:6] , temp[6:8])
    
save_oil_data()
local_xml()