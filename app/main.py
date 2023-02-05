import datetime
from . import cafe, errors


def go_to_cafe(friends: list, cafe: cafe.Cafe):
    todays_date = datetime.date.today()

    if not all(map(lambda x: todays_date <= x['vaccine']['expiration_date'] if x.get('vaccine') else False, friends)):
        print('All friends should be vaccinated')

    elif all(map(lambda x: x['wearing_a_mask'], friends)) is False:
        masks_to_buy = 0
        for friend_mask in list(map(lambda x: x['wearing_a_mask'], friends)):
            if friend_mask is False:
                masks_to_buy += 1
        print(f'Friends should buy {masks_to_buy} masks')

    else:
        print(f'Friends can go to {cafe}')

