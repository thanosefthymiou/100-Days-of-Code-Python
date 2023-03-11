#Thanos Efthymiou March 2023
import os
from alpha import az
from art import logo

while True:
  print(logo)
  #-------record action---------- 
  action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  
  while action != 'encode' and action != 'decode':
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  #----------------------------
  
  message = input("Type your message: ")
  message = message.lower()
  shift = int(input("Type the shift number: "))
  if shift > 26:
    shift = shift % 26

  result = ""
  if action == 'encode':
    for i in range (0,len(message)):
      result += az[az.index(message[i])+ shift]
  else:
    for i in range (27,27+len(message)):
      result += az[az.index(message[i-27])- shift]
      
  print(result)
    
  repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")

  if repeat == 'no':
    break
  os.system("clear")
