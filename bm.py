import requests

#https://ticketmasterbr.queue-it.net/?c=ticketmasterbr&e=brunomarsvgbsb&cid=pt-BR&q=90ed7de7-18ec-4a19-8388-91e522f41006

url = 'https://ticketmasterbr.queue-it.net/?c=ticketmasterbr&e=brunomarsvgbsb&cid=pt-BR&q=90ed7de7-18ec-4a19-8388-91e5'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'Queue-it-ticketmasterbr______brunomarsvgbsb=Qid=90ed7de7-18ec-4a19-8388-91e522f41006&Cid=pt-BR&f=0; Queue-it-90ed7de7-18ec-4a19-8388-91e522f41006=WasRedirected=false&i=638508046392985393; Queue-it=u=de3d3f21-f7c4-4fd9-8bb4-6c2b480dcdff',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}

response = requests.get(url, headers=headers)

if 'Set-Cookie' in response.headers:
    print("Cookies definidos na resposta:")
    # Obter o cabeçalho 'Set-Cookie' da resposta
    set_cookie_header = response.headers['Set-Cookie']
    # Dividir o cabeçalho 'Set-Cookie' em cookies individuais
    cookies = set_cookie_header.split(', ')
    # Iterar sobre os cookies e imprimir cada um
    for cookie in cookies:
        print(cookie)

#print(response.cookies)
#print(response.status_code)