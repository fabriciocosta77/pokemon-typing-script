from Types              import *
from SingleTypeImmunity import *

def getSingleTypeWeaknessAll():
    for type in types:
        getSingleTypeWeakness(type)

def getSingleTypeWeakness(type):
    weakness = []

    match type:
        case 'Normal':
            weaknesses = [types[6]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Fire':
            weaknesses = [types[2], types[8], types[9]]
            for i, slot in enumerate(weaknesses):
                weakness.append(slot)
            return weakness

        case 'Water':
            weaknesses = [types[3], types[4]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Grass':
            weaknesses = [types[1], types[5], types[7], types[14], types[15]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Electric':
            weaknesses = [types[8]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Ice':
            weaknesses = [types[1], types[6], types[9], types[10]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Fighting':
            weaknesses = [types[11], types[15], types[16]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Poison':
            weaknesses = [types[8], types[16]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Ground':
            weaknesses = [types[2], types[3], types[5]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Rock':
            weaknesses = [types[2], types[3], types[6], types[8], types[10]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Steel':
            weaknesses = [types[1], types[6], types[8]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Fairy':
            weaknesses = [types[7], types[10]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Ghost':
            weaknesses = [types[12], types[17]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Dragon':
            weaknesses = [types[5], types[11], types[13]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Bug':
            weaknesses = [types[1], types[9], types[15]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Flying':
            weaknesses = [types[4], types[5], types[9]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Psychic':
            weaknesses = [types[12], types[14], types[17]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case 'Dark':
            weaknesses = [types[6], types[11], types[14]]
            for i in weaknesses:
                weakness.append(i)
            return weakness

        case _:
            raise NameError("Type name incorrect! Check your spelling and try again.")

def printSingleTypeWeakness(type):
    print(f"{type} type is weak against {getSingleTypeWeakness(type)} types \n")

def printSingleTypeWeaknessAll():
    for type in types:
        print(f"{type} type is weak against {getSingleTypeWeakness(type)} types \n")