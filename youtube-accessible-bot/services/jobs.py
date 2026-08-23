import asyncio
from collections.abc import Awaitable, Callable

async def run_background(task: Callable[[], Awaitable[object]]):
    return await asyncio.to_thread(lambda: asyncio.run(task()))
