import pyupbit

access = "7ZKb2uva9TL7gISxWvGktCb6HBF1egqnWMErI4yz"          # 본인 값으로 변경
secret = "xIJoymDGIeYbkXSiJHkpDFx8BSMOS6247M3HGRcw"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
#print(pyupbit.get_tickers())
print(pyupbit.get_current_price("KRW-BTC"))
print(len(pyupbit.get_ohlcv("KRW-BTC", interval="day")))              # 일봉 데이터 (5일)

#print(pyupbit.get_ohlcv("KRW-BTC", interval="minute1")) 