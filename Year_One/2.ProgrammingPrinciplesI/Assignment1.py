# Assignment One - MetricConversion

def main():
    name = input("Enter your Name: ")
    height = input("Enter Height in inches: ")
    weight = input("Enter Weight in pounds: ")
    print()
    print("Metric Calculation")
    print("Name: " + name)
    print("Height:", convertInchToMeter(height), "meters")
    print("Weight:", convertPoundsToKilos(weight), "kilograms")

def convertInchToMeter(value):
    return float(value) * 0.0254

def convertPoundsToKilos(value):
    return float(value) * 0.4535

if __name__ == "__main__":
    main()