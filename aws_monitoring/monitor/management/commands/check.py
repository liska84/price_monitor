from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .utils import sendSMS

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
driver = webdriver.Firefox(options=firefox_options)

class Command(BaseCommand):
    help = "Checks https://skillbuilder.aws/subscriptions for changes in individual annual subscription price and sends an SMS notification if changes are detected."
    CHECK = '$444'

    def handle(self, *args, **options):
        driver.get('https://skillbuilder.aws/subscriptions')
        time.sleep(5)

        driver.save_screenshot('debug_screenshot.png')

        price_element = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="annual-subscripton-price"] span')
        price = price_element.text if price_element else 'Price not found'
        driver.quit()

        if price != self.CHECK:
            sendSMS(price)
            self.stdout.write(self.style.SUCCESS('SMS sent'))
        else:
            self.stdout.write(self.style.SUCCESS('No changes detected'))