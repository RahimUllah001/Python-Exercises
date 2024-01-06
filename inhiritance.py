
class chef:
    def make_chicken(self):
        print("chef can make chicken")

    def make_salad(self):
        print("chef can make salad")

    def make_special_dish(self):
        print("chef can make special  bbq")


class chineese_chef(chef):
    def make_fried_rice(self):
        print("chineese can make fried rice")

    def make_special_dish(self):
        print("chineense can make special orange chicken")  




my_chef = chef()
my_chineese_chef = chineese_chef()

my_chef.make_chicken()

my_chineese_chef.make_fried_rice()
my_chineese_chef.make_chicken()
my_chef.make_special_dish()
my_chineese_chef.make_special_dish()
