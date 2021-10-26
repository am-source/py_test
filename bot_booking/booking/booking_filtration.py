# responsible for interaction with website,  applying filtration to results
from selenium.webdriver.remote.webdriver import By, WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        self.driver.implicitly_wait(3)
        star_filtration_box = self.driver.find_element(
            By.CSS_SELECTOR, "div[data-filters-group='class']"
        )
        star_child_elements = star_filtration_box.find_elements(
            By.CSS_SELECTOR, "*"
        )

        # with get_attribute and the innerhtml tag we can extract things like
        # <h1>Hello</h1>
        for star_values in star_values:
            for star_elem in star_child_elements:
                if str(star_elem.get_attribute("innerHTML")).strip() == f"{star_values} Sterne/andere Bewertungen":
                    star_elem.click()

    def sort_price_asc(self):
        elem = self.driver.find_element(
            By.CSS_SELECTOR, "li[data-id='price']"
        )
        elem.click()