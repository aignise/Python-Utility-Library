import asyncio

async def async_task(duration):
    """
    An asynchronous task that simulates a delay.
    """
    print(f"Task started. Will run for {duration} seconds.")
    await asyncio.sleep(duration)
    print(f"Task completed after {duration} seconds.")

async def main():
    tasks = [async_task(i) for i in range(3)]
    await asyncio.gather(*tasks)

# asyncio.run(main())  # To execute the tasks
