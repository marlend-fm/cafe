import datetime
import errors


class Visitor:

    def __init__(self, visitor: dict):
        self.vaccine = visitor["vaccine"]
        self.wearing_a_mask = visitor["wearing_a_mask"]

    @property
    def vaccine_expiration_date(self) -> datetime.date:
        return self.vaccine["expiration_date"]


class Cafe:

    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor_data: dict):

        visitor = Visitor(visitor_data)

        date_today = datetime.date.today()

        if visitor.vaccine is None:
            raise errors.NotVaccinatedError("You are not vaccinated")

        elif date_today > visitor.vaccine_expiration_date:
            raise errors.OutdatedVaccineError("Your vaccine certificate is out of date")

        elif visitor.wearing_a_mask is False:
            raise errors.NotWearingMaskError("You are not wearing a mask")

        else:
            print(f'Welcome to {self.name}')

