import json
import requests
import time


base_history_url = "https://www.wtfskins.com/api/v1/rouletteroundhistory/?limit=50&offset="
num_of_history_pages = 25


def get_jsons_history():
    for i in range(0,num_of_history_pages):
        r = requests.get(base_history_url+str(i*50))
        with open('history/Roulette_hisory'+str(i)+".json", 'w') as output_file:
            output_file.write(r.text)
        time.sleep(0.4)
        print("In process: " + str((100*i)/num_of_history_pages)+"%")
    print("Ready: 100%")


def console_analysis():
    longest_no_red = 0    ##Value of the longest line when some color doesn`t drop
    longest_no_black = 0

    longest_red = 0       ##Value of the longest line with same color
    longest_black = 0

    num_black = 0
    num_red = 0       # Number of dropped color
    num_green = 0

    temp_no_red = 0
    temp_no_black = 0
    temp_red = 0     # Temp values to find the longest line
    temp_black = 0
    temp_snake = 0

    snake_line = 0 # The longest line where no same color that repeated


    for i in range(0,num_of_history_pages):
        with open('history/Roulette_hisory'+str(i)+".json", "r") as read_file:
            data = json.load(read_file)
        for session in data["response"]["data"]:
            color = int(session["outcome"])
            if color >= 1 and color <= 7:    # 1 <= RED <= 7
                
                num_red += 1
                temp_red += 1
                temp_no_black += 1
                if temp_no_red > longest_no_red:
                    longest_no_red = temp_no_red
                temp_no_red= 0
                if temp_black > longest_black:
                    longest_black = temp_black
                temp_black = 0
            elif color >= 8 and color <= 14:  # Black
                num_black += 1
                temp_no_red += 1
                temp_black += 1
                if temp_no_black > longest_no_black:
                    longest_no_black = temp_no_black
                temp_no_black = 0
                if temp_red > longest_red:
                    longest_red = temp_red
                temp_red = 0
            elif color == 0:      #Green
                num_green += 1
                temp_no_red += 1
                temp_no_black += 1
                if temp_red > longest_red:
                    longest_red = temp_red
                temp_red = 0
                if temp_black > longest_black:
                    longest_black = temp_black
                temp_black = 0
    print("Total items: " + str(num_red+num_green+num_black))
    print("Red items: " + str(num_red) + " - " + str((num_red)/(num_red+num_green+num_black) * 100) + "%")
    print("Black items: " + str(num_black)+ " - " + str((num_black)/(num_red+num_green+num_black) * 100) + "%")
    print("Green items: " + str(num_green)+ " - " + str((num_green)/(num_red+num_green+num_black) * 100) + "%")
    print("The longest red line: " + str(longest_red))
    print("The longest black line: " + str(longest_black))
    print("The longest NOred items: " + str(longest_no_red))
    print("The longest NOblack items: " + str(longest_no_black))

console_analysis()
