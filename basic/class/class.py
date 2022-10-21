class Restaurant:
    def __init__(self,restaurant_name,cuisine_type) -> None:
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaruant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("open restaurant")

restaurant_cs = Restaurant("csrest","fish")
restaurant_cs.describe_restaurant()
restaurant_cs.open_restaurant()
