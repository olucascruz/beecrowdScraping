from abc import ABC, abstractmethod

class State(ABC):
    
    owner = None
    
    def __init__(self, _owner) -> None:
        self.owner = _owner
    
    @abstractmethod
    def start_state(self):
        pass
    
    @abstractmethod
    def update_state(self):
        pass

    @abstractmethod
    def exit_state(self):
        pass