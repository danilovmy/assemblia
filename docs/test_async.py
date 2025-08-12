# import aiohttp
import asyncio
import httpx
from bs4 import BeautifulSoup as soup
from time import time
URLS =['http://example.net?idx=1', 'http://example.net?idx=2', 'http://example.net?idx=3', 'http://example.net?idx=4']

def test_requests():
    result = []
    for url in URLS:
        result += [made_request(url)]
    return result

def test_asyncrequests():
    tasks = []
    asyncio.run(gather_all(tasks))
    return [task.result() for task in tasks]

async def gather_all(tasks):
    for url in URLS:
        tasks.append(asyncio.create_task(made_arequest(url,)))
    async with asyncio.timeout(10):
        await asyncio.gather(*tasks)

async def made_arequest(url, text = ''):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    if getattr(response, 'status_code', None) == 200:
        text = response.text
    print(url, 'async ready')
    return soup(text, features="html.parser").title

def made_request(url, text = ''):
    response = httpx.get(url)
    if getattr(response, 'status_code', None) == 200:
        text = response.text
    print(url, ' sync ready')
    return soup(text, features="html.parser").title

if __name__ == '__main__':
    start = time()
    result = test_asyncrequests()
    print(result)
    print(time() - start)
    start = time()
    result = test_requests()
    print(result)
    print(time() - start)
