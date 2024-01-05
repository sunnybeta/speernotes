from pydantic import BaseModel

class Pagination(BaseModel):
    page_size: int
    page_number: int
    next_page: int
