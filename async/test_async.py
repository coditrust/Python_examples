import asyncio

async def simple_print(msg):
    print(msg)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(simple_print('Hello'))
