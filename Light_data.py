import serial
import matplotlib.pyplot as plt
import threading

arduino = serial.Serial("COM3", 9600)
datasheet = "sheet.txt"

Green = 0
Yellow = 0
Red = 0
Buzzer = 0

def repeat():
            print("The current count of green light presses is: ", Green)
            print("The current count of yellow light presses is: ", Yellow)
            print("The current count of red light presses is: ", Red)
            print("The current count of buzzer presses is: ", Buzzer)
            print("")

def save_counts():
    with open(datasheet, "w") as file:
        file.write(f"Green: {Green}\n")
        file.write(f"Yellow: {Yellow}\n")
        file.write(f"Red: {Red}\n")
        file.write(f"Buzzer: {Buzzer}\n")


def read_arduino():
    global Green, Yellow, Red, Buzzer
    while True:
        data = arduino.readline().decode().strip()

        if data == "G_PRESS":
            Green += 1
        
        elif data == "Y_PRESS":
            Yellow += 1

        elif data == "R_PRESS":
            Red += 1

        elif data == "BUZZER":
            Buzzer += 1

def load_counts():
    global Green, Yellow, Red, Buzzer

    try:
        with open(datasheet, "r") as file:
            for line in file:
                if line.startswith("Green:"):
                    Green = int(line.split(":")[1])

                elif line.startswith("Yellow:"):
                    Yellow = int(line.split(":")[1])

                elif line.startswith("Red:"):
                    Red = int(line.split(":")[1])

                elif line.startswith("Buzzer:"):
                    Buzzer = int(line.split(":")[1])
    except:
        Green = Yellow = Red = Buzzer = 0

load_counts()

threading.Thread(target=read_arduino, daemon=True).start()

                          
while True:
    print("Hello, this is my first ever arduino project")
    print("Please select the options below to continue:")
    print("1. datasheet")
    print("2. chart graph")
    print("3. Clear all data")
    print("4. exit")
    user = input("Enter your choice (1-4):\n ")

    if user == "1":
        print("This is the datasheet of the project:")
        repeat()                
        
    elif user == "2":

        labels = ["Green", "Yellow", "Red", "Buzzer"]
        values = [Green, Yellow, Red, Buzzer]

        plt.bar(labels, values)

        plt.title("Button Press Counts")
        plt.xlabel("Light")
        plt.ylabel("Count")

        plt.show()

    elif user == "3":
            Green = 0
            Yellow = 0
            Red = 0
            Buzzer = 0
            save_counts()
            print("All data has been cleared.\n")

    elif user == "4":
        save_counts()
        print("Exiting the program. Goodbye!\n")
        break

    else:   
        print("Invalid choice. Please enter a number between 1 and 4.\n")