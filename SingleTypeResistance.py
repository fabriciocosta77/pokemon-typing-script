from Types import *

def getSingleTypeResistanceAll():
    for type in types:
        getSingleTypeResistance(type)

def getSingleTypeResistance(type):
    resistance = []

    match type:
        case 'Normal':
            resistances = ['None']
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Fire':
            resistances = [types[1], types[3], types[5], types[10], types[11], types[14]]
            for i, slot in enumerate(resistances):
                resistance.append(slot)
            return resistance

        case 'Water':
            resistances = [types[1], types[2], types[5], types[10]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Grass':
            resistances = [types[2], types[3], types[4], types[8]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Electric':
            resistances = [types[4], types[10], types[15]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Ice':
            resistances = [types[5]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Fighting':
            resistances = [types[9], types[14], types[17]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Poison':
            resistances = [types[3], types[6], types[7], types[11], types[14]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Ground':
            resistances = [types[7], types[9]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Rock':
            resistances = [types[0], types[1], types[7], types[15]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Steel':
            resistances = [types[0], types[3], types[5], types[9], types[10], types[11], types[13], types[14], types[15], types[16]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Fairy':
            resistances = [types[6], types[14], types[17]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Ghost':
            resistances = [types[7], types[14]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Dragon':
            resistances = [types[1], types[2], types[3], types[4]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Bug':
            resistances = [types[3], types[6], types[8]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Flying':
            resistances = [types[3], types[6], types[14]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Psychic':
            resistances = [types[6], types[16]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case 'Dark':
            resistances = [types[12], types[17]]
            for i in resistances:
                resistance.append(i)
            return resistance

        case _:
            raise NameError("Type name incorrect! Check your spelling and try again.")

def printSingleTypeResistance(type):
    print(f"{type} type resists {getSingleTypeResistance(type)} types \n")

def printSingleTypeResistanceAll():
    for type in types:
        print(f"{type} type resists {getSingleTypeResistance(type)} types \n")