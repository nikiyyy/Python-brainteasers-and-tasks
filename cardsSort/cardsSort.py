class Card:
    
    def __init__(self, color, name, gamerule = None):
        self.__color = color
        self.__name = name
        self.gamerule = gamerule
        
    def __repr__(self):
        return "{} {}".format(self.__name, self.__color)

    def getter_name(self):
        return self.__name
    
    def applyGameRule(self, dictionary):
        
        for i in dictionary.keys():
            if i == self.__name:
                self.gamerule = dictionary.get(i)
                break
            
#Rule 1 - 7 > 8 > Queen > King > Ace > 9 > Jack
def sortByRules1(deck):
    #rules for the objects to be sorted by
    rule={"7" : 1, "8" : 2, "queen" : 3, "king" : 4, "10" : 5, "ace" : 6, "9" : 7, "vale" : 8}
    
    #applies the rules for the object to be sorted by
    for i in deck:
        i.applyGameRule(rule)
    
    #return the sorted list
    return sorted(deck ,key=lambda Card: Card.gamerule)
    
        

def main():
    # delaration of the list of cards
    Deck1 = [Card("pika","queen"),Card("karo","king"),Card("kupa","10"),Card("spatiq","7")]
    
    print(sortByRules1(Deck1))


if __name__ == "__main__":
    main()