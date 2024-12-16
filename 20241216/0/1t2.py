import asyncio

async def hello(name):
    print(f"Hello, {name}!")
    return 42

#asyncio.run(hello("Me"))

async def twostep(a, b):
    print("Start", a, b)
    await asyncio.sleep(a)
    print("Continue", a, b)
    await asyncio.sleep(b)
    print("End", a, b)



async def main():
    await asyncio.gather((twostep(3, 4)),(twostep(1, 2)))

asyncio.run (main())