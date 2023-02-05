class VaccineError(Exception):
    '''Родительский класс исключений'''
    pass

class NotVaccinatedError(VaccineError):
    '''Класс исключения при отсутствии вакцинации'''
    def __init__(self):
        self.message = 'You are not vaccinated'
        print(self.message)


class OutdatedVaccineError(VaccineError):
    '''Класс исключения при просрочке сертификата о вакцинации'''
    def __init__(self):
        self.message = 'Your certificate is out of date'
        print(self.message)


class NotWearingMaskError(Exception):
    '''Класс исключения при отстутсвии маски у посетителя'''
    def __init__(self):
        self.message = 'You should wearing mask'
        print(self.message)

