from yahoo_fin import stock_info

print(stock_info.get_live_price('AAPL'))

data = {}
data['AAPL'] = stock_info.get_data('AAPL', start_date='08-01-2020',  end_date='08-22-2020')
print(data['AAPL'].head())
print(data["AAPL"])

print("done")