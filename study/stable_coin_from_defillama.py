import requests
from datetime import datetime, timedelta

def stablecoins_tvl_volume_chains(days:int):
    # 定义API请求的URL和参数
    base_url = "https://stablecoins.llama.fi"
    endpoint = "/stablecoincharts/{}"
    chains = ["Ethereum", "Binance Smart Chain", "Polygon", "Solana", "Fantom", "Avalanche", "Harmony", "Arbitrum"]

    # 定义时间参数
    now = datetime.now()
    start_time = (now - timedelta(days)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    end_time = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    # 发送API请求并处理响应
    for chain in chains:
        response = requests.get(base_url + endpoint.format(chain), params={"start": start_time, "end": end_time})
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Failed to get data for {chain}, status code = {response.status_code}")
