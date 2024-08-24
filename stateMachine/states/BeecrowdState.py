from stateMachine.StateMachine import StateMachine
from ..State import State
from stateMachine.states.GitHubState import GitHubState
from botcity.web import WebBot, By

class BeecrowdState(State):
    def __init__(self, _owner: StateMachine) -> None:
        super().__init__(_owner)

    def start_state(self):
        super().start_state()
        print('Starting beecrowd state')
    
    def update_state(self):
        super().update_state()
        print('in beecrowd state')
        webbot:WebBot = self.owner.webbot
        webbot.browse("https://judge.beecrowd.com/pt/profile/592929")
        webbot.maximize_window()
        solved_number = webbot.find_element('profile-solved-number', by=By.CLASS_NAME)
        self.owner.solved_number = solved_number.text
        self.owner.switch_state(GitHubState(self.owner))
        
    
    def exit_state(self):
        super().update_state()
        print('Exiting beecrowd state')
        
        