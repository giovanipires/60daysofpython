"""Module providing a function async python version."""
import asyncio

async def tarefa1():
    """Utilizando o async."""
    print("Executando tarefa 1")
    await asyncio.sleep(2)
    print("Tarefa 1 concluída.")
    return 1

async def tarefa2():
    """Utilizando o async."""
    print("Executando tarefa 2")
    await asyncio.sleep(3)
    print("Tarefa 2 concluída.")
    return 2

async def tarefa3():
    """Utilizando o async."""
    print("Executando tarefa 3")
    await asyncio.sleep(5)
    print("Tarefa 3 concluída.")
    return 3

async def tarefa4():
    """Utilizando o async."""
    print("Executando tarefa 4")
    await asyncio.sleep(4)
    print("Tarefa 4 concluída.")
    return 4

async def main():
    """Utilizando o async."""
    t1 = asyncio.create_task(tarefa1())
    t2 = asyncio.create_task(tarefa2())
    t3 = asyncio.create_task(tarefa3())
    t4 = asyncio.create_task(tarefa4())
    results = await asyncio.gather(t1, t2, t3, t4)
    print(results)
    print("Tarefas finanlizadas")
    await main()

