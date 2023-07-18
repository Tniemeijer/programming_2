# Good work!
"""
Main starts the server for the network client to get the data from
"""
import asyncio

from network_client import NetworkClient


async def main():
    base_url = "http://localhost:9000/data/"
    nc = NetworkClient(base_url)
    tasks = [
        asyncio.sleep(5),
        nc.get_data('2000/2001'),
        asyncio.sleep(1),
        nc.get_data('all'),
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        if result is not None:
            print(result)



if __name__ == '__main__':
        asyncio.run(main())