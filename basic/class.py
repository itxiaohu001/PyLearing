# 类
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        # 属性
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # 方法
    def describe_restaurant(self):
        print(self.restaruant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("open restaurant")


restaurant_cs = Restaurant("csrest", "china")
restaurant_cs.describe_restaurant()
restaurant_cs.open_restaurant()


# 继承
class Hotel(Restaurant):
    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)

    def eat_lunch(self):
        print("eat beef")

    # 重写父类
    def open_restaurant(self):
        print("open hotel")


hotel_cs = Hotel("cshotel", "japan")
hotel_cs.describe_restaurant()
hotel_cs.eat_lunch()
hotel_cs.open_restaurant()
