from datetime import datetime


def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()

        today = datetime.today().date()

        difference = today - date_obj

        return difference.days
    except ValueError:
        raise ValueError("Incorrect date format. Please use the format 'YYYY-MM-DD'.")


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
