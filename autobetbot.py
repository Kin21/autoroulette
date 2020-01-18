import pyautogui
import json
import msvcrt


def coords_init():
    with open("config.json",'r') as config_file: ## Main json file with all necessary info
        config = json.load(config_file)
    current_key = 's'
    bad_keys_num = 0
    while current_key != b'q':
        current_key = msvcrt.getch()
        current_key.lower()
        if current_key == b'r':
            config["coords"]["red"] = pyautogui.position()
            print("Red coords had successfully set!")
        elif current_key == b'g':
            config["coords"]["green"] = pyautogui.position()
            print("Green coords had successfully set!")
        elif current_key == b'b':
            config["coords"]["black"] = pyautogui.position()
            print("Black coords had successfully set!")
        elif current_key == b'i':
            config["coords"]["item"] = pyautogui.position()
            print("Item coords had successfully set!")
        elif current_key == b'l':
            config["coords"]["betline"] = pyautogui.position()
            print("Betline coords had successfully set!")
        else:
            if bad_keys_num >= 5:
                print("Press key to set coords:\nr/g/b to set color\ni to Item\nl(L) to betline")
                bad_keys_num = 0
            else:
                 bad_keys_num += 1
    with open("config.json", "w") as config_file:
        json.dump(config , config_file,sort_keys=True, indent=4)

def make_bet(bet,color):
    with open("config.json",'r') as config_file:
        config = json.load(config_file)
    pyautogui.doubleClick(config["coords"]["betline"])
    pyautogui.write(str(bet), interval=0.1)
    x,y = config["coords"][color]
    pyautogui.click(x, y, duration = 0.2)


def sell_item():
    with open("config.json",'r') as config_file:
        config = json.load(config_file)
    x,y = config["coords"]["item"]
    pyautogui.click(x, y, duration = 0.2)
    pyautogui.click(x, y-50, duration = 0.2)

def test_coord():
    with open("config.json",'r') as config_file:
        config = json.load(config_file)
    for section in config["coords"]:
        x,y = config["coords"][section]
        pyautogui.moveTo(x, y, 2, pyautogui.easeInQuad)



coords_init()
