import logging
import time

from dayu import RateLimit

LOG = logging.getLogger(__name__)


@RateLimit(limit=3)
def add(a, b):
    time.sleep(0.01)
    return a + b


@RateLimit(limit=3, uniform_rate=True)
def sub(a, b):
    time.sleep(0.02)
    return a - b


def test():

    for i in range(20):
        LOG.info(add(i, i))

    for i in range(20):
        LOG.info(sub(i, 1))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    test()
