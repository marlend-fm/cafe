import datetime
from .cafe import Cafe
from errors import VaccineError, NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        ...
    return "Friends can go to {}".format(cafe.name)
