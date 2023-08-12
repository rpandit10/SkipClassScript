import pyautogui
import time

# open google chrome
time.sleep(1)

pyautogui.hotkey('command','command')
pyautogui.hotkey('command', 'space')
time.sleep(1)
pyautogui.write('google chrome', interval=.1)
time.sleep(0.5)
pyautogui.press('enter')

# opens email
time.sleep(3)
pyautogui.hotkey('command','t')
time.sleep(.5)
pyautogui.write('mail.google.com', interval=.1)
time.sleep(.5)
pyautogui.press('enter')
time.sleep(7)
pyautogui.click(150,250)
time.sleep(.5)

# writes email
pyautogui.press('tab')
pyautogui.write('Class Absence Tomorrow')
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('Dear Professor, ')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.write('I hope this email finds you well. I would like to let you know '
                'that I can not attend class tomorrow due to unforeseen'
                ' health circumstances. I am not feeling well and think it is '
                'best for me to take a day to rest and recover ')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.write('I understand how important the class material is, and I will make sure to '
                'catch up on any missed content or assignments. If there are any important'
                ' materials or announcements from class tomorrow, I would really appreciate it if'
                ' you could share those with me')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.write('Thank you so much for your understanding, and I apologize for any inconvenience'
                ' this may cause. I hope to be back in your class soon')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.write('Thank you again, ')
pyautogui.press('enter')
pyautogui.write('Raunak Pandit')

# returns user to subject line to input professor name
n = 0
while (n < 15):
    pyautogui.press('tab')
    n = n + 1



