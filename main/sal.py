import os
import tkinter
import easygui
import datetime
import pathlib
import webbrowser
import requests
import sys
import json

name = "SAL"
current = pathlib.Path(__file__).parent.resolve()

json_path = current / "about.json"
fp = ""
jbin = (current / "jdk8" / "jre" / "bin" / "javaw.exe").resolve()

class jsoncheck():
    def __init__(self):
        with open(json_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

if jsoncheck().metadata["asign"] != "com.7alide.sal" or jsoncheck().metadata["ver"] != "1.0" or jsoncheck().metadata["enc"] != "G9nkCyU8SYfEK6ApFuhE26FWliJeDDapfjySbg7pZHprHeO3wANRBcjO7AFiBtXu":
    tkinter.messagebox.showerror("Error", "File had been modified (Error Code: 575)\nPlease reinstall the launcher again.")
    sys.exit()

if not jbin.exists():
    tkinter.messagebox.showerror("Cannot found Java", f"Cannot found Java at {jbin} (Error Code: 579)\nPlease reinstall the launcher again.")
    sys.exit()

links = {
    # Alpha v1.0
    "Alpha v1.0.6": "a1.0.6/a1.0.6",
    "Alpha v1.0.6_01": "a1.0.6/a1.0.6_01",
    "Alpha v1.0.6_02": "a1.0.6/a1.0.6_02",
    "Alpha v1.0.6_03": "a1.0.6/a1.0.6_03",
    "Alpha v1.0.7": "a1.0.7/a1.0.7",
    "Alpha v1.0.8_01": "a1.0.8/a1.0.8_01",
    "Alpha v1.0.9": "a1.0.9/a1.0.9",
    "Alpha v1.0.10": "a1.0.10/a1.0.10",
    "Alpha v1.0.11": "a1.0.11/a1.0.11",
    "Alpha v1.0.12": "a1.0.12/a1.0.12",
    "Alpha v1.0.13": "a1.0.13/a1.0.13",
    "Alpha v1.0.13_01 (Original)": "a1.0.13/a1.0.13_01-o",
    "Alpha v1.0.13_01": "a1.0.13/a1.0.13_01",
    "Alpha v1.0.14 (Original)": "a1.0.14/a1.0.14-o",
    "Alpha v1.0.14": "a1.0.14/a1.0.14",
    "Alpha v1.0.14 (Launcher)": "a1.0.14/a1.0.14-l",
    "Alpha v1.0.15": "a1.0.15/a1.0.15",
    "Alpha v1.0.16": "a1.0.16/a1.0.16",
    "Alpha v1.0.16_01": "a1.0.16/a1.0.16_01",
    "Alpha v1.0.16_02": "a1.0.16/a1.0.16_02",
    "Alpha v1.0.17": "a1.0.17/a1.0.17",
    "Alpha v1.0.17_01": "a1.0.17/a1.0.17_01",
    "Alpha v1.0.17_02": "a1.0.17/a1.0.17_02",
    "Alpha v1.0.17_03": "a1.0.17/a1.0.17_03",
    "Alpha v1.0.17_04": "a1.0.17/a1.0.17_04",
    # Alpha v1.1
    "Alpha v1.1.0": "a.1.1.0/a1.1.0",
    "Alpha v1.1.1": "a.1.1.1/a1.1.1",
}

pair = {
    # Alpha v1.0
    "Alpha v1.0.6": "a1.0.6",
    "Alpha v1.0.6_01": "a1.0.6_01",
    "Alpha v1.0.6_02": "a1.0.6_02",
    "Alpha v1.0.6_03": "a1.0.6_03",
    "Alpha v1.0.7": "a1.0.7",
    "Alpha v1.0.8_01": "a1.0.8_01",
    "Alpha v1.0.9": "a1.0.9",
    "Alpha v1.0.10": "a1.0.10",
    "Alpha v1.0.11": "a1.0.11",
    "Alpha v1.0.12": "a1.0.12",
    "Alpha v1.0.13": "a1.0.13",
    "Alpha v1.0.13_01 (Original)": "a1.0.13_01-o",
    "Alpha v1.0.13_01": "a1.0.13_01",
    "Alpha v1.0.14 (Original)": "a1.0.14-o",
    "Alpha v1.0.14": "a1.0.14",
    "Alpha v1.0.14 (Launcher)": "a1.0.14-l",
    "Alpha v1.0.15": "a1.0.15",
    "Alpha v1.0.16": "a1.0.16",
    "Alpha v1.0.16_01": "a1.0.16_01",
    "Alpha v1.0.16_02": "a1.0.16_02",
    "Alpha v1.0.17": "a1.0.17",
    "Alpha v1.0.17_01": "a1.0.17_01",
    "Alpha v1.0.17_02": "a1.0.17_02",
    "Alpha v1.0.17_03": "a1.0.17_03",
    "Alpha v1.0.17_04": "a1.0.17_04",
    # Alpha v1.1
    "Alpha v1.1.0": "a1.1.0/a1.1.0",
    "Alpha v1.1.1": "a1.1.1/a1.1.1",
}

now = datetime.datetime.now()
if now.hour < 12 and now.hour >= 6:
    tms = "Good morning!"
elif now.hour >= 12 and now.hour < 18:
    tms = "Good Arvo!"
else:
    tms = "Good evening!"

if now.month == 7 and now.day == 24:
    ad = "Happy birthday, MBLC7!"
if now.month == 4 and now.day == 1:
    ad = "April Fool!"
else:
    ad = ""

def download(url, filename):
    d = requests.get(url)
    save = current / filename

    if d.status_code == 200:
        save.write_bytes(d.content)
    else:
        tkinter.messagebox.showerror("Failed", "Download failed (Error Code: 578)\nPlease check your internet connection.")

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

if now.year < 2009 and now.month < 5 and now.day < 17:
    tkinter.messagebox.showerror("Invalid Date", f"Date is invalid (Error Code: 576)\nPlease set your time server.")

match easygui.choicebox(f"👋{tms}, today is {months[now.month]} {now.day} of {now.year}. {ad}", name, ["Select Versions", "About", "Join Organisation", "Exit"]):
    case "Select Versions":
        select = easygui.choicebox("Select Version\n(Due to technical issues, Applet does not support launching yet)", name, [
            # Alpha v1.0
            "Alpha v1.0.6",
            "Alpha v1.0.6_01",
            "Alpha v1.0.6_02",
            "Alpha v1.0.6_03",
            "Alpha v1.0.7",
            "Alpha v1.0.8_01",
            "Alpha v1.0.9",
            "Alpha v1.0.10",
            "Alpha v1.0.11",
            "Alpha v1.0.12",
            "Alpha v1.0.13",
            "Alpha v1.0.13_01 (Original)",
            "Alpha v1.0.13_01",
            "Alpha v1.0.14 (Original)",
            "Alpha v1.0.14",
            "Alpha v1.0.14 (Launcher)",
            "Alpha v1.0.15",
            "Alpha v1.0.16",
            "Alpha v1.0.16_01",
            "Alpha v1.0.16_02",
            "Alpha v1.0.17",
            "Alpha v1.0.17_01",
            "Alpha v1.0.17_02",
            "Alpha v1.0.17_03",
            "Alpha v1.0.17_04",
            # Alpha v1.1
            "Alpha v1.1.0",
            "Alpha v1.1.1",

        ])

        if select is None:
            sys.exit()
        elif "a" in pair[select] or "b" in pair[select]:
            asign = "net.minecraft.client.Minecraft"
        
        fp = current / f"{pair[select]}.jar"

        if fp.exists():
            os.chdir(current)
            cmd = f'{jbin} -Xmx1024M -Xms1024M -cp "lwjgl.jar";"lwjgl_util.jar";"jinput.jar";"{pair[select]}.jar" -Djava.library.path="{current / "natives"}" -Dnet.java.games.input.librarypath="{current / "natives"}" -Djava.util.Arrays.useLegacyMergeSort=true -Dsun.java2d.opengl=true -Dorg.lwjgl.librarypath="{current / "natives"}" {asign}'
            os.system(cmd + " & pause")
        else:
            download(f"https://github.com/7alide/sal/raw/refs/heads/main/versions/{links[select]}.jar", f"{pair[select]}.jar")
            os.chdir(current)
            cmd = f'{jbin} -Xmx1024M -Xms1024M -cp "lwjgl.jar";"lwjgl_util.jar";"jinput.jar";"{pair[select]}.jar" -Djava.library.path="{current / "natives"}" -Dnet.java.games.input.librarypath="{current / "natives"}" -Djava.util.Arrays.useLegacyMergeSort=true -Dsun.java2d.opengl=true -Dorg.lwjgl.librarypath="{current / "natives"}" {asign}'
            os.system(cmd + " & pause")
    
    case "About":
        tkinter.messagebox.showinfo("About", f"Version: {jsoncheck().metadata['ver']}\nhttps://github.com/7alide/sal\nCopyright©️ 2026 7alide")

    case "Join Organisation":
        webbrowser.open("https://github.com/7alide")
    
    case "Exit":
        sys.exit()
    
    case None:
        sys.exit()