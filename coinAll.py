import coinConnect
import mongoClient
from datetime import datetime

upbit = coinConnect.upbit
pyupbit = coinConnect.pyupbit
database = mongoClient.database
collection = database.get_collection('coin_all_list')

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회

#print(pyupbit.get_tickers())

print(datetime.today().strftime("%Y%m%d"))

result = pyupbit.get_tickers()
for i in result:
    print(i)
    
    #Insert Data
    collection.insert_one(
        {
            "name" : i,
            "use_yn" : "Y",
            "reg_dt" : datetime.today().strftime("%Y%m%d")
        }
    )