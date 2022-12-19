from Birds_Main_File import * 

class Eagle(Birds):
    def birds_name(self):
        return self.name + ' is Eagle'
    def make_sound(self):
        return self.name + ' sounds errr'
    def birds_colour(self):
        return self.name + ' colour is Dark Brown'
    def walking_ability(self):
        return self.name + ' can walk'
    def swimming_ability(self):
        return False
     