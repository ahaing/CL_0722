## https://youtube.com/live/ajU_bMfGYvE

import requests

def download_weather():
    url ='https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-007?Authorization=rdec-key-123-45678-011121314&format=JSON'

    responseR = requests.get(url)
    if responseR.status_code == 200:
        print("下載成功")
        weather = responseR.json()
        return weather
    else:
        print("下載失敗")
        return False


def main():
    print("main function")
    # 下載json
    weather = download_weather()
    if weather != False:
        print("下載完畢")
    else:
        print("應用程式下載失敗")
        return


if __name__ == "__main__":
    main()  


