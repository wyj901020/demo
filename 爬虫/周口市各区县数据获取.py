import requests
import pandas as pd
import json
import xlwt
import time


session = requests.Session()
first_url = 'https://hepp.zc12369.com/api/pollute_map/air_quality_city?time='
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'hepp.zc12369.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
}

time_range = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start='2020-10-27', end='2020-11-01'))]
book = xlwt.Workbook()
sheet = book.add_sheet('周口市各区县数据')
n = 1
sheet.write(0,0,'ID')
sheet.write(0,1,'时间')
sheet.write(0,2,'PM10')
sheet.write(0,3,'PM2.5')

for i in time_range:
    for j in range(0,24):
        time.sleep(5)
        url = first_url+str(i)+'+'+str(j)+ '%3A00'
        response = session.get(url,headers = headers).text
        data = json.loads(response)
        res = data['data']
        for k in res:
            if k['id'] in ['411626','411628','411627','411681','411624','411622','411621','411625','411602','411623',]:
                sheet.write(n, 0, k['areaAllName'])
                sheet.write(n, 1, k['updateTime'])
                sheet.write(n, 2, k['pm10'])
                sheet.write(n, 3, k['pm25'])
                n+=1
                print(k)
        # print(res)

book.save('hourdata11月1日.xls')