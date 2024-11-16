# import random
# from django.core.management.base import BaseCommand
# from api.models import Customer, Product, StockInventory, DailyLubeSales
# from faker import Faker
# from django.contrib.auth.models import User


# fake = Faker("en_IN")

# COUNT = 100


# class Command(BaseCommand):
#     help = "Ingests random records"

#     def truncate_tables(self):
#         Customer.objects.all().delete()
#         Product.objects.all().delete()
#         self.stdout.write(self.style.SUCCESS("Successfully truncated Product table"))

#     def get_user(self):
#         users = User.objects.filter(is_staff=True)
#         return random.choice(users)

#     def create_customers(self):
#         for _ in range(COUNT):
#             Customer.objects.create(
#                 name=fake.name(),
#                 email=fake.email(),
#                 address=fake.address(),
#                 phone_number=fake.phone_number(),
#                 user=self.get_user(),
#             )

#         self.stdout.write(self.style.SUCCESS(f"Successfully created {COUNT} customers"))

#     def create_products(self):
#         for _ in range(COUNT):
#             Product.objects.create(
#                 code=fake.unique.random_number(digits=10),
#                 name=fake.word(),
#                 is_fuel=fake.boolean(chance_of_getting_true=50),
#                 price=fake.random_number(digits=4),
#                 user=self.get_user(),
#             )

#         self.stdout.write(self.style.SUCCESS(f"Successfully created {COUNT} products"))
    
#     def create_stock_inventory(self):
#         products = Product.objects.all()
#         for _ in range(COUNT):
#             StockInventory.objects.create(
#                 product=random.choice(products),
#                 quantity=fake.random_number(digits=3),
#                 date=fake.date_this_year(),
#                 user=self.get_user(),
#             )

#         self.stdout.write(self.style.SUCCESS(f"Successfully created {COUNT} stock inventory records"))
 
#     def create_daily_lube_sales(self):
#         products = Product.objects.all()
#         for _ in range(COUNT):
#             DailyLubeSales.objects.create(
#                 product=random.choice(products),
#                 quantity=fake.random_number(digits=2),
#                 date=fake.date_this_year(),
#                 user=self.get_user(),
#             )

#         self.stdout.write(self.style.SUCCESS(f"Successfully created {COUNT} daily lube sales records"))

#     def handle(self, *args, **kwargs):
#         pass
#         # self.truncate_tables()
#         # self.create_customers()
#         # self.create_products()
#         # self.create_stock_inventory()
#         # self.create_daily_lube_sales()