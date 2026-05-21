from pydantic import BaseModel
from typing import Optional


class Booking(BaseModel):
    full_name: str
    email: str
    phone: str
    check_in: str
    check_out: str
    room_type: str
    guests: int
    special_requests: Optional[str] = ""
