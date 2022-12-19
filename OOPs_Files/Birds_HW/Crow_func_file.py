from Birds_Main_File import Birds
class Crow(Birds):
    
    def birds_name(self):
        return self.name + ' is Crow'
    def make_sound(self):
        return self.name + ' sounds ka ka'
    def birds_colour(self):
        return self.name + ' colour is Black'
    def walking_ability(self):
        return self.name + ' can walk'
    def swimming_ability(self):
        return False