import asyncio
from typing import Any, Dict, List
import logging

logging.basicConfig(level=logging.INFO)

class PubSub:
    def __init__(self):
        self.channels: Dict[str, List[asyncio.Queue]] = {}

    async def publish(self, channel: str, message: Any):
        logging.info(f"Publishing to channel {channel}: {message}")
        if channel in self.channels:
            for queue in self.channels[channel]:
                await queue.put(message)

    async def subscribe(self, channel: str) -> asyncio.Queue:
        queue = asyncio.Queue()
        if channel not in self.channels:
            self.channels[channel] = []
        self.channels[channel].append(queue)
        logging.info(f"Subscribed to channel {channel}")
        return queue

    async def unsubscribe(self, channel: str, queue: asyncio.Queue):
        if channel in self.channels:
            self.channels[channel].remove(queue)
            logging.info(f"Unsubscribed from channel {channel}")
            if not self.channels[channel]:
                del self.channels[channel]

pubsub = PubSub()
