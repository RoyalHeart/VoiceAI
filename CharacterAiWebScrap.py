
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from modules.EL_TTS import EL_TTS

CHROME_DRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"
chrome_service = Service(CHROME_DRIVER_PATH)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-login-animations")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
characterAiUrl = "https://beta.character.ai"
characterAiAmaUrl = "https://beta.character.ai/chat?char=zb7I4U9OYfewmEgOWLBHScefPeELkm1J-_GZDjHLY1M"


def main():
    global driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(characterAiUrl)
    print(driver.get_cookies)
    print("> Load Charater AI")
    try:
        # acceptCookies()
        # time.sleep(1)
        # logIn()
        # time.sleep(1)
        # logIn2()
        # time.sleep(1)
        # inputUsername()
        # time.sleep(1)
        # inputPassword()
        # time.sleep(1)
        # clickContinue()
        # time.sleep(1)
        message = "Can you give me a Selenium example to scrap character.ai"
        # inputMessage(message)
        # EL_TTS(message)
        print("> Cookie: ", driver.get_cookies)
        # sendMessage()
    except:
        print("> Error")
    finally:
        print("> Finally")
        while (True):
            time.sleep(1)
            # driver.quit()


def chooseAIBot():
    bot = getElementXpathWait("")
    bot.click()


def acceptCookies():
    getElementXpathWait("//*[@id=\"#AcceptButton\"]").click()
    print("> Accept cookies")


def logIn():
    getElementXpathWait("//*[@id=\"header-row\"]/a[4]/button").click()
    print("> Log in")


def logIn2():
    getElementXpathWait(
        "/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/button").click()
    print("> Log in")


def inputUsername():
    username = "huyenma2002@gmail.com"
    getElementXpathWait(
        "//*[@id=\"username\"]").send_keys(username)
    print("> Input username", username)


def inputPassword():
    password = "K@rot42002"
    getElementXpathWait("//*[@id=\"password\"]").send_keys(password)
    print("> Input password")


def clickContinue():
    getElementXpathWait(
        "/html/body/div/main/section/div/div/div/form/div[2]/button").click()
    print("> Click continue")


def inputMessage(message: str) -> bool:
    try:
        print("> Input Message: ", message)
        inputBox = getElementXpathWait("//*[@id=\"user-input\"]")
        inputBox.send_keys(message)
        return True
    except:
        return False


def sendMessage() -> bool:
    try:
        sendMessage: WebElement = getElementXpathWait(
            "//*[@id=\"root\"]/div[2]/div/div[3]/div/div/form/div/div/div[2]/button[1]"
        )
        sendMessage.click()
        return True
    except:
        return False


def getElementXpathWait(XPath: str, timeout=10) -> WebElement:
    try:
        element = WebDriverWait(
            driver,
            timeout=timeout).until(lambda x: x.find_element(By.XPATH, XPath))
        return element
    except:
        return None


# global driver
# driver = webdriver.Chrome(
#     service=chrome_service, options=chrome_options)
# driver.get(characterAiUrl)
# while (True):
#     True
if __name__ == "__main__":
    main()
