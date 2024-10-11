import os
os.system('cls')

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
            elif actionSelect == 2:
                actionSelect = "remove"
            elif actionSelect == 3:
                actionSelect = "toggle"
            os.system('cls')
            
            targetList = [1,2]
            targetListWithInput = [3]
            targetSelect = 0
            print("Target:")
            print("1. (Self) Target yourself")
            print("2. (Target) Target your designated target")
            print("3. (Firstname Lastname or Firstname Lastname@Homewold) Selects your specified character. Attach @homeworld if you want to specify where they're from.\n")
            while targetSelect not in targetList:
                targetSelect = int(input("Enter a number: "))
                if targetSelect in targetList:
                    if targetSelect == 1:
                        targetSelect = "self"
                    elif targetSelect == 2:
                        targetSelect = "target"
                    os.system('cls')
                elif targetSelect in targetListWithInput:
                    targetSelectWithInput = input("Enter your target's name (w/ @homeworld example: Thancred Waters@Behemoth): \n")
                    os.system('cls')
                    
                    elementList = [1,2,3]
                    elementSelect = 0
                    print("Element:")
                    print("1. (Moodle) Specifies that this command applies to Moodles.")
                    print("2. (Preset) Specifies that this command applies to Presets.")
                    print("3. (Automation) Specifies that this command applies to Automations.\n")
                    while elementSelect not in elementList:
                        elementSelect = int(input("Enter a number: "))
                        if elementSelect in elementList:
                            if elementSelect == 1:
                                elementSelect = "moodle"
                            elif elementSelect == 2:
                                elementSelect = "preset"
                            elif elementSelect == 3:
                                elementSelect = "automation"
                            os.system('cls')
                            
                            print("1. (GUID) The GUID of the element you want target.")
                            print("2. (Preset) The EXACT name of the element you want to target.\n")
                            elementNameSelect = input("Put in the exact name or GUID of the element you wish to apply: \n")
                            os.system('cls')
                                    
                            if targetSelect in targetListWithInput:
                                print(f"/moodle {actionSelect} \"{targetSelectWithInput}\" {elementSelect} \"{elementNameSelect}\"")
                            else:
                                print(f"/moodle {actionSelect} {targetSelect} {elementSelect} \"{elementNameSelect}\"")
                            print("Don't forget to copy this code!\n")
                            print("Do you want to make another command?\nType Yes or 1 if yes, type anything else if not.")
                            repetitionDeciderList = ["Yes", "yes", "YES", "1"]
                            repetitionDecider = str(input(" "))
                            if repetitionDecider in repetitionDeciderList:
                                creationMode()
                            else:
                                exit()
            
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
