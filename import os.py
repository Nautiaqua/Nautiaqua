import os
os.system('cls')

# /moodle apply self moodle "Fluffy"

def creationMode():
    actionList = [1,2,3]
    actionSelect = 0
    print("Actions:")
    print("1. (Apply) Applies the specified element to the specified target selector.")
    print("2. (Remove) Removes the specified element to the specified target selector.")
    print("3. (Toggle) Toggles the specified element to the specified target selector.\n")
    while actionSelect not in actionList:
        actionSelect = int(input("Enter a number: "))
        if actionSelect in actionList:
            if actionSelect == 1:
                actionSelect = "apply"
            if actionSelect == 2:
                actionSelect = "apply"
            if actionSelect == 3:
                actionSelect = "apply"
            if actionSelect == 4:
                actionSelect = "apply"
            os.system('cls')
            targetList = [1,2,3,4]
            targetSelect = 0
            print("Target:")
            print("1. (Self) Target yourself")
            print("2. (Target) Target your designated target")
            print("3. (Firstname Lastname) Selects your specified character as the designated target.")
            print("4. (Firstname Lastname@Homeworld) Selects your specified character with the given homeworld as the designated target.\n")
            while targetSelect not in targetList:
                targetSelect = int(input("Enter a number: "))
                if targetSelect in targetList:
                    os.system('cls')
                    elementList = [1,2,3]
                    elementSelect = 0
                    print("Element:")
                    print("1. (Moodle) Specifies that this command applies to Moodles.")
                    print("2. (Preset) Specifies that this command applies to Presets.")
                    print("3. (Automation) Specifies that this command applies to Automations.")
                    while elementSelect not in elementList:
                        elementSelect = int(input("Enter a number: "))
                        if elementSelect in elementList:
                            os.system('cls')
                            elementNameList = [1,2,3]
                            elementNameSelect = 0
                            print("1. (GUID) The GUID of the element you want target.")
                            print("2. (Preset) The EXACT name of the element you want to target.")
                            while elementNameSelect not in elementNameList:
                                elementNameSelect = int(input("Enter a number: "))
                                if elementNameSelect in elementNameList:
                                    os.system('cls')
                                    if targetSelect == 2 or targetSelect == 3:
                                        print(f"/moodle {actionSelect} \"{targetSelect}\" {elementSelect} \"{elementNameSelect}\"")
                                    else:
                                        print(f"/moodle {actionSelect} {targetSelect} {elementSelect} \"{elementNameSelect}\"")
                            
            
def mainMenu():
    selectorList = ["start", "START"]
    selector = "false"
    print("Moodles Command Helper")
    # /moodle apply self moodle "Fluffy"
    print("Type START for a new command\n")
    while selector not in selectorList:
        selector = input("")
        if selector == "START" or selector == "start":
            os.system('cls')
            creationMode()
        
    
    
mainMenu()
    