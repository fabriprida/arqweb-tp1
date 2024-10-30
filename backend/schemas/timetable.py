from pydantic import BaseModel
from typing import List, Dict
from datetime import time
from core.constants import DayOfWeek

class Timetable(BaseModel):
    
    class TimeSlot(BaseModel):
        opening_time: time
        closing_time: time

    timetable: Dict[DayOfWeek, List[TimeSlot]]
