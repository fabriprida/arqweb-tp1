from pydantic import BaseModel, model_validator
from typing import List, Dict
from datetime import time
from core.constants import DayOfWeek

class Timetable(BaseModel):
    
    class TimeSlot(BaseModel):
        opening_time: str  # !TODO: Change to time - MongoDB does not support keys other than strings
        closing_time: str # !TODO: Change to time - MongoDB does not support keys other than strings

    # timetable: Dict[DayOfWeek, List[TimeSlot]] # !TODO: Change to DayOfWeek - MongoDB does not support keys other than strings
    timetable: Dict[str, List[TimeSlot]]

  
