import time, random, pyautogui, pydirectinput, psutil, atexit, win32gui
# os, subprocess, ctypes, win32com.client
import tkinter as tk
from pycaw.pycaw import AudioUtilities
from win32gui import GetWindowText, GetForegroundWindow
from win32api import GetKeyState
from win32con import VK_SCROLL, VK_NUMLOCK

pyautogui.FAILSAFE = False

pydirectinput.FAILSAFE = False

# TESTS

# dec
client_process = "LeagueClient.exe"
config_dir = "C:/Riot Games/League of Legends/Config/game.cfg"
dir_config_normal = "C:/Users/Admin/Desktop/tes86/loltftbot/cfg/gameNormal.cfg"
dir_config_window = "C:/Users/Admin/Desktop/tes86/loltftbot/cfg/gameWindow.cfg"
client_window_name = "League of Legends"
game_window_name = "League of Legends (TM) Client"
game_process = "League of Legends.exe"
states = ["queue", "champ select", "loading", "game", "post", "lol mode"]
state = states[0]
windowList = []
route_images = "sm1"
count_seconds = 0
images = {
    "play": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientplay.png",
    "tft": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clienttft.png",
    "confirm": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientconfirmlobby.png",
    "queue": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientfindgame.png",
    "accept": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientacceptgame.png",
    "tftbuyxp": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftbuyexp.png",
    "tftbuy2g": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftbuy2g.png",
    "tftbuy3g": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftbuy3g.png",
    "tftbuy5g": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftbuy5g.png",
    "gameconfirmff": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gameconfirmff.png",
    "gamestage1": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/game_stage_1.png",
    "gamestage3": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/game_stage_3.png",
    "gamestage5": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/game_stage_5.png",
    "again": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/clientplayagain.png",
    "champ1": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/champ1.png",
    "champ2": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/champ2.png",
    "champ3": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/champ3.png",
    "gameleave": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/game_leave.png",
    "tftdefault": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gametftdefault.png",
    "clientok": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/ok.png",
    "reconnect": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/reconnect.png",
    "group": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/group.png",
    "tftquestionmark": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/game_questionmark.png",
    "tftupgrade": "C:/Users/Admin/Desktop/tes86/loltftbot/" + route_images + "/gameselectupgrade.png",
}

def read_file(file):
    print("0.001 - Reading file: " + file)
    with open(file, "r") as f:
        return f.read()

def write_file(content, file):
    print("0.002 - Writing file ")
    with open(file, "w") as f:
        f.write(content)

#configs
def change_configs():
    print("0.01 - CONFIGS CHANGED: Volume Mute & Resolution")
    configs = read_file(dir_config_window)
    write_file(configs, config_dir)

def mute(self):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        if session.Process and session.Process.name() == self:
            interface.SetMute(1, None)
            print(self, " has been muted.")  # debug

def unmute(self):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        if session.Process and session.Process.name() == self:
            interface.SetMute(0, None)
            print(self, " has been unmuted.")  # debug

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        if (win32gui.GetWindowText(hwnd) != None):
            n = [win32gui.GetWindowText(hwnd), hwnd]
            if n:
                windowList.append(n)

def focusWindow(windowName):
    win32gui.EnumWindows(winEnumHandler, None)
    for window in windowList:
        if (window[0] == windowName):
            hwnd = window[1]
            if (win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '' and GetForegroundWindow() != hwnd):
                #shell = win32com.client.Dispatch("WScript.Shell")
                #shell.SendKeys('%')
                try:
                    win32gui.SetForegroundWindow(hwnd)
                except:
                    print("Exception treatment, prob: pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')")
                windowList.clear()
                print("0.2.1 - Focus window: " + str(window) + " -with informed name and hwnd: " + str(windowName) + str(hwnd) + str(windowList))

def process_exists(process_name):
    if (process_name in (p.name() for p in psutil.process_iter()) is True):
        print("0.3.2 - Process Confirmed: " + str(process_name))
    return process_name in (p.name() for p in psutil.process_iter())

def restore_configs():
    print("10.0 - CONFIGS RESTORED")
    unmute("League of Legends.exe")
    configs = read_file(dir_config_normal)
    write_file(configs, config_dir)

def alert_box(delay_sec, image=images.get("clientok"), text=None, bg=None):
    x_current, y_current = pyautogui.position()
    window = tk.Tk()
    window.geometry(f'10x30+{x_current-50}+{y_current-45}')
    photo = tk.PhotoImage(file=image)
    if(text != None):
        labelText = tk.Label(window, text=text)
        labelText.pack()
    label = tk.Label(window, image=photo, bg=bg, width=150, height=100)
    label.pack()
    window.update()
    # window.attributes("-topmost", True)
    # Line below and above might crashes 'Scroll Lock' verifications;
    # window.after(1, lambda: window.focus_force())
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    time.sleep(delay_sec)
    window.destroy()

