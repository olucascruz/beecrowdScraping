from stateMachine.StateMachineBeecrowd import StateMachineBeecrowd
from botcity.web import WebBot, Browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from botcity.web.browsers.edge import default_options
if __name__ == '__main__':
    webbot = WebBot()
    webbot.browser = Browser.FIREFOX

    print("starting download")
    # set the WebDriver path
    webbot.driver_path = GeckoDriverManager().install()
    
    StateMachineBeecrowd(webbot)