import requests

from bs4 import BeautifulSoup

def fetch_usdt_tvl_from_defillama():
    """
    This function fetches the total value locked (TVL) of USDT on the Defillama protocol.
    """
    response = requests.get('https://defillama.com/protocol/usdt')
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    usdt_tvl = soup.find('div', {'class': 'tvl-value'})
    return usdt_tvl

    

