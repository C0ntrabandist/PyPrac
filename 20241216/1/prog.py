import asyncio

event = asyncio.Event()


async def writer(queue, delay):
    await asyncio.sleep(delay)
    i = 0
    while not event.is_set():
        await queue.put(f"{i}_{delay}")
        i += 1
        await asyncio.sleep(delay)


async def stacker(queue, stack):
    while not event.is_set():
        await asyncio.sleep(0)
        item = await queue.get()
        await stack.put(item)


async def reader(stack, count, delay):
    await asyncio.sleep(delay)
    i = 0
    while i < count:
        item = await stack.get()
        print(item)
        i += 1
        await asyncio.sleep(delay)
    event.set()


async def main():
    delay_1, delay_2, delay_3, count = eval(input())
    queue = asyncio.Queue(0)
    stack = asyncio.LifoQueue(0)
    await asyncio.gather(
        writer(queue, delay_1),
        writer(queue, delay_2),
        stacker(queue, stack),
        reader(stack, count, delay_3))

asyncio.run(main())