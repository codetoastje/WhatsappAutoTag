import keyboard as kb
import time


if __name__ == "__main__":
    print("Welcome to Whatsapp AutoTag\n")
    print("Enter the Number of members in your Group excluding yourself : ")
    x = int(input())

    print("Click on the whatsap group chatbox within 10 seconds or else u are doomed")
    time.sleep(10)

    i = 0

    while i!=x:
        j = 0
        kb.press("shift + @")
        kb.release("shift + @")

        while j!=i:
            kb.press("down")
            kb.release("down")
            j+=1

        kb.press("enter")
        kb.release("enter")
        i+=1
        time.sleep(0.2)


