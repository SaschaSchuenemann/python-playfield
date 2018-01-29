import requests

def load(x):
    myurl = 'https://api.binance.com/api/v1/trades?symbol=' + x
    response = requests.get(myurl)
    if response.status_code != requests.codes.ok:
      raise Exception("Call to url %s failed with status: %s" % (myurl, response.status_code))
    result = response.json()
    return result

def getAverage(data):
    count = 0
    sum = 0
    for trade in data:
      count = count + 1
      sum= sum + float(trade['price'])
    return sum/count  