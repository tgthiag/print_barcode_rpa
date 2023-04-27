import pyautogui
import cv2
import time

def findWindow():
    try :
        pyautogui.getWindowsWithTitle("barcodes_logistica")[0].minimize()
        pyautogui.getWindowsWithTitle("barcodes_logistica")[0].maximize()
    except: 
        print("Mantenha o aplicativo de códigos de barras aberto antes de executar")
        input('Digite qualquer tecla para fechar.')
        
def clickPrint():
    printBt = pyautogui.locateOnScreen('print.png', grayscale= True, confidence=0.5)
    pyautogui.click(printBt)

def writeAndPrint(street, position):
    time.sleep(1)
    myText = street + position
    buttonx, buttony = pyautogui.locateCenterOnScreen('print.png', grayscale= True, confidence=0.5)
    textBox = pyautogui.moveTo(buttonx, buttony -71)
    pyautogui.doubleClick(textBox)
    pyautogui.write(str(myText), interval=0.35)

    pyautogui.press('enter')
    clickPrint()
    time.sleep(1)
    pyautogui.press('enter')

whatStreet = input("Qual a rua? ")
starting = input("Por qual número começaremos a imprimir? ")
ending = input("Iremos imprimir até qual número? ")

findWindow()
time.sleep(1)
for i in range(int(starting), int(ending) +1, 1):
    if len(str(i)) == 1:
        writeAndPrint(str(whatStreet).lower(),"00"+str(i))
    elif len(str(i)) == 2:
        writeAndPrint(str(whatStreet).lower(),"0"+str(i))
    elif len(str(i)) == 3:
        writeAndPrint(str(whatStreet).lower(), str(i))
    time.sleep(3)
