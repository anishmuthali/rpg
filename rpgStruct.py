class Player:
    def __init__(self, health):
        self.health = health
    def dmged(self):
        self.health -= 1
    def kicked(self):
        self.health -= 10 #change 10 to whatever u want later
    def punched(self):
        self.health -= 5 #change 5 to whatever u want later
    def stomped(self):
        self.health -= 15 #change 15 to whatever u want later
    def getHealth(self):
        return self.health


bob = Player(100)
health = 100
bob.kicked()
print bob.getHealth()



        
