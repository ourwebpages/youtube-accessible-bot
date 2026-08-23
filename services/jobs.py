"""Background job helpers kept intentionally small for reliable polling."""
import asyncio
from collections.abc import Awaitable, Callable


async def run_in_background(fn: Callable[..., Awaitable[object]], *args) -> asyncio.Task:
    return asyncio.create_task(fn(*args))
