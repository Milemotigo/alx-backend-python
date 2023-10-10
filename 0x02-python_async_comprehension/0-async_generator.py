#/usr/bin/env python3
"""a coroutine called async_generator that takes no arguments."""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random
    """
    for _ in range(10):
        await asyncio.sleep(1)
        x = random.random() * 10
        yield x