from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_destination("New York")
    bot.select_dates("2021-10-29", "2021-11-09")
    bot.select_room_and_people(1)
    bot.click_search()
    bot.apply_filtrations()