#TempConvert.py
#Name:Riley Mayfield
#Date:2/3
#Assignment:Lab 3
#Purpose: convert F to C

def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = input("What's the tempurature in Fahrenheit? :")
  tempF = int(tempF)
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempC = (tempF-32)*5/9
  tempC = round(tempC,1)
  print(tempF, "degrees Fahrenheit is ", tempC, "degrees Celsius.")
if __name__ == '__main__':
  main()
