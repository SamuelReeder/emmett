from player import Player

class Main:
    
    def __init__(self, players) -> None:
        self.player = Person("name")
        
    
    def prompt(self, prompt: str, variable: object, func) -> None:
        # here could have a generic function for prompting where you can pass a prompt
        # and a variable to update based on response or thing to run
        # even a reference to a function to determine outcome of promp 
        variable = input(prompt)
        if prompt == "prompt":
            func()
        pass
    
    
    def display(self) -> None:
        pass
    
    
    def run(self) -> None:
        # run init functions
        
        player = Player("name")
        
        while True:
            # game loop
            
           self.var = None 
            
           self.prompt("prompt", self.var, self.display) 
           pass