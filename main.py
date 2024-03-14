from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.data
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY = "FRA"

for i in sheet_data:
    if i['iataCode'] == '':
        i['iataCode'] = flight_search.get_destination_code(i['city'])
        data_manager.data = sheet_data
        data_manager.update_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_email(message=f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
