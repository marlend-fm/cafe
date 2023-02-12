import datetime
from .errors import VaccineError, NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Visitor:

    def __init__(self, visitor: dict):
        self.vaccine = visitor.get("vaccine")
        self.wearing_a_mask = visitor.get("wearing_a_mask")
        self.visiting_date = datetime.date.today()

    @property
    def vaccine_expiration_date(self) -> datetime.date:
        return self.vaccine.get("expiration_date")

    @property
    def is_vaccine_date_expirated(self) -> bool:
        return self.visiting_date > self.vaccine_expiration_date


class Cafe:

    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor_data: dict) -> str:

        visitor = Visitor(visitor_data)

        if visitor.vaccine is None:
            raise NotVaccinatedError("You are not vaccinated")

        elif visitor.is_vaccine_date_expirated:
            raise OutdatedVaccineError("Your vaccine certificate is out of date")

        elif not visitor.wearing_a_mask:
            raise NotWearingMaskError("You are not wearing a mask")

        return f"Welcome to {self.name}"
