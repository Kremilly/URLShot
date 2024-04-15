from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Screenshot:
    
    @classmethod
    def take(cls, url: str, width: int, height: int):
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        
        options.use_chromium = True
        
        driver = webdriver.Edge(options=options)

        driver.get(url)
        driver.set_window_size(width, height)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, 'body')
            )
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'img[src], [background], [href], [srcset], script, style, iframe, link[rel=stylesheet]')
            )
        )
        
        driver.implicitly_wait(10)

        screenshot = driver.get_screenshot_as_png()
        driver.quit()
        
        return screenshot
