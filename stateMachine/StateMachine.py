from stateMachine.State import State


class StateMachine:
    previous_state:State = None
    current_state:State = None
    is_running:bool = True


    def __init__(self) -> None:
        pass

    
    def run():
        pass
    
    def stop(self):
        if self.current_state != None:
            self.current_state.exit_state()
        self.is_running = False
    
    def switch_state(self, next_state:State):
        if self.current_state != None:
            self.current_state.exit_state()
        self.previous_state = self.current_state
        self.current_state = next_state
        self.current_state.start_state()

    