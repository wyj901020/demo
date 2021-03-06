import requests
import pandas as pd
import json
import xlwt
import time


session = requests.Session()
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
first_url_month = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county'
first_url_year = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county '
url_list = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/getCityStationDetail'
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}

def year(url):
    data = {
        'end':'2020-10-31',
        'sort':'asc',
        'start':'2020-01-01'
    }
    response = session.post(url= url,data=data,headers = headers).text
    print(response)
    return response

def month(url):
    data = {
        'sort':'asc',
        'month':'2019-01'
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response

def day(url):
    data = {
        'sort':'asc',
        'time':'2020-09-27'
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response


def real(url):
    response = session.get(url= url_list,headers = headers).text
    return response
    data = json.loads(l)['detail']
    for i in data:
        print(i)


# print(real(url_list))




l = year(first_url_year)
data = json.loads(l)['data']
book = xlwt.Workbook()
sheet = book.add_sheet('周口市各区县数据')
n = 1
sheet.write(0,0,'区县')
sheet.write(0,1,'CO')
sheet.write(0,2,'O3')
sheet.write(0,3,'SO2')
sheet.write(0,4,'NO2')
sheet.write(0,5,'PM10')
sheet.write(0,6,'PM2.5')
sheet.write(0,7,'综合指数')
for k in data:
    if k['city'] in ['南召县','方城县','西峡县','镇平县','内乡县','淅川县','社旗县','唐河县','新野县','桐柏县','邓州市']:
        sheet.write(n, 0, k['city'])
        sheet.write(n, 1, k['co'])
        sheet.write(n, 2, k['o3'])
        sheet.write(n, 3, k['so2'])
        sheet.write(n, 4, k['no2'])
        sheet.write(n, 5, k['pm10'])
        sheet.write(n, 6, k['pm25'])
        sheet.write(n, 7, k['zong'])
        n+=1

book.save('周报邓州市12020年1-10月累计.xls')

print(data)

