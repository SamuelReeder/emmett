class Entity:
    
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    # this class will be the parent class for all entities in the game
    # then create subclasses for the different types of entities 
    # and program in exclusive things for them, like player rn