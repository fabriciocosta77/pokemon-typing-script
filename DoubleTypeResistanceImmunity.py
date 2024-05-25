from Types                import *
from SingleTypeWeakness   import *
from SingleTypeResistance import *
from SingleTypeImmunity   import *

def getDoubleTypeResistanceImmunityAll():
    if not None:
        for type1 in types:
            for type2 in types:
                if type1 == type2:
                    pass
                else:
                    getDoubleTypeResistanceImmunity(type1, type2)

def getDoubleTypeResistanceImmunity(type1, type2):
    type1Weakness        = []
    type2Weakness        = []
    type1Resistance      = []
    type2Resistance      = []
    type1Immunity        = []
    type2Immunity        = []
    doubleTypeImmunity   = []
    doubleTypeResistance = []

    type1Weakness.append   (getSingleTypeWeakness(type1))
    type2Weakness.append   (getSingleTypeWeakness(type2))
    type1Resistance.append (getSingleTypeResistance(type1))
    type2Resistance.append (getSingleTypeResistance(type2))
    type1Immunity.append   (getSingleTypeImmunity(type1))
    type2Immunity.append   (getSingleTypeImmunity(type2))

    if type1Immunity[0][0] == 'None':
        type1Immunity[0].remove('None')
    if type2Immunity[0][0] == 'None':
        type2Immunity[0].remove('None')

    weaknessMergeWeakness   = type1Weakness[0]   + type2Weakness[0]
    weaknessMergeResistance = type1Resistance[0] + type2Resistance[0]
    weaknessMergeImmunity   = type1Immunity[0]   + type2Immunity[0]

    doubleTypeImmunity.append(weaknessMergeImmunity)

    for type in weaknessMergeWeakness:
        if type in weaknessMergeResistance:
            weaknessMergeResistance.remove(type)

    for type in weaknessMergeImmunity:
        if type in weaknessMergeResistance:
            weaknessMergeResistance.remove(type)

    doubleTypeResistance.append(weaknessMergeResistance)

    if not doubleTypeResistance[0]:
        print(f"{type1} + {type2} typing doesn't have any resistances \n")
    else: print(f"{type1} + {type2} typing is resistant against {doubleTypeResistance[0]} types \n")

    if not doubleTypeImmunity[0]:
        print(f"{type1} + {type2} typing doesn't have any immunities \n")
    else: print(f"{type1} + {type2} typing is immune against {doubleTypeImmunity[0]} types")