import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        url = 'http://httpbin.org/post'
        data = FormData()
        data.add_field('file',
                      open('report.xls', 'rb'),
                      filename='report.xls',
                      content_type='application/vnd.ms-excel')
        await session.post(url, data=data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