change_configs()
mute("League of Legends.exe")
atexit.register(restore_configs)

def find_img(image, delay=0.14, timeout=2, grayscale=True, confidence=0.9):
    start_time = time.time()
    loc = None
    while time.time() - start_time < timeout:
        loc = pyautogui.locateCenterOnScreen(image=image, confidence=confidence, grayscale=grayscale)
        if loc is not None:
            break
    if loc is None:
        print("X - No img matching " + image + " was found. Continuing...")
        return False
    print("Y - Img matching image " + image + " was found.")
    return True

def script_available_validation(image):
    count_times = -1
    while pyautogui.position()[0] < 0:
        count_times += 1
        if (count_times == 10 or count_times == -1):
            print("X - Mouse out of screen: " + str(pyautogui.position()[0]) + ", image: " + image)
            count_times = 0
        time.sleep(1)
    return True

def click(loc, delay=random.uniform(0.0009, 0.001), button="left", image=images.get("clientok"), clicks=1, grayscale=True, confidence=0.9, sleep1=0.001, sleep2=0.004):
    locRand0 = loc[0]+random.uniform(-1,3)
    locRand1 = loc[1]+random.uniform(-1,3)
    if ((GetKeyState(VK_SCROLL) >= 1) is True and (script_available_validation(image) == True)):
        if (pyautogui.position() == (683, 375)):
            current_pos = (13, 600)
        else:
            current_pos = pyautogui.position()
        active_window = GetWindowText(GetForegroundWindow())
        alert_box(0.4, image, text=f'{clicks}')
        pydirectinput.mouseUp()
        if(GetWindowText(GetForegroundWindow()) != game_window_name):
            pyautogui.moveTo(x=locRand0, y=locRand1, duration=delay, tween=pyautogui.easeInSine)
            pydirectinput.mouseDown()
            time.sleep(random.uniform(0.06, 0.09))
            pydirectinput.mouseUp()
        for click in range(clicks):
            if (find_img(image=image, timeout=0.01, grayscale=grayscale, confidence=confidence) is False):
                focusWindow(active_window)
                pyautogui.moveTo(x=13, y=600, duration=0.01, tween=pyautogui.easeInSine)
                pyautogui.moveTo(current_pos, duration=0)
                alert_box(0.1, image, bg="black")
                break
            elif (click <= clicks or find_img(image=image, timeout=0.01, grayscale=grayscale, confidence=confidence) is True):
                if (pyautogui.position() != loc):
                    pyautogui.moveTo(x=locRand0, y=locRand1, duration=delay, tween=pyautogui.easeInSine)
                    print(" - Click and move: " + str(click+1) + str(clicks) + str(image))
                pydirectinput.mouseDown(button=button)
                time.sleep(random.uniform(sleep1, sleep2))
                pydirectinput.mouseUp(button=button)
                if (click+1 == clicks or find_img(image=image, timeout=0.01, grayscale=grayscale, confidence=confidence) is False):
                    pyautogui.moveTo(x=13, y=600, duration=0.01, tween=pyautogui.easeInSine)
                    pyautogui.moveTo(current_pos, duration=0)
                    alert_box(0.1, image, bg="black")
                    print(" - Mouse returned to initial position: " + str(current_pos))
            else:
                focusWindow(active_window)
                pyautogui.moveTo(x=13, y=600, duration=0.01, tween=pyautogui.easeInSine)
                pyautogui.moveTo(current_pos, duration=0)
                alert_box(0.1, image, bg="black")
                break
        time.sleep(1)
    else:
        print("X - 0 Click not realized, scroll state: " + str(GetKeyState(VK_SCROLL)))

def click_button(image, grayscale=True, delay=0.014, timeout=2, button="left", clicks=1, confidence=0.9, sleep1=0.025, sleep2=0.04):
    start_time = time.time()
    loc = None
    while time.time() - start_time < timeout:
        loc = pyautogui.locateCenterOnScreen(image=image, confidence=confidence, grayscale=grayscale)
        if loc is not None:
            break
    if loc is None:
        print("X - No button matching image " + image + " was found. Continuing...")
        return False
    click(loc, delay, button, image=image, clicks=clicks, grayscale=grayscale, confidence=confidence, sleep1=sleep1, sleep2=sleep2)
    print("Y - Button matching image " + image + " was found.")
    return True

