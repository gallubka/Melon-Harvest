############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
       

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", "seedless", "best seller", "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)
    casaba = MelonType("cas", 2003, "orange", "has seeds", None, "Casaba")
    casaba.add_pairing("strawberries and mint")
    all_melon_types.append(casaba)
    crenshaw = MelonType("cren", 1996, "green", "has seeds", None, "Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)
    yellow = MelonType("yw", 2013, "yellow", "has seeds", "best seller", "Yellow Watermelon")
    yellow.add_pairing("ice cream")
    all_melon_types.append(yellow)


    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""


    for melon in melon_types:
        print(f"{melon.name}, pairs with")
        for pairing in melon.pairings:
            print(f"-{pairing}")

#print_pairing_info(make_melon_types())


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # dict = { code : melon }
    melon_by_code = {}
    for melon in melon_types:
        melon_by_code[melon.code] = melon


    return melon_by_code

#print(make_melon_type_lookup(make_melon_types()))



############
# Part 2   #
############ 



class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape, color, field, harvested_by):

        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvested_by = harvested_by

    
    def is_sellable(self):
        """can this melon be sold"""
        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True
        else: 
            return False

        #return message
        


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    # Fill in the rest
    all_melons = []
    #melon_by_code = dictionary of melon types by code
    melon_by_code = make_melon_type_lookup(melon_types)

    melon1 = Melon(melon_by_code['yw'], 8, 7, 2, 'Sheila')
    all_melons.append(melon1)
    melon2 = Melon(melon_by_code['yw'], 3, 4, 2, 'Shelia')
    all_melons.append(melon2)
    melon3 = Melon(melon_by_code['yw'], 9, 8, 3, 'Shelia')
    all_melons.append(melon3)
    melon4 = Melon(melon_by_code['cas'], 10, 6, 35, 'Shelia')
    all_melons.append(melon4)
    melon5 = Melon(melon_by_code['cren'], 8, 9, 35, 'Michael')
    all_melons.append(melon5)
    melon6 = Melon(melon_by_code['cren'], 8, 2, 35, 'Michael')
    all_melons.append(melon6)
    melon7 = Melon(melon_by_code ['cren'], 2, 3, 4, 'Michael')
    all_melons.append(melon7)
    melon8 = Melon(melon_by_code['musk'], 6, 7, 4, 'Micheal')
    all_melons.append(melon8)
    melon9 = Melon(melon_by_code['yw'], 7, 10, 3, 'Sheila')
    all_melons.append(melon9)


    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
    
        if melon.is_sellable():
            message = "(CAN BE SOLD)"
        else:
            message = "(NOT SELLABLE)"

        print(f"Harvested by {melon.harvested_by} From field {melon.field} {message}")

    
            
get_sellability_report(make_melons((make_melon_types())))
