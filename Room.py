class Room:
    #constructor
    def __init__ (self):
        self.name=None
        self.description=None
    #getter
    def get_description(self):
        return self.description
    #setter
    def set_description(self, room_description):
        self.description=room_description   
    
    def describe(self):
        print(self.description)
    
    def get_name(self):
        return self.name
    
    def set_name(self, room_name):
        self.name=room_name
