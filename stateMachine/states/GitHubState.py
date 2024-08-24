from stateMachine.StateMachine import StateMachine
from ..State import State
from botcity.web import WebBot, By
from dotenv import dotenv_values
from selenium.webdriver.common.keys import Keys

class GitHubState(State):
    def __init__(self, _owner: StateMachine) -> None:
        super().__init__(_owner)

    username = None
    password = None
    
    def start_state(self):
        super().start_state()
        print('Starting github state')
        config = dotenv_values(r"stateMachine/states/.env")
        self.username = config.get("USERNAME")
        self.password = config.get("PASSWORD")
    
    def update_state(self):
        super().update_state()
        
        print('in github state')
        webbot:WebBot = self.owner.webbot
        webbot.navigate_to('https://github.com/login')
        login_field = webbot.find_element('login_field', by=By.ID)
        login_field.click()
        webbot.kb_type(self.username)
        webbot.tab()
        webbot.kb_type(self.password)
        webbot.tab()
        webbot.tab()
        webbot.enter()
        webbot.wait(3000)
        webbot.navigate_to(f'https://github.com/{self.username}/{self.username}/edit/main/README.md')
        webbot.wait(3000)
        webbot.type_keys([Keys.CONTROL, 'f'])
        webbot.kb_type('Resolvidos')
        webbot.enter()
        webbot.type_keys([Keys.ESCAPE])
        webbot.type_keys([Keys.SHIFT, Keys.END])
        webbot.kb_type(f'Resolvidos: {self.owner.solved_number}')
        webbot.wait(3000)
        commit_button = webbot.find_element('/html/body/div[1]/div[5]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/button', by=By.XPATH)
        commit_button.click()
        breakpoint()
        self.owner.stop()
    
    def exit_state(self):
        super().update_state()
        print('Exiting githubState state')