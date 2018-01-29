import binance,pytest



@pytest.fixture()
def valid_data():
    print("setup")
    data = binance.load("LTCBTC")
    return data

def test_loaded_data_is_dictionary(valid_data):
    assert isinstance(valid_data, list)

def test_loaded_data_contains_trades(valid_data):
    assert len(valid_data) > 0
    for trade in valid_data:
      assert 'id' in trade
      assert 'price' in trade

def test_loaded_data_contains_valid_trades(valid_data):
    for trade in valid_data:
      assert isinstance(trade['id'],int)
      assert isinstance(float(trade['price']),float)

def test_load_fails_when_using_invalid_input():
    with pytest.raises(Exception):
      binance.load("fail")

def test_calulate_average_of_real_prices(valid_data):
    assert binance.getAverage(valid_data) > 0

def test_calculate_average_price():
    data = []
    for i in range(1,20):
      data.append({'id' : i, 'price': i})
    assert binance.getAverage(data) == 10