def move_item(duration=random.uniform(0.005, 0.008)):
    if ((GetKeyState(VK_SCROLL) >= 1) is True):
        print(" - Moving item")
        if (pyautogui.position() == (683, 375)):
            current_pos = (13, 600) #13, 600 main monitor
        else:
            current_pos = pyautogui.position()
        alert_box(0.5, text=f'OK')
        pyautogui.moveTo(x=270+random.randrange(-2,2), y=500+random.randrange(-2,2), duration=duration, tween=pyautogui.easeInSine)
        pydirectinput.mouseDown()
        pyautogui.moveTo(x=700+random.randrange(-2,2), y=400+random.randrange(-2,2), duration=duration, tween=pyautogui.easeInSine)
        time.sleep(random.uniform(0.04, 0.6))
        pydirectinput.mouseUp()
        pyautogui.moveTo(x=13, y=600, duration=0.01, tween=pyautogui.easeInSine)
        pyautogui.moveTo(current_pos, duration=0)
        alert_box(0.2, text=None, bg="black")
    else:
        print("X - 0 Move item not realized, scroll state: " + str(GetKeyState(VK_SCROLL)))

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
    if (find_img(images.get("accept"),  timeout=0.01) is True):
        click_button(images.get("accept"), grayscale=False)
    if (find_img(images.get("again")) is True):
        click_button(images.get("again"))
    if (find_img(images.get("queue"),  timeout=0.01) is True):
        click_button(images.get("queue"))
    if (find_img(images.get("reconnect")) is True):
        click_button(images.get("reconnect"))
    if (find_img(images.get("accept")) is True):
        click_button(images.get("accept"), grayscale=False)
    if (find_img(images.get("group")) is True):
        click_button(images.get("group"))
    while click_button(images.get("queue")):
        print("Attempting to start queue.")
    start_time = time.time()
    print("Queue successfully started at: " + str(start_time))
    global state
    while time.time() - start_time < timeout:
        if (find_img(images.get("accept")) is True):
            click_button(images.get("accept"), grayscale=False)
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
        mute(game_process)
        print("Playing Game and Checking Stage to FF")
        if (pyautogui.position() == (683, 375)):
            pyautogui.moveTo(x=13, y=600, duration=0, tween=pyautogui.easeInSine)
        if (find_img(images.get("gameleave")) is True):
            print("Leaving game...")
            click_button(images.get("gameleave"))
            pyautogui.click()
            return True
        # if (find_img(images.get("gamestage3")) is True):
        #     print("FFing...")
        #     click_button(images.get("gamestage3"))
        #     pydirectinput.press("enter")
        #     pyautogui.write("/ff")
        #     pydirectinput.press("enter")
        if (click_button(images.get("gameconfirmff")) is True):
            pyautogui.click()
            print("Game completed.")
            return True
        if (process_exists(game_process) is True and find_img(images.get("tftdefault")) is True and find_img(images.get("gamestage1")) is False and find_img(images.get("gamestage5")) is False):
            print("9.1 - Playing TFT")
            click_button(images.get("tftupgrade"))
            if (find_img(images.get("tftdefault")) is True):
                active_window2 = GetWindowText(GetForegroundWindow())
                focusWindow(game_window_name)
                click_button(images.get("tftdefault"))
                if(GetWindowText(GetForegroundWindow()) == game_window_name):
                    pydirectinput.press(['space'])
                    print(" - Space Press Walking Around")
                focusWindow(active_window2)
                click_button(images.get("champ3"), confidence=0.85)
                click_button(images.get("champ1"))
                click_button(images.get("tftbuy3g"))
                click_button(images.get("tftbuy2g"))
                click_button(images.get("tftbuyxp"), grayscale=False, button="left", clicks=random.randrange(4, 6), sleep1=0.006, sleep2=0.008)
                click_button(images.get("tftquestionmark"), button="right")
                active_window2 = GetWindowText(GetForegroundWindow())
                focusWindow(game_window_name)
                move_item()
                focusWindow(active_window2)
                for press1 in range(random.randrange(0, 2)):
                    time.sleep(random.uniform(1, 1.5))
                    click_button(images.get("tftdefault"))
                    click_button(images.get("tftquestionmark"), button="right", confidence=0.8)
                    time.sleep(random.uniform(2, 4))
                    active_window = GetWindowText(GetForegroundWindow())
                    focusWindow(game_window_name)
                    if(GetWindowText(GetForegroundWindow()) == game_window_name):
                        pydirectinput.press(['1'])
                        print(" - 1 Press Walking Around")
                    focusWindow(active_window)
                    click_button(images.get("tftquestionmark"), button="right", confidence=0.7)
                    time.sleep(random.uniform(2, 4))
                    click_button(images.get("gameleave"))
            time.sleep(random.uniform(18, 33))
            click_button(images.get("tftdefault"))
            if(GetWindowText(GetForegroundWindow()) == game_window_name):
                pydirectinput.press(['space'])
                print(" - Space Press Walking Around")
            click_button(images.get("champ3"), confidence=0.85)
            time.sleep(random.uniform(68, 97))
        elif (process_exists(game_process) is True and find_img(images.get("tftdefault")) is True and find_img(images.get("gamestage1")) is True or find_img(images.get("tftupgrade"))):
            print("9.2 - Playing TFT Round 1")
            click_button(images.get("tftupgrade"))
            click_button(images.get("tftquestionmark"), button="right", confidence=0.8)
            click_button(images.get("champ3"), confidence=0.85)
            click_button(images.get("champ2"))
            if(find_img(images.get("tftbuy2g"), timeout=1) is True):
                click_button(images.get("tftbuy2g"))
            else:
                click_button(images.get("champ2"))
            click_button(images.get("tftbuyxp"), grayscale=False, button="left", sleep1=0.006, sleep2=0.008)
            if (pyautogui.position() == (683, 375)):
                pyautogui.moveTo(x=13, y=600, duration=0, tween=pyautogui.easeInSine)
            time.sleep(random.uniform(2, 4))
        elif (process_exists(game_process) is True and find_img(images.get("tftdefault")) is True and find_img(images.get("gamestage5")) is True):
            print("9.2 - Playing TFT Round 5")
            click_button(images.get("champ3"), confidence=0.85)
            click_button(images.get("champ1"))
            click_button(images.get("tftbuy3g"))
            click_button(images.get("champ1"))
            click_button(images.get("tftquestionmark"), button="right")
            if (find_img(images.get("gamestage5")) is True):
                click_button(images.get("tftbuyxp"), grayscale=False, button="left", clicks=random.randrange(9, 14), sleep1=0.005, sleep2=0.006)
            time.sleep(random.uniform(18, 33))
            click_button(images.get("champ3"), confidence=0.85)
            time.sleep(random.uniform(64, 83))
            click_button(images.get("gameleave"))
        else:
            print("9.3 - Playing TFT Failed: process " + str(process_exists(game_process) is True) + ", find image default " + str(find_img(images.get("tftdefault")) is True) + ", is on stage 3 " + str(find_img(images.get("gamestage3")) is False) + " and stage 1: " + str(find_img(images.get("gamestage1")) is True))
        global state
        state = states[4]
        return True

