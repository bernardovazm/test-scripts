import time, ctypes, random, pyautogui, pydirectinput, subprocess, psutil

pyautogui.FAILSAFE = False

# TESTS

# dec
client_process = "LeagueClient.exe"
game_process = "League of Legends.exe"
states = ["queue", "champ select", "loading", "game", "post", "lol mode"]
state = states[0]
route_images = "sm1"
images = {
    "play": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientplay.png",
    "tft": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clienttft.png",
    "confirm": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientconfirmlobby.png",
    "queue": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientfindgame.png",
    "accept": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientacceptgame.png",
    "tftbuyxp": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftbuyexp.png",
    "tftbuy2g": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftbuy2g.png",
    "tftbuy3g": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftbuy3g.png",
    "gameconfirmff": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gameconfirmff.png",
    "gamestage3": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/game_stage_3.png",
    "again": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientplayagain.png",
    "champ1": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/champ1.png",
    "champ2": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/champ2.png",
    "champ3": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/champ3.png",
    "gameleave": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/game_leave.png",
    "tftdefault": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftdefault.png",
    "clientok": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/ok.png",
}

def process_exists(process_name):
    return process_name in (p.name() for p in psutil.process_iter())

def find_img(image, delay=0.14, timeout=2):
    start_time = time.time()
    loc = None
    while time.time() - start_time < timeout:
        loc = pyautogui.locateCenterOnScreen(image=image, confidence=0.9, grayscale=True)
        if loc is not None:
            break
    if loc is None:
        print("No img matching " + image + " was found. Continuing...")
        return False
    print("Img matching image " + image + " was found.")
    return True

def click(loc, delay=0.013, button="left"):
    current_pos = pyautogui.position()
    pyautogui.moveTo(x=loc[0], y=loc[1], duration=0.01)
    pydirectinput.mouseDown()
    time.sleep(0.022)
    pydirectinput.mouseUp()
    pyautogui.moveTo(x=500, y=300, duration=0)
    pyautogui.moveTo(x=loc[0], y=loc[1], duration=0)
    pydirectinput.mouseDown()
    time.sleep(0.09)
    pydirectinput.mouseUp()
    pyautogui.moveTo(x=1000, y=500, duration=0.01)
    print("Mouse: " + str(current_pos))
    pyautogui.moveTo(current_pos, duration=0)
    time.sleep(1)

def click_button(image, delay=0.014, timeout=2, button="left"):
    start_time = time.time()
    loc = None
    while time.time() - start_time < timeout:
        loc = pyautogui.locateCenterOnScreen(image=image, confidence=0.9, grayscale=True)
        if loc is not None:
            break
    if loc is None:
        print("No button matching image " + image + " was found. Continuing...")
        return False
    click(loc, delay, button)
    print("Button matching image " + image + " was found.")
    return True

def make_lobby():
    print("Making lobby.")
    global state
    click_button(images.get("again"))
    if (click_button(images.get("play")) and click_button(images.get("tft"))
            and click_button(images.get("confirm"))):
        state = states[0]
        return True
    else:
        pyautogui.click()
        if (click_button(images.get("tft"))
                and click_button(images.get("confirm"))):
            state = states[0]
            return True
        if (click_button(images.get("again"))):
            click_button(images.get("queue"))
            state = states[0]
        if (click_button(images.get("queue"))):
            state = states[0]
    print("Unable to make lobby.")
    return False

def queue(timeout=18):
    global state
    print("Def Queue")
    if (find_img(images.get("accept")) is True):
        click_button(images.get("accept"))
    if (find_img(images.get("again")) is True):
        click_button(images.get("again"))
    if (find_img(images.get("queue")) is True):
        click_button(images.get("queue"))
    while click_button(images.get("queue")):
        print("Attempting to start queue.")
    start_time = time.time()
    print("Queue successfully started at: " + str(start_time))
    global state
    while time.time() - start_time < timeout:
        if (find_img(images.get("accept")) is True):
            click_button(images.get("accept"))
            start_time = time.time()
            while time.time() - start_time < 15:
                return True
    #if pyautogui.locateOnScreen(image=images.get("choose"), confidence=0.8, grayscale=True) is not None or \
        if process_exists(game_process):
            state = states[1]
        return True
    print("Queue timed out.")
    return False

