"""
    @ open source by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ facebook : https://www.facebook.com/YounisDgk
    
"""

import requests
import sys
import os
import time
sys.stdout.write('\x1b]2; ⏤͟͟͞͞ ⍣⃝😈🆈🄾🆄🄽🅸🅂⍣⃝😈 ͟͞⏤ \x07')
os.system('xdg-open https://www.youtube.com/@YounisXyz')
R = "\033[1;91m"
P = "\033[1;97m"
H = "\033[1;92m"
reset = "\x1b[0m"

class Code:
    def __init__(self):
        self.l = 54

    def clear(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system("clear")

    def divider(self):
        print(f"{P}-" * self.l)

    def display_header(self):
        self.divider()
        print(f"                   {P}A2F Code Generator")
        self.divider()

    def get_code(self, key):
        url = f"https://2fa.live/tok/{key}"
        try:
            response = requests.get(url)
            data = response.json()
            code = data.get("token")
            if code:
                return code
            else:
                return f"{R}Key salah atau tidak valid!{reset}"
        except requests.exceptions.RequestException as e:
            return f"{R}Terjadi kesalahan saat meminta data: {str(e)}{reset}"

    def run(self):
        self.clear()
        self.display_header()
        while True:
            key = input(f"{P}Masukkan Key A2F: ")
            if key == "":
                print(f"{R}Jangan kosong bodoh!"); time.sleep(2); generator.run()
            if key == "none":
                sys.exit()
            else:
                code = self.get_code(key)
                print(f"Kode: {H}{code}{reset}")
                self.divider()

if __name__ == "__main__":
    generator = Code()
    generator.run()
