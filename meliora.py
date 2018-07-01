#!/usr/bin/env python3.6
#----------------------------------------
#Return Multiples in Python
#Author: Joseph Skrzysowski
#Date 6-29-18
#Python3.6 env
#sudo chmod +x maliora.py
#./tic_tac_toe.py
#----------------------------------------

"""
  1) Write program that counts from 1- 50
  2) on multiple of 3 print nursing
  3) on multiple of 7 print Meliora
  4) on multiple of both print Nursing Meliora
  5) if the number is neither a multiple of 3 or 7 print only the number
"""

multiples_of_three = 0
multiples_of_5 = 0
multiples_of_7 = 0
for number in range(50):
    if number % 3 == 0:
        multiples_of_3 = number
        print ('Nursing')
    elif number % 5 == 0:
        multiples_of_5 = number
        print ('Meliora')
    elif number % 7 == 0:
        multiples_of_7 = number
        print ('Nursing Meliora')
    else:
        print (number)
