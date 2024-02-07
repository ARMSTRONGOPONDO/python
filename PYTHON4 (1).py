class Temperature:
    def __init__(self):
        # You can initialize any attributes or variables here if needed
        pass

    def convert_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

    def convert_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")

# Create an object of the Temperature class
temperature_obj = Temperature()

# Access the two methods using the dot operator
temperature_obj.convert_to_fahrenheit(30)
temperature_obj.convert_to_celsius(86)