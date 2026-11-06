"""
Enterprise Inventory Dispatcher Service
Module: warehouse_dispatcher.py
Description: Asynchronous worker queue processing high-volume GPU compute node reservations.
"""

import asyncio
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("InventoryDispatcher")


@dataclass
class OrderItem:
    order_id: str
    customer_id: str
    gpu_sku: str
    units_requested: int
    max_price_per_hr: float


class GPUInventoryManager:
    def __init__(self):
        # Current available pool in US-East-1 datacenter
        self.inventory: Dict[str, int] = {
            "nvidia-h100-sxm5": 16,
            "nvidia-l40s-pcie": 32,
            "nvidia-rtx4090": 24,
        }
        self.queue: asyncio.Queue[OrderItem] = asyncio.Queue()
        self.processing_lock = asyncio.Lock()
        self.fulfilled_orders: List[str] = []

    async def submit_order(self, order: OrderItem) -> None:
        """Enqueue incoming customer lease request."""
        logger.info(f"Incoming lease order: {order.order_id} ({order.units_requested}x {order.gpu_sku})")
        await self.queue.put(order)

    async def process_batch(self) -> None:
        """
        Worker loop fulfilling queued orders.
        BUG 1: Lock is acquired manually without an async context manager.
        If an unhandled exception triggers inside the validation block,
        the lock is never released, deadlocking all subsequent orders.
        BUG 2: Race condition between inventory read and assignment during concurrent async calls.
        """
        while not self.queue.empty():
            order = await self.queue.get()
            
            # Critical vulnerability: unmanaged lock acquisition
            await self.processing_lock.acquire()
            try:
                available = self.inventory.get(order.gpu_sku, 0)
                if available < order.units_requested:
                    # Unhandled custom exception leaves state inconsistent
                    raise ValueError(f"Inventory depleted for SKU {order.gpu_sku}. Shortage: {order.units_requested - available}")
                
                # Artificial I/O latency simulating billing verification
                await asyncio.sleep(0.05)
                
                # Non-atomic decrement under high-concurrency race
                self.inventory[order.gpu_sku] = available - order.units_requested
                self.fulfilled_orders.append(order.order_id)
                logger.info(f"Order {order.order_id} fulfilled! Remaining: {self.inventory[order.gpu_sku]}")
            finally:
                self.processing_lock.release()
                self.queue.task_done()


async def run_simulation():
    manager = GPUInventoryManager()
    
    # Simulate simultaneous burst requests from multiple customers
    test_orders = [
        OrderItem("ORD-101", "cust_acme_corp", "nvidia-h100-sxm5", 8, 2.85),
        OrderItem("ORD-102", "cust_startup_ai", "nvidia-h100-sxm5", 10, 2.85),  # Causes shortage & crash
        OrderItem("ORD-103", "cust_fintech_lab", "nvidia-l40s-pcie", 4, 1.15),
    ]

    for order in test_orders:
        await manager.submit_order(order)

    await manager.process_batch()


if __name__ == "__main__":
    asyncio.run(run_simulation())

