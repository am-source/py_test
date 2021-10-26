import bot_booking.booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bot_booking.booking.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"D:/Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        # instantiate super class, needed in child
        super(Booking, self).__init__()
        self.implicitly_wait(15)   # wait in case find_elem is called
        self.maximize_window()

    def __exit__(self, *args) -> None:  # method for teardown the whole test
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.accept_cookies()

    def accept_cookies(self):
        cookie_btn = self.find_element(
            By.ID, "onetrust-accept-btn-handler")
        cookie_btn.click()

    def change_currency(self, currency=None):
        curr_btn = self.find_element(
            By.CSS_SELECTOR, "button[data-tooltip-text='Wählen Sie Ihre Währung']")
        curr_btn.click()
        curr_select = self.find_element(
            By.CSS_SELECTOR, f"a[data-modal-header-async-url-param *={currency}]")
        curr_select.click()

    def select_destination(self, place_to_go):
        dest_elem = self.find_element(
            By.ID, "ss")
        dest_elem.clear()
        dest_elem.send_keys(place_to_go)

        sel_first_elem = self.find_element(
            By.CSS_SELECTOR, "li[data-i='0']")
        sel_first_elem.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_room_and_people(self, adults):
        room_people_elem = self.find_element(
            By.ID, "xp__guests__toggle")
        room_people_elem.click()
        self.select_adults(adults)

    def select_adults(self, adults):
        while True:
            decrease_adults_elem = self.find_element(
                By.CSS_SELECTOR, "button[aria-label='Erwachsene: Anzahl verringern']")
            decrease_adults_elem.click()
            # if value = 1 then leave loop
            adults_value_elem = self.find_element(
                By.ID, "group_adults")
            adults_value = adults_value_elem.get_attribute(
                "value")  # gets back the value of the adults count
            if int(adults_value) == 1:
                break
        add_adult_btn = self.find_element(
                By.CSS_SELECTOR, "button[aria-label='Erwachsene: Anzahl erhöhen']")
        for _ in range(adults-1):
            add_adult_btn.click()

    def click_search(self):
        search_btn = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_btn.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(5, 3, 4)
        filtration.sort_price_asc()

