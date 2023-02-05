import datetime
from . import errors


class Visitor:

    def __init__(self, visitor: dict):
        self.vaccine = visitor["vaccine"]
        self.wearing_a_mask = visitor.get("wearing_a_mask")

    @property
    def vaccine_expiration_date(self) -> datetime.date:
        return self.vaccine['expiration_date']


class Cafe:

    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor_data: dict):
        visitor = Visitor(visitor_data)
        date2 = datetime.date.today()
        if visitor.vaccine is None:
            raise errors.NotVaccinatedError("Should be vassinated")

        elif date2 > visitor.vaccine_expiration_date:
            raise errors.OutdatedVaccineError

        elif visitor.wearing_a_mask is False:
            raise errors.NotWearingMaskError

        else:
            print(f'Welcome to {self.name}')
