"""
    @ open source by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ facebook : https://www.facebook.com/YounisDgk
    
"""
from rich.console import Console
from threading import Thread
import requests, random
import string, json
sys.stdout.write('\x1b]2; ⏤͟͟͞͞ ⍣⃝😈🆈🄾🆄🄽🅸🅂⍣⃝😈 ͟͞⏤ \x07')
os.system('xdg-open https://www.youtube.com/@YounisXyz')
Con = Console()
Ex = 0

def Users():
    global Ex
    try:
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        UseriD = str(random.randrange(5249322))
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        username = response.json()['data']['user']['username']
        Ex += 1
        with open("2011.txt", "a") as file:
            file.write(username + "\n")
        Con.print(f"{username}")
        return username
    except Exception as e:
        return None

def ExUsers():
    for _ in range(2500):
        Users()

threads = []
for _ in range(100):
    thread = Thread(target=ExUsers)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

Con.print(f"</> Users ExtracteD : [bold]{Ex}[/bold]")

