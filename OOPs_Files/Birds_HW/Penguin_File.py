from Birds_Main_File import Birds
class Penguin(Birds):
    
    def birds_name(self):
        return self.name + ' is Penguin'
    def make_sound(self):
        return self.name + ' sounds krrr'
    def birds_colour(self):
        return self.name + ' colour is Black and White'
    def flying_ability(self):
        return False
    def walking_ability(self):
        return self.name + ' can walk'
    def swimming_ability(self):
        return True