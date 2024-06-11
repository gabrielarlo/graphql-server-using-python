from datetime import date
from dateutil.relativedelta import relativedelta
import strawberry

@strawberry.type
class UserType:
    id: int
    name: str
    age: int

    @staticmethod
    def calculate_age(bdate: date) -> int:
        today = date.today()
        return relativedelta(today, bdate).years
