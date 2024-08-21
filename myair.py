import requests
serviceKey='vsdv0OjnMICmdPWCZ7UQ1XZfqxBM2sMvlfyaxgBhVCHG2m5VA5LLG5jvhKddJZPEu9u45h240oUwyCUTnbC0ng=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey , 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
data=response.json()
print(type(data))
print(data['response']['body']['items'][1]['pm10Value'])
