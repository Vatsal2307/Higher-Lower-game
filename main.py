from art import logo
from art import vs
from game_data import data
from replit import clear
import random
print(logo)
score = 0
item_2 = random.choice(data)
game_continues = True


while game_continues:
  def format_acc(item):
    """Takes the data and returns printable format"""
    item_name = item['name']
    item_description = item['description']
    item_country = item['country']
    return f"{item_name}, {item_description} in {item_country}"
  
  
  def compare(fllw_1, fllw_2,guess):
    """Uses if statement to check higher follower count and retrun if the user got it right."""
    if fllw_1 > fllw_2:
      return guess == "a" 
    else:
      return guess == "b"
      
  item_1 = item_2
  item_2 = random.choice(data)
  while item_1 == item_2:
    item_2 = random.choice(data)
  
  fllw_1 = item_1['follower_count']
  fllw_2 = item_2['follower_count']
  
  print(f"A: {format_acc(item_1)}")
  print(vs)
  print(f"B: {format_acc(item_2)}")
  guess = input("Choose A or B: ").lower()
  
  clear()
  print(logo)
  is_correct = compare(fllw_1,fllw_2,guess)
  if is_correct == True:
    print("You are right")
    score += 1
    print(f"Your score is: {score}")
    
  else:
    print("You are wrong")
    print(f"Your final score is: {score}")
    game_continues = False

  
 