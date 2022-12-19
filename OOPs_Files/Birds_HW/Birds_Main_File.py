class Birds():
     
    def birds_name(self):
        return ''
    
    def birds_colour(self):
        return ''
     
    def make_sound(self):
        return ''
    
    def flying_ability(self):
        return True
    
    def walking_ability(self):
        return True
    #underwater swimming ability
    def swimming_ability(self):
        return True

def Birds_details(birds):
    print(birds.birds_name())
    print(birds.birds_colour())
    print(birds.make_sound())
    print(birds.walking_ability())
    if birds.flying_ability() == True:
        print(birds.name + ' can fly')
    else:
        print(birds.name + ' can not fly')
    
    if birds.swimming_ability() == True :
        print(birds.name + ' can Swim')
    else:
        print(birds.name + ' can not Swim')