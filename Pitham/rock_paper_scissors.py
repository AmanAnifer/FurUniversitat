import random
import time
import os

# Index 0 is stone, index 1 is paper, index 2 is scissors
# In this matrix, 1 represents win, 0 tie, -1 lose
# So if user is stone(0) and PC is scissors(2), we check
# versus_matrix[0][2] to get user's win status.
versus_matrix = [[ 0, -1,  1],
                 [ 1,  0, -1],
                 [-1,  1,  0]]

left_ascii = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
 ---.__________)
""",
"""
    _______
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)
"""
]


right_ascii = [
"""
  _______    |
 (____   '---|
(_____)      |
(_____)      |
 (____)      |
  (___)__.---|
""",
"""
      _______     |
 ____(____   '----|
(______           |
(_______          |
 (_______         |
    (_________.---|
""",
"""
       _______    |
  ____(____   '---|
 (______          |
(__________       |
      (____)      |
       (___)__.---|
"""
]

def join_lr_ascii(left, right, middle):
    final_string = ""
    mid_index = int(len(left.split("\n"))/2)    # Where should we print the middle text
    for i, s in enumerate(zip(left.split("\n"), right.split("\n"))):
        mid_text = ""
        if(i == mid_index):
            mid_text = middle;
        final_string += "{:<20}{:^20}{:>20}\n".format(s[0], mid_text, s[1])
    final_string += "{:<20}{:^20}{:>20}\n".format("YOU", "", "COMPUTER")
    return final_string;

def show_animation(user_choice, pc_choice):
    user_init = left_ascii[0]
    pc_init = right_ascii[0]
    user_ascii = left_ascii[user_choice]
    pc_ascii = right_ascii[pc_choice]
    os.system("clear")
    for middle_text in ["STONE", "PAPER", "SCISSOR"]:
        print(join_lr_ascii(user_init, pc_init, middle_text))
        time.sleep(0.75)
        os.system("clear")

    status = versus_matrix[user_choice][pc_choice]
    status_text = ""
    if status == -1:
        status_text = "YOU LOSE :("
    elif status == 0:
        status_text = "IT'S A TIE :|"
    else:
        status_text = "YOU WIN! :D"
    print(join_lr_ascii(user_ascii, pc_ascii, status_text))
    input("Press [Enter] to continue")
    os.system("clear")

while True:
    choice = int(input("""Stone-Paper-Scissor™: Premium Edition
1) Stone
2) Paper
3) Scissor
4) Exit
Select your choice: """))
    if choice == 4:
        print("K thx bye  ᕕ( ᐛ )ᕗ\n")
        break
    elif choice > 4 or choice < 1:
        print("Look before you type, you nincompoop (╯°□°）╯︵ ┻━┻\n")
        continue
    else:
        pc_choice = random.randint(0, 2)
        # Its 0-index based, so choice minus 1
        show_animation(choice-1, pc_choice)

