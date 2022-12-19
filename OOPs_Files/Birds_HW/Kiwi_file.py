from Birds_Main_File import *

class Kiwi(Birds):
    def birds_name(self):
        return self.name + ' is Kiwi'
    def make_sound(self):
        return self.name + ' sounds trrr'
    def birds_colour(self):
        return self.name + ' colour is Grayish Brown'
    def walking_ability(self):
        return self.name + ' can walk'
    def flying_ability(self):
        return False
    def swimming_ability(self):
        return False