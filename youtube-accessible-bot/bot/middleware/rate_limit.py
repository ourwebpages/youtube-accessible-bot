import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, limit: int, window: float = 60):
        self.limit = limit
        self.window = window
        self._events = defaultdict(deque)

    def allowed(self, user_id: int) -> bool:
        now = time.monotonic()
        q = self._events[user_id]
        while q and now - q[0] >= self.window:
            q.popleft()
        if len(q) >= self.limit:
            return False
        q.append(now)
        return True
