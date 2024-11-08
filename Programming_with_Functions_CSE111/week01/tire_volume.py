import math
import datetime

def calculate_tire_volume():
	w = int(input("Enter the width of the tire in millimeters: "))
	a = int(input("Enter the aspect ratio of the tire: "))
	d = int(input("Enter the diameter of the wheel in inches: "))

	v = math.pi * (w ** 2) * (a / 100) * ((a / 100) + 2540) / (10000000000)
	print(f"The volume of space inside the tire is: {v:.2f} liters")

	current_date = datetime.datetime.now().strftime("%Y-%m-%d")
	with open("volumes.txt", "a") as file:
		file.write(f"{current_date},{w},{a},{d},{v:.2f}\n")

if __name__ == "__main__":
	calculate_tire_volume()
