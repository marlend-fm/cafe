class VaccineError(Exception):
    ''''''
    pass

class NotVaccinatedError(VaccineError):
    '''Exception class in the absence of vaccination'''



class OutdatedVaccineError(VaccineError):
    '''Exemption class for expired certificate of vaccination'''



class NotWearingMaskError(Exception):
    '''Exception class when the visitor does not have a mask'''

