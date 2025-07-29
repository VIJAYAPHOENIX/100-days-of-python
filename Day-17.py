# # from configparser import DuplicateSectionError
# #
# #
# class User:
#
#      def __init__(self,user_id,username):
#          self.id = user_id
#          self.username = username
#          self.followers = 0
#          self.following = 0
#
#      def follow(self,user):
#
#         user.followers += 1
#         self.following += 1
#
# user1 = User("001","Vijay")
#
# user_2 = User("002","Durga")
# print(user1.username,user_2.username)
#
# user1.follow(user_2)
# print(user1.following)
# print(user1.followers)
# print(user_2.followers)
# print(user_2.following)
#
# # MINI PROJECT
#
#
class BankAccount:

    def __init__(self,username,amount):
        self.username = username
        self.balance = amount

    def deposit_money(self,amount):
        self.balance += amount

    def withdraw_money(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("insufficient balance")

    def display_info(self):
        print(f"{self.username} has {self.balance} balance in the account")

client1 = BankAccount("vijay", 40000)
client2 = BankAccount("durga", 40000)

account = client1
account.deposit_money(60000)
account.withdraw_money(10000)
account.display_info()
print(account)