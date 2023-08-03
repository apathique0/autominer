import time, pyautogui, os
os.system("cls")

count = 0

verywoof = input("Ton adresse VeryWoofWallet : ")
ticker = input("Ton ticket (ex: dogi) : ")
limitpermint = input("Limite par mint : ")

for i in range(100):
    time.sleep(10)
    pyautogui.write(f"node . drc-20 mint {verywoof} {ticker} {limitpermint} 12")
    pyautogui.hotkey('enter')
    time.sleep(310)