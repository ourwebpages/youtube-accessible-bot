from database.repository import VideoRepository

class SearchService:
    def __init__(self, repository=None):
        self.repository = repository or VideoRepository()

    def search(self, user_id: int, query: str, limit: int = 10):
        return self.repository.search(user_id, query, limit)
