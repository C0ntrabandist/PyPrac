import asyncio

q1 = asyncio.Queue()
q2 = asyncio.Queue()

async def cons():
    while True:
        res = await q2.get()
        print(f"\tcons: Got {res}, from q2")

async def prod():
    for i in range(5):
        await q1.put(f"value{i}")
        print(f"prod: Put q1: value{i}")
        await asyncio.sleep(1)
    print("prod: finished producing")

async def mid():
    while True:
        res = await q1.get()
        print(f"\t mid: Got {res}, from q1")
        await q2.put(res)
        print(f"mid: Put q2: {res}")

async def main():
    await asyncio.gather(prod(), mid(), cons())

asyncio.run(main())