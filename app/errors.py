class VaccineError(Exception):
    '''Родительский класс исключений'''
    pass


class NotVaccinatedError(VaccineError):
    '''Класс исключения при отсутствии вакцинации'''


class OutdatedVaccineError(VaccineError):
    '''Класс исключения при просрочке сертификата о вакцинации'''


class NotWearingMaskError(Exception):
    '''Класс исключения при отстутсвии маски у посетителя'''

