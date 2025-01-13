import asyncio

async def start_strongman(name, power):
    balls = 1
    print(f"Силач {name} начал соревнования.")
    while balls < 6:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {balls}')
        balls += 1
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():

    task1 = asyncio.create_task(start_strongman('Олег', 4))
    task2 = asyncio.create_task(start_strongman('Виктор', 3))
    task3 = asyncio.create_task(start_strongman('Данил', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())