def post_game():
    print("Post Game.")
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

def w_press():
    pydirectinput.press(['w'])
    #pyautogui.press(['w'])

def e_press():
    time.sleep(random.randrange(6, 18))
    pyautogui.press(['e'])
    
# restarts the game if there is an error
def fail_safe(tries=50, timeout=9):
    global state
    click_button(images.get("accept"), button="left", clicks=3)
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
    click_button(images.get("accept"), button="left", clicks=2)
    time.sleep(1)
    global state
    global count_seconds
    while True:
        if ((GetKeyState(VK_SCROLL) >= 1) is True):
            print('2 - Scroll Lock ativo ' + str(GetKeyState(VK_SCROLL)))
            if process_exists(client_process) is False:
                print('2.1 - Client não identificado. Aguardando abertura do client. Erro: ' + game_process + process_exists(game_process))
            else:
                print('2.2 - Processo ' + client_process + ', executando sequência')
                if (GetKeyState(VK_NUMLOCK) == 0):
                    print('3.1 - Numlock OFF - LoL Yuumi Bot Mode - ' + str(GetKeyState(VK_NUMLOCK)))
                    if process_exists(game_process) is True:
                        state = "lol mode"
                        print('3.2 - Processo ' + game_process + ', executando sequência')
                        e_press()
                        print('e')
                        time.sleep(random.randrange(30, 45))
                        print('w')
                        w_press()
                if (GetKeyState(VK_NUMLOCK) == 1):
                    print('4.1 - Numlock ON - TFT Permaqueue Mode - ' + str(GetKeyState(VK_NUMLOCK)) + ' ' + state)
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
        else:
            time.sleep(10)
            count_seconds += 10
            print('1.1 - Script pronto, aguardando ativação do Scroll Lock ' + str(GetKeyState(VK_SCROLL)) + ", segundos: " + str(count_seconds))

main()
