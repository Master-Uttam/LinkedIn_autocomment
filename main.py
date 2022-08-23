import random
import time
import pyautogui
import webbrowser

comment_list = ["Valuable insights", "Nice post", "This post can feature", "Such a nice post"]


def launch():
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab("https://www.linkedin.com/feed/")


def comment(ncomments):
    n = 0
    launch()
    while int(ncomments) > n:
        try:
            pyautogui.vscroll(-150)
            time.sleep(3)
            locate = pyautogui.center(pyautogui.locateOnScreen("comment.png", confidence=0.6))
            time.sleep(2)
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
            pyautogui.locateOnScreen("post.png")
            post = pyautogui.center(pyautogui.locateOnScreen("post.png"))
            pyautogui.moveTo(post)
            time.sleep(4)
            pyautogui.click()
            time.sleep(4)
            n = + 1
        except:
            time.sleep(3)
            continue


def likes(nlikes):
    t = 0
    launch()
    while int(nlikes) > t:
        try:
            pyautogui.vscroll(-150)
            time.sleep(3)
            like = pyautogui.center(pyautogui.locateOnScreen("like.png"))
            time.sleep(2)
            pyautogui.moveTo(like)
            time.sleep(2)
            pyautogui.click()
            t = + 1
            time.sleep(4)

        except:
            time.sleep(2)
            pass


if __name__ == '__main__':
    t = 0
    n = 0
    d = int(input("Enter the number of likes\t"))
    c = int(input("Enter the number of comments\t"))

    likes(d)
    comment(c)
    print(f"Thanks! {d} Likes and {c} Comments are done.")

''' 
Works fine on 80% resolution 
It's working rn, the post button is not added yet.

'''
