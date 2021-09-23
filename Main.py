# Make a class named Restaurant. The __init__()
# method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type. Make a
# method named describe_restaurant() that prints these
# two pieces of information, and a method named
# open_restaurant() that prints a message indicating
# that the restaurant is open.

# Make an instance named restaurant from your class.
# Print the two attributes individually, and then call
# both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurant = Restaurant("Healthy Eating", "healthy food")

restaurant.describe_restaurant()
restaurant.open_restaurant()
