#!/usr/bin/env python3
"""async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async wait_random"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
