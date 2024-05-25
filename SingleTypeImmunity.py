from Types import *

def getSingleTypeImmunityAll():
    for type in types:
        getSingleTypeImmunity(type)

def getSingleTypeImmunity(type):
    immunity = []

    match type:
        case 'Normal':
            immunities = [types[12]]
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Fire':
            immunities = ['None']
            for i, slot in enumerate(immunities):
                immunity.append(slot)
            return immunity

        case 'Water':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Grass':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Electric':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Ice':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Fighting':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Poison':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Ground':
            immunities = [types[4]]
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Rock':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Steel':
            immunities = [types[7]]
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Fairy':
            immunities = [types[13]]
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Ghost':
            immunities = [types[0], types[6]]
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Dragon':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Bug':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Flying':
            immunities = [types[8]]
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Psychic':
            immunities = ['None']
            for i in immunities:
                immunity.append(i)
            return immunity

        case 'Dark':
            immunities = [types[16]]
            for i in immunities:
                immunity.append(i)
            return immunity

        case _:
            raise NameError("Type name incorrect! Check your spelling and try again.")

def printSingleTypeImmunity(type):
    print(f"{type} type is immune against {getSingleTypeImmunity(type)} types \n")

def printSingleTypeImmunityAll():
    for type in types:
        print(f"{type} type is immune against {getSingleTypeImmunity(type)} types \n")