def game():
    time.sleep(1)
    if (process_exists(game_process) is True):
        print("Game found. Def Game")
        start_time = time.time()
        timer = start_time
        print("Playing Game and Checking Stage to FF")
        if (find_img(images.get("gameleave")) is True):
            print("Leaving game...")
            click_button(images.get("gameleave"))
            pyautogui.click()
            return True
        if (find_img(images.get("gamestage3")) is True):
            print("FFing...")
            click_button(images.get("gamestage3"))
            pydirectinput.press("enter")
            pyautogui.write("/ff")
            pydirectinput.press("enter")
        if (click_button(images.get("gameconfirmff")) is True):
            pyautogui.click()
            print("Game completed.")
            return True
        if (process_exists(game_process) is True and find_img(images.get("tftdefault")) is True and find_img(images.get("gamestage3")) is False):
            print("9.1 - Playing TFT")
            time.sleep(random.randrange(196, 280))
            if (find_img(images.get("tftdefault")) is True):
                click_button(images.get("gameleave"))
                click_button(images.get("tftbuyxp"))
                click_button(images.get("tftbuy2g"))
                click_button(images.get("tftbuy3g"))
                click_button(images.get("champ1"))
                click_button(images.get("champ2"))
                click_button(images.get("champ3"))
        global state
        state = states[4]
        return True

def post_game():
    start_time = time.time()
    global state
    time.sleep(3)
    click_button(image=images.get("again"))
    while not click_button(image=images.get("again"), timeout=1):
        if time.time() - start_time > 60:
            print("Post game lobby timed out.")
            return False
    state = states[0]
    return True
    
# restarts the game if there is an error
def fail_safe(tries=50, timeout=9):
    global state
    click_button(images.get("accept"))
    click_button(images.get("clientok"))
    if process_exists(game_process) is not False:
        print("Em jogo, tentativas de mantar o bot aumentadas em 1 State: " + str(state))
        tries += 1
    if state == "queue":
        print("Em q, tentativas de mantar o bot aumentadas em 1. State: " + str(state))
        tries += 1
    print("Fail safe. Verifying game... " + str(state))
    if process_exists(game_process) is False:
        print("Game not found. Fail safe continuing..")
        state = None
        start_time = time.time()
        while tries > 0:
            if process_exists(client_process) and \
                    pyautogui.locateOnScreen(image=images.get("play"), confidence=0.8, grayscale=True) is not None and \
                    make_lobby():
                return
            else:
                if process_exists(game_process) is not False:
                    tries += 1
                    state = "game"
                    return
            if time.time() - start_time > timeout:
                start_time = time.time()
                tries -= 1
                state = "queue"
                queue()
                print("Failed to load client. Retrying... " + str(state))
        exit("Failed to load client (patching?).")

def main():
    print('1 - Função main rodando')    
    click_button(images.get("accept"))
    time.sleep(1)
    global state
    while True:
        print('1.1 - Script pronto, aguardando ativação do Scroll Lock ' + str(get_scrolllock_state()))
        while get_scrolllock_state() >= 1:
            print('2 - Scroll Lock ativo ' + str(get_scrolllock_state()))
            #if process_exists(client_process):
            if process_exists(client_process) is False:
                print('2.1 - Client não identificado. Aguardando abertura do client. Erro: ' + game_process + process_exists(game_process))
            else:
                print('2.2 - Processo ' + client_process + ', executando sequência')
                while get_numlock_state() == 0:
                    print('3.1 - Numlock OFF - LoL Yuumi Bot Mode - ' + str(get_numlock_state()))
                    if process_exists(game_process) is True:
                        state = "lol mode"
                        print('3.2 - Processo ' + game_process + ', executando sequência')
                        e_press()
                        print('e')
                        time.sleep(random.randrange(30, 45))
                        print('w')
                        w_press()
                if get_numlock_state() == 1:
                    print('4.1 - Numlock ON - TFT Permaqueue Mode - ' + str(get_numlock_state()) + ' ' + state)
                    if process_exists(game_process) is True:
                        print('Jogo identificado ' + game_process)
                        state = "game"
                    else:
                        fail_safe()
                    worked = True
                    if state == "queue":
                        worked = queue()
                    elif state == "game":
                        worked = game()
                    elif state == "post":
                        worked = post_game()
                    else:
                        worked = False
                    if not worked:
                        print("FATAL ERROR! Attempting fail safe measures...")
                        fail_safe()
                        

def w_press():
    pydirectinput.press(['w'])
    #pyautogui.press(['w'])

def e_press():
    time.sleep(random.randrange(6, 18))
    pyautogui.press(['e'])

def get_scrolllock_state():
    while True:
        hllDll = ctypes.WinDLL ("User32.dll")
        VK_SCROLL = 0x91
        return hllDll.GetKeyState(VK_SCROLL)

def get_numlock_state():
    while True:
        hllDll = ctypes.WinDLL ("User32.dll")
        VK_NUMLOCK = 0x90
        return hllDll.GetKeyState(VK_NUMLOCK)

main()
