

# Class de prise en charge des calculs

def calcul():

    def __init__(self, elem1, elem2):
        self.el1 = elem1
        self.el2 = elem2

    def addition(self):
        return self.el1 + self.el2

    def soustraction(self):
        return self.el1 - self.el2

    def multiplication(self):
        return self.el1 * self.el2

    def division(self):

        if self.el1 == 0 or self.el2 == 0:
            print "Division par zero !"

        else:
            return self.el1 / self.el2
