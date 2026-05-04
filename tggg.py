# -*- coding: utf-8 -*-
import os
import webbrowser
import random
import time
import subprocess
import sys

VIOLET = "\033[95m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def run_tool(path):
    subprocess.run([sys.executable, path])


def effet_inversion_logo(logo):
    chars = list(logo)
    start = time.time()

    while time.time() - start < 1:
        temp = chars[:]

        for i in range(len(temp)):
            if random.random() < 0.2:
                temp[i] = random.choice("█▓▒░ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

        clear()
        print(VIOLET + "".join(temp) + RESET)
        time.sleep(0.05)

    clear()
    print(VIOLET + logo + RESET)


def afficher_logo():
    logo = r"""
███████╗ ██████╗ ███████╗ ██████╗ ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝██╔═══██╗██╔════╝██╔═══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████╗██║   ██║███████╗██║   ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
╚════██║██║   ██║╚════██║██║   ██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
███████║╚██████╔╝███████║╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
"""
    effet_inversion_logo(logo)


def afficher_menu():
    print(VIOLET + r"""
      ╔══════════════════════════════════════════════════════════════════════════════════╗
      ║ Cyb3rtech Tool | v1.0.4 | [0] > Support (discord)             [ - ] [ □ ] [ X ]  ║
      ║══════════════════════════════════════════════════════════════════════════════════║
      ║                                                                                  ║
      ║ [01] > gunlol                                                                    ║
      ║ [02] > discord_n3tro_generator                                                   ║
      ║ [03] > grab-t3ken-discord                                                       ║
      ║ [04] > phone_number_tracker                                                     ║
      ║ [05] > Token-Nuker                                                              ║
      ║                                                                                  ║
      ╚══════════════════════════════════════════════════════════════════════════════════╝
    """ + RESET)


def glitch_loading(text, duration=1):
    chars = list(text)
    start = time.time()

    while time.time() - start < duration:
        temp = chars[:]

        for i in range(len(temp)):
            if random.random() < 0.25:
                temp[i] = random.choice("█▓▒░0123456789ABCDEF")

        clear()
        print(VIOLET + "".join(temp) + RESET)
        time.sleep(0.05)


def menu_interactif():
    while True:
        clear()
        afficher_menu()

        choice = input(VIOLET + "\n👉 Choisis un numéro (Q pour quitter) : " + RESET).strip().lower()

        if choice == "q":
            break

        # 🌐 GUNLOL MENU
        elif choice == "1":
            while True:
                clear()
                print(VIOLET + "╔════════════════════╗" + RESET)
                print(VIOLET + "║     GUNLOL MENU    ║" + RESET)
                print(VIOLET + "╚════════════════════╝\n" + RESET)

                print(VIOLET + "[1] slayz" + RESET)
                print(VIOLET + "[2] spixx" + RESET)
                print(VIOLET + "[P] retour\n" + RESET)

                sub = input(VIOLET + "👉 choix : " + RESET).strip().lower()

                if sub == "1":
                    glitch_loading("OUVERTURE SLAYZ...")
                    webbrowser.open("https://guns.lol/slayz33k")
                    time.sleep(1)

                elif sub == "2":
                    glitch_loading("OUVERTURE SPIXX...")
                    webbrowser.open("https://guns.lol/spixxx")
                    time.sleep(1)

                elif sub == "p":
                    break

        # ✅ TES VRAIS SCRIPTS
        elif choice == "2":
            print(VIOLET + "discord_n3tro_generator lancé..." + RESET)
            time.sleep(1)
            run_tool("tools/discord_n3tro_generator.py")

        elif choice == "3":
            print(VIOLET + "grab-t3ken-discord lancé..." + RESET)
            time.sleep(1)
            run_tool("tools/grab-t3ken-discord.py")

        elif choice == "4":
            print(VIOLET + "phone_number_tracker lancé..." + RESET)
            time.sleep(1)
            run_tool("tools/phone_number.py")

        elif choice == "5":
            print(VIOLET + "Token-Nuker lancé..." + RESET)
            time.sleep(1)
            run_tool("tools/Token-Nuker.py")

        else:
            print(VIOLET + "Option inconnue." + RESET)
            time.sleep(1)


if __name__ == "__main__":
    clear()
    afficher_logo()
    afficher_menu()

    webbrowser.open("https://guns.lol/sosogf")

    menu_interactif()

    input(VIOLET + "\nAppuie sur Entrée pour quitter..." + RESET)