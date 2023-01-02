#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import numpy as np
import random 

def display_menu():
    """display menu"""
    print()
    print('Input your last name, birthmonth, favorite animal, and favorite color to get a strong password!')

def PasswordGenerator():
    """Main user interaction loop"""
    while True:
        display_menu()
        desired_length = int(input('Enter your desired password length: '))
        if desired_length < 0:
            print('Please enter a valid length greater than zero')
            break
        lastname = str(input('Enter your last name: '))
        if lastname[0].isupper() == False:
            print('Please enter your last name with the first letter capitalized')
            break
        birthmonth = str(input('Enter your birthmonth: '))
        if birthmonth[0].isupper() == False:
            print('Please enter your birthmonth with the first letter capitalized')
            break
        favorite_animal = str(input('Enter your favorite animal: '))
        if favorite_animal[0].isupper() == False:
            print('Please enter your favorite animal with the first letter capitalized')
            break
        favorite_color = input('Enter your favorite color: ')
        if favorite_color[0].isupper() == False:
            print('Please enter your favorite color with the first letter capitalized')
            break
        password = Password(lastname,birthmonth,favorite_animal,favorite_color)
        print('Here is your strong password! --> ' + password.create_password(desired_length))
        break
    
    
class Password:
    """creates a random strong password from a your last name, birthmonth, favorite animal, and favorite color
    implement a uniqueness feature?
    implement something that checks if the parameters are correct
    implement an interface
    Maybe add parameters to each password? Like if you want numbers, strings, symbols"""
    def __init__(self, lastname, birthmonth, animal, color):
        self.lastname = lastname
        self.birthmonth = birthmonth
        self.animal = animal
        self.color = color
        
    
    def __str__(self):
        return 'Your last name is: ' + str(self.lastname) + \
    '\nYour birthmonth is: ' + str(self.birthmonth) + \
        '\nYour favorite animal is: ' + str(self.animal) + \
            '\nYour favorite color is: ' + str(self.color)
        
    def manipulate_lastname(self):
        """manipulates the last name string into a scrambled string"""
        name = self.lastname
        step1 = list(name)
        random.shuffle(step1)
        step2 = ''.join(step1)
        return step2
    
    def manipulate_birthmonth(self):
        """Manipulates the birthmonth string into a string of numbers"""
        string = ''
        random_number = random.randint(0,100)
        for x in range(len(self.birthmonth)):
            string += str(ord(self.birthmonth[x]) - random_number)
        return string
    
    def manipulate_animal(self):
        """Manipulates the animal string into a string of symbols"""
        string = ''
        for x in range(len(self.animal)):
            placeholder = False
            while placeholder == False:
                randominteger = random.randint(1,30)
                symbol = str(chr(ord(self.animal[x]) - randominteger))
                if symbol in '!@#$%^&*()-_+=[{]}\|/<,>.?/;:~`':
                    placeholder = True
                    string += symbol
        return string

    def manipulate_color(self):
        """Manipulates the color string into a string of uppercase letters"""
        string = list(self.color.upper())
        random.shuffle(string)
        string = ''.join(string)
        return string
    
    def create_password_base(self, desired_size):
        """Creates a list of lists that is the password base based on the parameters, of a desired length > 4"""
        if desired_size < 4:
            print('Length of password must be larger than four characters')
            return
        lowerletters = self.manipulate_lastname()
        upperletters = self.manipulate_color()
        numbers = self.manipulate_birthmonth()
        symbols = self.manipulate_animal()
        listvar = [[]] * desired_size
        random_number = random.randint(0,desired_size-1)
        listvar[random_number] = str(lowerletters[random.randint(0,len(lowerletters)-1)])
        random_number2 = random.randint(0,desired_size-1)
        if random_number2 == random_number:
            while random_number2 == random_number:
                random_number2 = random.randint(0,desired_size-1)
        listvar[random_number2] = str(upperletters[random.randint(0,len(upperletters)-1)])
        random_number3 = random.randint(0,desired_size-1)
        if random_number3 == random_number or random_number3 == random_number2:
            while random_number2 == random_number or random_number3 == random_number2:
                random_number3 = random.randint(0,desired_size-1)
        listvar[random_number3] = str(numbers[random.randint(0,len(numbers)-1)])
        random_number4 = random.randint(0,desired_size-1)
        if random_number4 == random_number or random_number4 == random_number2 or random_number4 == random_number3:
            while random_number2 == random_number or random_number3 == random_number2 or random_number4 == random_number3:
                random_number4 = random.randint(0,desired_size-1)
        listvar[random_number4] = str(symbols[random.randint(0,len(symbols)-1)])
        return listvar
        
    def create_password(self, desired_size):
        """fills in the password base"""
        password = ''
        base = self.create_password_base(desired_size - 1)
        lowerletters = self.manipulate_lastname()
        upperletters = self.manipulate_color()
        numbers = self.manipulate_birthmonth()
        symbols = self.manipulate_animal()
        for x in range(len(base)):
            if base[x] == []:
                number = random.randint(1,4)
                if number == 1:
                    base[x] = str(lowerletters[random.randint(0,len(lowerletters)-1)])
                if number == 2:
                    base[x] = str(upperletters[random.randint(0,len(upperletters)-1)])
                if number == 3:
                    base[x] = str(numbers[random.randint(0,len(numbers)-1)])
                if number == 4:
                    base[x] = str(symbols[random.randint(0,len(symbols)-1)])
        for i in range(len(base)):
            password += base[i]
        return password
        
        
        
