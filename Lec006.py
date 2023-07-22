# .py "裁示"正式版本
# 現在的版本還有BUG，因為如果沒下載成功 ( not == 200 ) 就會報錯
 
import requests
import csv


# urlNewTaipei = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-010?Authorization=rdec-key-123-45678-011121314&format=JSON'
url ='https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-007?Authorization=rdec-key-123-45678-011121314&format=JSON'
responseR = requests.get(url)
if responseR.status_code == 200:
    print("下載成功")
    weather = responseR.json()


wLocation = weather['cwbopendata']['dataset']['location']
for listLocation in wLocation:
    cityN = listLocation['locationName']
    print(cityN)


wLocation = weather['cwbopendata']['dataset']['location']
weather_list = [] # 建立一個空的list
for item in wLocation:
    city_item = {} # 在list裡面建立一個空的dictionary
    city_item['CityName'] = item['locationName'] # 建立dictionary裡面的 keys
    city_item['StartTime'] = item['weatherElement'][1]['time'][0]['startTime']
    city_item['HighTemp'] = item['weatherElement'][1]['time'][0]['elementValue']['value']
    #city_item['低溫'] = item['weatherElement'][1]['time'][0]['startTime']['elementValue']
    #city_item['End'] = item['weatherElement'][1]['time'][0]['endTime']
    #city_item['高溫'] = item['weatherElement'][2]['time'][0]['elementValue']
    weather_list.append(city_item) # 加入原本的空list裡面
weather_list # 看一下加了甚麼


import csv
with open('溫度TmaxDownloadOnlinePY.csv', 'w', encoding='utf-8', newline='') as saveCityT:
    TITLE = ['CITY','TIME','TEMP']
    title = ['CityName','StartTime','HighTemp']
    dataWrite = csv.DictWriter(saveCityT,fieldnames=title)
    dataWrite.writeheader()
    dataWrite.writerows(weather_list)