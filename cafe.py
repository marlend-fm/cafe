import datetime
import errors


class Cafe:

    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):

        date2 = datetime.date.today()

        if visitor.get('vaccine') is None:
            raise errors.NotVaccinatedError

        elif date2 > visitor['vaccine']['expiration_date']:
            raise errors.OutdatedVaccineError

        elif visitor['wearing_a_mask'] is False:
            raise errors.NotWearingMaskError

        else:
            print(f'Welcome to {self.name}')
