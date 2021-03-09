# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 03:41:10 2020

@author: kwame
"""

# Write your code here
amount_of_water = 400
amount_of_milk = 540
amount_of_coffee_beans = 120
No_of_cups = 9
money = 550
def buy():
    global amount_of_water
    global amount_of_milk
    global amount_of_coffee_beans
    global No_of_cups
    global money
    action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if action == "1":
        amount_of_water = amount_of_water - 250
        amount_of_coffee_beans = amount_of_coffee_beans - 16
        money = money + 4
        No_of_cups = No_of_cups - 1 
    elif action == "2":
        amount_of_water = amount_of_water - 350
        amount_of_coffee_beans = amount_of_coffee_beans - 20
        amount_of_milk = amount_of_milk - 75
        money = money + 7
        No_of_cups = No_of_cups - 1  
    elif action == "3":
        amount_of_water = amount_of_water - 200
        amount_of_coffee_beans = amount_of_coffee_beans - 12
        amount_of_milk = amount_of_milk - 100
        money = money + 6
        No_of_cups = No_of_cups - 1
    message = print("The coffee machine has:\n" + str(amount_of_water) + " of water\n" + str(amount_of_milk) + " of milk\n"
    + str(amount_of_coffee_beans) + " of cofffee beans\n" + str(No_of_cups) + " of disposable cup\n" + str(money) + " of money")
    return message
                
def fill():
    water = int( input("Write how many ml of water do you want to add: ")) + 400
    milk = int(input("Write how many ml of milk do you want to add: ")) + 540
    coffee_bean = int(input("Write how many grams of coffee beans do you want to add: ")) +120
    cups = int(input("Write how many disposable cups of coffee do you want to add: ")) + 9
    message = print("The coffee machine has:\n" + str(water) + " of water\n" + str(milk) + " of milk\n"
    + str(coffee_bean) + " of cofffee beans\n" + str(cups) + " of disposable cup\n" + str(money) + " of money")
    return message  
def take():
    global money
    print("I gave you $" + str(money))
    money = 0
    message = print("The coffee machine has:\n" + str(amount_of_water) + " of water\n" + str(amount_of_milk) + " of milk\n"
    + str(amount_of_coffee_beans) + " of cofffee beans\n" + str(No_of_cups) + " of disposable cup\n" + str(money) + " of money")
    return message         
def main():
    print("The coffee machine has:\n" + str(amount_of_water) + " of water\n" + str(amount_of_milk) + " of milk\n"
    + str(amount_of_coffee_beans) + " of cofffee beans\n" + str(No_of_cups) + " of disposable cup\n" + str(money) + " of money")
    action = input("Write action (buy, fill, take): ")
    if action == "buy":
       buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    else:
        action
if __name__ == '__main__': main()