from Types                import *
from SingleTypeWeakness   import *
from SingleTypeResistance import *

def getDoubleTypeWeaknessAll():
    if not None:
        for type1 in types:
            for type2 in types:
                if type1 == type2:
                    pass
                else:
                    getDoubleTypeWeakness(type1, type2)

def getDoubleTypeWeakness(type1, type2):
    type1Weakness      = []
    type2Weakness      = []
    type1Resistance    = []
    type2Resistance    = []
    type1Immunity      = []
    type2Immunity      = []
    doubleTypeWeakness = []

    type1Weakness.append   (getSingleTypeWeakness(type1))
    type2Weakness.append   (getSingleTypeWeakness(type2))
    type1Resistance.append (getSingleTypeResistance(type1))
    type2Resistance.append (getSingleTypeResistance(type2))
    type1Immunity.append   (getSingleTypeImmunity(type1))
    type2Immunity.append   (getSingleTypeImmunity(type2))

    weaknessMergeWeakness   = type1Weakness[0]   + type2Weakness[0]
    weaknessMergeResistance = type1Resistance[0] + type2Resistance[0]
    weaknessMergeImmunity   = type1Immunity[0]   + type2Immunity[0]

    for type in weaknessMergeResistance:
        if type in weaknessMergeWeakness:
            weaknessMergeWeakness.remove(type)

    for type in weaknessMergeImmunity:
        if type in weaknessMergeWeakness:
            weaknessMergeWeakness.remove(type)

    doubleTypeWeakness.append(weaknessMergeWeakness)

    print(f"{type1} + {type2} typing is weak against {doubleTypeWeakness[0]} types \n")