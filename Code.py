# importar bibliotecas
import pyautogui
import time
import pyperclip

# Esperar um segundo e emitir alerta que o programa vai começar a rodar
pyautogui.PAUSE = 1
pyautogui.alert("O Robô vai começar a trabalhar, aperte OK e não mexa em nada")
# Resolução da tela tem que estar em 1280 x 1024, e o Chrome em 80% - NCLS01.
# Passo 1 - Abrir Milvus
time.sleep(1)
pyautogui.click(353,1000)
time.sleep(2)
pyautogui.click(106,14)
time.sleep(2)
# Abrir inventario
pyautogui.click(19,229)
time.sleep(1)
# Abrir licenças
pyautogui.click(126,347)
time.sleep(1)
# Selecionar Clientes
pyautogui.click(367,85)
time.sleep(1)
pyautogui.write("HARMONIA")
time.sleep(3)
pyautogui.click(401,183)
time.sleep(2)

i=0
while i < 400:
    pyautogui.click(1228,331)
    time.sleep(3)
    pyautogui.click(660,168)
    time.sleep(3)
    pyautogui.click(976,113)
    time.sleep(3)
    i +=1
    print(i)
