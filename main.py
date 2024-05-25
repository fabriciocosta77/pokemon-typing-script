from Types                        import *
from SingleTypeWeakness           import *
from SingleTypeResistance         import *
from SingleTypeImmunity           import *
from DoubleTypeWeakness           import *
from DoubleTypeResistanceImmunity import *

if __name__ == '__main__':
    print("POKÉMON TYPING PYTHON SCRIPT")
    while True:
        print(f"1.  CHECK ALL TYPES "
            f"\n2.  CHECK SINGLE-TYPE WEAKNESSES "
            f"\n3.  CHECK SINGLE-TYPE RESISTANCES "
            f"\n4.  CHECK SINGLE-TYPE IMMUNITIES "
            f"\n5.  CHECK DOUBLE-TYPE WEAKNESSES "
            f"\n6.  CHECK DOUBLE-TYPE RESISTANCES AND IMMUNITIES "
            f"\n7.  CHECK ALL SINGLE-TYPES WEAKNESSES "
            f"\n8.  CHECK ALL SINGLE-TYPES RESISTANCES "
            f"\n9.  CHECK ALL SINGLE-TYPES IMMUNITIES "
            f"\n10. CHECK ALL DOUBLE-TYPES WEAKNESSES "
            f"\n11. CHECK ALL DOUBLE-TYPES RESISTANCES AND IMMUNITIES "
            f"\n12. EXIT SCRIPT ")

        nav = str(input())

        match nav:
            case '1':
                getTypeList()
            case '2':
                type = str(input("Insert type: ")).capitalize()
                printSingleTypeWeakness(type)
            case '3':
                type = str(input("Insert type: ")).capitalize()
                printSingleTypeResistance(type)
            case '4':
                type = str(input("Insert type: ")).capitalize()
                printSingleTypeImmunity(type)
            case '5':
                type1 = str(input("Insert first type: ")).capitalize()
                type2 = str(input("Insert second type: ")).capitalize()
                getDoubleTypeWeakness(type1, type2)
            case '6':
                type1 = str(input("Insert first type: ")).capitalize()
                type2 = str(input("Insert second type: ")).capitalize()
                getDoubleTypeResistanceImmunity(type1, type2)
            case '7':
                getSingleTypeWeaknessAll()
            case '8':
                getSingleTypeResistanceAll()
            case '9':
                getSingleTypeImmunityAll()
            case '10':
                getDoubleTypeWeaknessAll()
            case '11':
                getDoubleTypeResistanceImmunityAll()
            case '12':
                print("Exiting script")
                break
            case _:
                print("Wrong input!")