import random
import time
import pyautogui
import webbrowser
comment_list = ["Valuable insights", "Nice post", "This post can feature", "Such a nice post"]

chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab("https://www.linkedin.com/feed/")

if __name__ == '__main__':
    while True:
        try:
            pyautogui.vscroll(-150)
            time.sleep(3)
            locate = pyautogui.center(pyautogui.locateOnScreen("comment.png", confidence=0.6))
            pyautogui.moveTo(locate)
            pyautogui.moveTo(locate)
            time.sleep(3)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(locate.x, locate.y + 50)
            pyautogui.moveTo(locate.x, locate.y + 50)
            time.sleep(4)
            pyautogui.click()
            pyautogui.typewrite(random.choice(comment_list))
            time.sleep(4)
        except:
            continue

''' 
Works fine on 80% resolution 
It's working rn, the post button is not added yet.

'''


