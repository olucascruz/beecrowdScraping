from stateMachine.StateMachine import StateMachine
from .states.BeecrowdState import BeecrowdState

class StateMachineBeecrowd(StateMachine):
    webbot = None
    solved_number = None
    def __init__(self, _webbot) -> None:
        super().__init__()
        self.webbot = _webbot
        self.switch_state(BeecrowdState(self))
        self.run()

    def run(self):
        while self.is_running:
            self.current_state.update_state()

