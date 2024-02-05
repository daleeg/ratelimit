import asyncio
import logging

from dayu import AsyncRateLimit

LOG = logging.getLogger(__name__)


@AsyncRateLimit(limit=3)
async def add(a, b):
    await asyncio.sleep(0.01)
    return a + b


@AsyncRateLimit(limit=3, uniform_rate=True)
async def sub(a, b):
    await asyncio.sleep(0.2)
    return a - b


async def test():
    for i in range(20):
        LOG.info(await add(i, i))

    for i in range(20):
        LOG.info(await sub(i, 1))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    asyncio.run(test())
