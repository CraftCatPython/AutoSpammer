import pyautogui,time
print("Enter The Word You Want To Spam")
Word = input("")
time.sleep(5)
while True:
  pyautogui.typewrite(Word)
  time.sleep(0.100)
  pyautogui.press("enter")
