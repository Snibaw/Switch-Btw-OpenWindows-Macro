from pynput.keyboard import Key, Controller
import keyboard
import time
windowsList = [1,2,3]
isKeyPressed = 0
KeyPressed = 0
homeKey = 'Alt'
stopKey = 'AltGr'
k = Controller()

def ChangeWindow(i, windowsList):
    print(windowsList)
    k.press(Key.alt)
    k.press(Key.tab)
    for _ in range(windowsList[1::].index(i)):
        time.sleep(0.01)
        k.press(Key.tab)
        k.release(Key.tab)
    time.sleep(0.01)
    k.release(Key.tab)
    k.release(Key.alt)
    windowsList.pop(windowsList[1::].index(i)+1)
    return [i] + windowsList
    
while True:
    if(keyboard.is_pressed(stopKey)):
        break
    if(isKeyPressed == 0):
        for i in windowsList[1::]:
            if(keyboard.is_pressed(str(i))): #keyboard.is_pressed(homeKey) and&é
                isKeyPressed = 1
                KeyPressed = str(i)
                print(i)
                windowsList = ChangeWindow(i, windowsList)
                print(windowsList)
                break
    else:
        if(keyboard.is_pressed(KeyPressed) == 0):
            isKeyPressed = 0
    
        
