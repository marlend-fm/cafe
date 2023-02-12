import datetime
import cafe, errors

class Friends():

    def __init__(self, friend: dict):
        self.vaccine = friend["vaccine"]
        self.wearing_a_mask = friend["wearing_a_mask"]

    @property
    def vaccine_expiration_date(self) -> datetime.date:
        return self.vaccine["expiration_date"]

    try:
        def go_to_cafe(friends: list, cafe: cafe.Cafe):

            date_today = datetime.date.today()

            vaccine_flag = True
            wearing_a_mask_flag = True

            masks_to_buy = 0

            for friend in friends:
                if friend.vaccine is None or date_today >= friend.vaccine_expiration_date:
                    vaccine_flag = False

                if friend.wearing_a_mask is False:
                    wearing_a_mask_flag = False
                    masks_to_buy += 1

            if vaccine_flag == False:
                print("All friends should be vaccinated")

            elif wearing_a_mask_flag == False:
                print(f'Friends should buy {masks_to_buy} masks')

            else:
                print(f'Friends can go to {cafe.name}')

    except errors.VaccineError:
        pass
    except errors.NotWearingMaskError:
        pass

Friends.go_to_cafe(
        (
            [
                {
                    "name": "Ivan",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=4),
                    },
                    "wearing_a_mask": True,
                },]
            ), cafe.Cafe("KFC"))
