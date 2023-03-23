from stable_coin_from_defillama import fetch_usdt_tvl_from_defillama

def test_usdt():
    tvl = fetch_usdt_tvl_from_defillama()
    print("usdt tvl = ",tvl)

if __name__ == '__main__':
    test_usdt()
