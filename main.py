import datetime
import cafe
import errors


def go_to_cafe(friends: list, cafe: str):
    data2 = datetime.date.today()

    if all(map(lambda x: data2 <= x['vaccine']['expiration_date'] if x.get('vaccine') else False, friends)) is False:
        print('All friends should be vaccinated')

    elif all(map(lambda x: x['wearing_a_mask'], friends)) is False:
        masks_to_buy = 0
        for friend_mask in list(map(lambda x: x['wearing_a_mask'], friends)):
            if friend_mask is False:
                masks_to_buy += 1
        print(f'Friends should buy {masks_to_buy} masks')

    else:
        print(f'Friends can go to {cafe}')


# Проверка

caffe = cafe.Cafe('KFC')
try:
    caffe.visit_cafe({
        "name": "Paul",
        "age": 23,
        "vaccine": {
            "expiration_date": datetime.date(year=2019, month=2, day=23)
        },
        "wearing_a_mask": True
    })
except errors.VaccineError:
    pass
except errors.NotWearingMaskError:
    pass
go_to_cafe([
    {
        "name": "Alisa",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    },
], 'KFC')
