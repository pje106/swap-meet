from .item import Item

class Decor(Item):
    def __init__(self, condition = 0):
        # super().__init__(condition)
        self.category = "Decor"
        self.condition = condition
      
    

    def __str__(self):
        return "Something to decorate your space."
    
    def condition_description(self):
        super().condition_description(self)