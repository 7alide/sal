import os
import tkinter
import easygui
import datetime
import pathlib
import webbrowser
import requests
import sys
import json
import subprocess

name = "SAL"
current = pathlib.Path(__file__).parent.resolve()

json_path = current / "about.json"
fp = ""
jbin = (current / "jdk8" / "jre" / "bin" / "javaw.exe").resolve()

class jsoncheck():
    def __init__(self):
        with open(json_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

if jsoncheck().metadata["asign"] != "com.7alide.sal" or jsoncheck().metadata["ver"] != "1.2.1" or jsoncheck().metadata["enc"] != "KSaFWV0vVWobOjsX0oSKWgisbvL1UQ50mfmBtY5L04JDjIvdkFICDrhBxi0E1qFM":
    tkinter.messagebox.showerror("Modified", "File had been modified (Error Code: 575)\nPlease reinstall the launcher again.")
    sys.exit()

if not jbin.exists():
    tkinter.messagebox.showerror("Java Lost", f"Cannot found Java at {jbin} (Error Code: 579)\nPlease reinstall the launcher again.")
    sys.exit()

links = {
    "Classic 0.0.11a": "c0.0.11a/c0.0.11a",
    "Classic 0.0.12a_03": "c0.0.12a/c0.0.12a_03",
    "Classic 0.0.13a": "c0.0.13a/c0.0.13a",
    "Classic 0.0.13a_03": "c0.0.13a/c0.0.13a_03",
    "Classic 0.0.14a_08": "c0.0.14a/c0.0.14a_08",
    "Classic 0.0.15a": "c0.0.15a/c0.0.15a",
    "Classic 0.0.16a_02": "c0.0.16a/c0.0.16a_02",
    "Classic 0.0.17a": "c0.0.17a/c0.0.17a",
    "Classic 0.0.18a_02": "c0.0.18a/c0.0.18a_02",
    "Classic 0.0.19a_04": "c0.0.19a/c0.0.19a_04",
    "Classic 0.0.19a_06": "c0.0.19a/c0.0.19a_06",
    "Classic 0.0.20a_01": "c0.0.20a/c0.0.20a_01",
    "Classic 0.0.20a_02": "c0.0.20a/c0.0.20a_02",
    "Classic 0.0.21a": "c0.0.21a/c0.0.21a",
    "Classic 0.0.22a_05": "c0.0.22a/c0.0.22a_05",
    "Classic 0.0.23a_01": "c0.0.23a/c0.0.23a_01",
    "Classic 0.24_Survival_Test_03": "c0.24/c0.24_st_03",
    "Classic 0.25_05 Survival Test": "c0.25/c0.25_05_st",
    "Classic 0.27 Survival Test": "c0.27/c0.27_st",
    "Classic 0.28_01": "c0.28/c0.28_01",
    "Classic 0.29": "c0.29/c0.29",
    "Classic 0.29_01": "c0.29/c0.29_01",
    "Classic 0.29_02": "c0.29/c0.29_02",
    "Classic 0.30 Survival": "c0.30/c0.30s",
    "Classic 0.30 Creative": "c0.30/c0.30c",
    "Classic 0.30 Creative (Renew)": "c0.30/c0.30c_r",
    "Alpha v1.0.6": "a1.0.6/a1.0.6",
    "Alpha v1.0.6_01": "a1.0.6/a1.0.6_01",
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
    "Alpha v1.0.17_02": "a1.0.17/a1.0.17_02",
    "Alpha v1.0.17_03": "a1.0.17/a1.0.17_03",
    "Alpha v1.0.17_04": "a1.0.17/a1.0.17_04",
    "Alpha v1.1.0 (Original)": "a1.1.0/a1.1.0-o",
    "Alpha v1.1.0 (Launcher)": "a1.1.0/a1.1.0-o-l",
    "Alpha v1.1.0": "a1.1.0/a1.1.0",
    "Alpha v1.1.1": "a1.1.1/a1.1.1",
    "Alpha v1.1.2": "a1.1.2/a1.1.2",
    "Alpha v1.1.2_01": "a1.1.2/a1.1.2_01",
    "Alpha v1.2.0": "a1.2.0/a1.2.0",
    "Alpha v1.2.0_01": "a1.2.0/a1.2.0_01",
    "Alpha v1.2.0_02": "a1.2.0/a1.2.0_02",
    "Alpha v1.2.0_02 (Launcher)": "a1.2.0/a1.2.0_02-l",
    "Alpha v1.2.1_01": "a1.2.1/a1.2.1_01",
    "Alpha v1.2.2 (Original)": "a1.2.2/a1.2.2-o",
    "Alpha v1.2.2": "a1.2.2/a1.2.2",
    "Alpha v1.2.3": "a1.2.3/a1.2.3",
    "Alpha v1.2.3_01 (Original)": "a1.2.3/a1.2.3-o",
    "Alpha v1.2.3_01": "a1.2.3/a1.2.3_01",
    "Alpha v1.2.3_02": "a1.2.3/a1.2.3_02",
    "Alpha v1.2.3_04": "a1.2.3/a1.2.3_04",
    "Alpha v1.2.3_05": "a1.2.3/a1.2.3_05",
    "Alpha v1.2.4_01": "a1.2.4/a1.2.4_01",
    "Alpha v1.2.5": "a1.2.5/a1.2.5",
    "Alpha v1.2.6": "a1.2.6/a1.2.6",
    "Beta 1.0": "b1.0/b1.0",
    "Beta 1.0_01": "b1.0/b1.0_01",
    "Beta 1.0.2": "b1.0/b1.0.2",
    "Beta 1.1 (Original)": "b1.1/b1.1-o",
    "Beta 1.1": "b1.1/b1.1",
    "Beta 1.1_01": "b1.1/b1.1_01",
    "Beta 1.1_02": "b1.1/b1.1_02",
    "Beta 1.2": "b1.2/b1.2",
    "Beta 1.2_01": "b1.2/b1.2_01",
    "Beta 1.2_02": "b1.2/b1.2_02",
    "Beta 1.2_02 (Launcher)": "b1.2/b1.2_02-l",
    "Beta 1.3 (Original)": "b1.3/b1.3-o",
    "Beta 1.3 (Reupload)": "b1.3/b1.3-r",
    "Beta 1.3": "b1.3/b1.3",
    "Beta 1.3 Demo": "b1.3/b1.3-d",
    "Beta 1.3_01": "b1.3/b1.3_01",
    "Beta 1.4 (Original)": "b1.4/b1.4-o",
    "Beta 1.4": "b1.4/b1.4",
    "Beta 1.4_01": "b1.4/b1.4_01",
    "Beta 1.5": "b1.5/b1.5",
    "Beta 1.5_01": "b1.5/b1.5_01",
    "Beta 1.6 Test Build 3": "b1.6/b1.6-tb3",
    "Beta 1.6": "b1.6/b1.6",
    "Beta 1.6.1": "b1.6/b1.6.1",
    "Beta 1.6.2": "b1.6/b1.6.2",
    "Beta 1.6.3": "b1.6/b1.6.3",
    "Beta 1.6.4": "b1.6/b1.6.4",
    "Beta 1.6.5": "b1.6/b1.6.5",
    "Beta 1.6.6": "b1.6/b1.6.6",
    "Beta 1.7": "b1.7/b1.7",
    "Beta 1.7_01": "b1.7/b1.7_01",
    "Beta 1.7.2": "b1.7/b1.7.2",
    "Beta 1.7.3": "b1.7/b1.7.3",
    "Beta 1.8 Pre-release 1 (Original)": "b1.8/b1.8-pre1-o",
    "Beta 1.8 Pre-release 1": "b1.8/b1.8-pre1",
    "Beta 1.8 Pre-release 2 (Original)": "b1.8/b1.8-pre2-o",
    "Beta 1.8 Pre-release 2": "b1.8/b1.8-pre2",
    "Beta 1.8": "b1.8/b1.8",
    "Beta 1.8.1": "b1.8/b1.8.1",
    "Beta 1.9 Pre-release 1": "b1.9/b1.9-pre1",
    "Beta 1.9 Pre-release 2": "b1.9/b1.9-pre2",
    "Beta 1.9 Pre-release 3 (Original)": "b1.9/b1.9-pre3-o",
    "Beta 1.9 Pre-release 3": "b1.9/b1.9-pre3",
    "Beta 1.9 Pre-release 4 (Original)": "b1.9/b1.9-pre4-o",
    "Beta 1.9 Pre-release 4 (Reupload)": "b1.9/b1.9-pre4-r",
    "Beta 1.9 Pre-release 4": "b1.9/b1.9-pre4",
    "Beta 1.9 Pre-release 5": "b1.9/b1.9-pre5",
    "Beta 1.9 Pre-release 6": "b1.9/b1.9-pre6",
    "1.0.0 Release Candidate 1": "1.0.0/1.0.0-rc1",
    "1.0.0 Release Candidate 2 (Original)": "1.0.0/1.0.0-rc2-o",
    "1.0.0 Release Candidate 2 (Reupload)": "1.0.0/1.0.0-rc2-r",
    "1.0.0 Release Candidate 2": "1.0.0/1.0.0-rc2",
    "1.0.0": "1.0.0/1.0.0"
}

pair = {
    "Classic 0.0.11a": "c0.0.11a",
    "Classic 0.0.12a_03": "c0.0.12a_03",
    "Classic 0.0.13a": "c0.0.13a",
    "Classic 0.0.13a_03": "c0.0.13a_03",
    "Classic 0.0.14a_08": "c0.0.14a_08",
    "Classic 0.0.15a": "c0.0.15a",
    "Classic 0.0.16a_02": "c0.0.16a_02",
    "Classic 0.0.17a": "c0.0.17a",
    "Classic 0.0.18a_02": "c0.0.18a_02",
    "Classic 0.0.19a_04": "c0.0.19a_04",
    "Classic 0.0.19a_06": "c0.0.19a_06",
    "Classic 0.0.20a_01": "c0.0.20a_01",
    "Classic 0.0.20a_02": "c0.0.20a_02",
    "Classic 0.0.21a": "c0.0.21a",
    "Classic 0.0.22a_05": "c0.0.22a_05",
    "Classic 0.0.23a_01": "c0.0.23a_01",
    "Classic 0.24_Survival_Test_03": "c0.24_st_03",
    "Classic 0.25_05 Survival Test": "c0.25_05_st",
    "Classic 0.27 Survival Test": "c0.27_st",
    "Classic 0.28_01": "c0.28_01",
    "Classic 0.29": "c0.29",
    "Classic 0.29_01": "c0.29_01",
    "Classic 0.29_02": "c0.29_02",
    "Classic 0.30 Survival": "c0.30s",
    "Classic 0.30 Creative": "c0.30c",
    "Classic 0.30 Creative (Renew)": "c0.30c_r",
    "Alpha v1.0.6": "a1.0.6",
    "Alpha v1.0.6_01": "a1.0.6_01",
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
    "Alpha v1.0.17_02": "a1.0.17_02",
    "Alpha v1.0.17_03": "a1.0.17_03",
    "Alpha v1.0.17_04": "a1.0.17_04",
    "Alpha v1.1.0 (Original)": "a1.1.0-o",
    "Alpha v1.1.0 (Launcher)": "a1.1.0-o-l",
    "Alpha v1.1.0": "a1.1.0",
    "Alpha v1.1.1": "a1.1.1",
    "Alpha v1.1.2": "a1.1.2",
    "Alpha v1.1.2_01": "a1.1.2_01",
    "Alpha v1.2.0": "a1.2.0",
    "Alpha v1.2.0_01": "a1.2.0_01",
    "Alpha v1.2.0_02": "a1.2.0_02",
    "Alpha v1.2.0_02 (Launcher)": "a1.2.0_02-l",
    "Alpha v1.2.1_01": "a1.2.1_01",
    "Alpha v1.2.2 (Original)": "a1.2.2-o",
    "Alpha v1.2.2": "a1.2.2",
    "Alpha v1.2.3": "a1.2.3",
    "Alpha v1.2.3_01 (Original)": "a1.2.3-o",
    "Alpha v1.2.3_01": "a1.2.3_01",
    "Alpha v1.2.3_02": "a1.2.3_02",
    "Alpha v1.2.3_04": "a1.2.3_04",
    "Alpha v1.2.3_05": "a1.2.3_05",
    "Alpha v1.2.4_01": "a1.2.4_01",
    "Alpha v1.2.5": "a1.2.5",
    "Alpha v1.2.6": "a1.2.6",
    "Beta 1.0": "b1.0",
    "Beta 1.0_01": "b1.0_01",
    "Beta 1.0.2": "b1.0.2",
    "Beta 1.1 (Original)": "b1.1-o",
    "Beta 1.1": "b1.1",
    "Beta 1.1_01": "b1.1_01",
    "Beta 1.1_02": "b1.1_02",
    "Beta 1.2": "b1.2",
    "Beta 1.2_01": "b1.2_01",
    "Beta 1.2_02": "b1.2_02",
    "Beta 1.2_02 (Launcher)": "b1.2_02-l",
    "Beta 1.3 (Original)": "b1.3-o",
    "Beta 1.3 (Reupload)": "b1.3-r",
    "Beta 1.3": "b1.3",
    "Beta 1.3 Demo": "b1.3-d",
    "Beta 1.3_01": "b1.3_01",
    "Beta 1.4 (Original)": "b1.4-o",
    "Beta 1.4": "b1.4",
    "Beta 1.4_01": "b1.4_01",
    "Beta 1.5": "b1.5",
    "Beta 1.5_01": "b1.5_01",
    "Beta 1.6 Test Build 3": "b1.6-tb3",
    "Beta 1.6": "b1.6",
    "Beta 1.6.1": "b1.6.1",
    "Beta 1.6.2": "b1.6.2",
    "Beta 1.6.3": "b1.6.3",
    "Beta 1.6.4": "b1.6.4",
    "Beta 1.6.5": "b1.6.5",
    "Beta 1.6.6": "b1.6.6",
    "Beta 1.7": "b1.7",
    "Beta 1.7_01": "b1.7_01",
    "Beta 1.7.2": "b1.7.2",
    "Beta 1.7.3": "b1.7.3",
    "Beta 1.8 Pre-release 1 (Original)": "b1.8-pre1-o",
    "Beta 1.8 Pre-release 1": "b1.8-pre1",
    "Beta 1.8 Pre-release 2 (Original)": "b1.8-pre2-o",
    "Beta 1.8 Pre-release 2": "b1.8-pre2",
    "Beta 1.8": "b1.8",
    "Beta 1.8.1": "b1.8.1",
    "Beta 1.9 Pre-release 1": "b1.9-pre1",
    "Beta 1.9 Pre-release 2": "b1.9-pre2",
    "Beta 1.9 Pre-release 3 (Original)": "b1.9-pre3-o",
    "Beta 1.9 Pre-release 3": "b1.9-pre3",
    "Beta 1.9 Pre-release 4 (Original)": "b1.9-pre4-o",
    "Beta 1.9 Pre-release 4 (Reupload)": "b1.9-pre4-r",
    "Beta 1.9 Pre-release 4": "b1.9-pre4",
    "Beta 1.9 Pre-release 5": "b1.9-pre5",
    "Beta 1.9 Pre-release 6": "b1.9-pre6",
    "1.0.0 Release Candidate 1": "1.0.0-rc1",
    "1.0.0 Release Candidate 2 (Original)": "1.0.0-rc2-o",
    "1.0.0 Release Candidate 2 (Reupload)": "1.0.0-rc2-r",
    "1.0.0 Release Candidate 2": "1.0.0-rc2",
    "1.0.0": "1.0.0"
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
        tkinter.messagebox.showerror("Download Failed", "Download failed (Error Code: 578)\nPlease check your internet connection.")

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
            "Classic 0.0.11a",
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
            "Alpha v1.1.0",
            "Alpha v1.1.1",
            "Alpha v1.1.2",
            "Alpha v1.1.2_01",
            "Alpha v1.2.0",
            "Alpha v1.2.0_01",
            "Alpha v1.2.0_02",
            "Alpha v1.2.0_02 (Launcher)",
            "Alpha v1.2.1_01",
            "Alpha v1.2.2 (Original)",
            "Alpha v1.2.2",
            "Alpha v1.2.3",
            "Alpha v1.2.3_01 (Original)",
            "Alpha v1.2.3_01",
            "Alpha v1.2.3_02",
            "Alpha v1.2.3_04",
            "Alpha v1.2.3_05",
            "Alpha v1.2.4_01",
            "Alpha v1.2.5",
            "Alpha v1.2.6",
            "Beta 1.0",
            "Beta 1.0_01",
            "Beta 1.0.2",
            "Beta 1.1 (Original)",
            "Beta 1.1",
            "Beta 1.1_01",
            "Beta 1.1_02",
            "Beta 1.2",
            "Beta 1.2_01",
            "Beta 1.2_02",
            "Beta 1.2_02 (Launcher)",
            "Beta 1.3 (Original)",
            "Beta 1.3 (Reupload)",
            "Beta 1.3",
            "Beta 1.3 Demo",
            "Beta 1.3_01",
            "Beta 1.4 (Original)",
            "Beta 1.4",
            "Beta 1.4_01",
            "Beta 1.5",
            "Beta 1.5_01",
            "Beta 1.6 Test Build 3",
            "Beta 1.6",
            "Beta 1.6.1",
            "Beta 1.6.2",
            "Beta 1.6.3",
            "Beta 1.6.4",
            "Beta 1.6.5",
            "Beta 1.6.6",
            "Beta 1.7",
            "Beta 1.7_01",
            "Beta 1.7.2",
            "Beta 1.7.3",
            "Beta 1.8 Pre-release 1 (Original)",
            "Beta 1.8 Pre-release 1",
            "Beta 1.8 Pre-release 2 (Original)",
            "Beta 1.8 Pre-release 2",
            "Beta 1.8",
            "Beta 1.8.1",
            "Beta 1.9 Pre-release 1",
            "Beta 1.9 Pre-release 2",
            "Beta 1.9 Pre-release 3 (Original)",
            "Beta 1.9 Pre-release 3",
            "Beta 1.9 Pre-release 4 (Original)",
            "Beta 1.9 Pre-release 4 (Reupload)",
            "Beta 1.9 Pre-release 4",
            "Beta 1.9 Pre-release 5",
            "Beta 1.9 Pre-release 6",
            "1.0.0 Release Candidate 1",
            "1.0.0 Release Candidate 2 (Original)",
            "1.0.0 Release Candidate 2 (Reupload)",
            "1.0.0 Release Candidate 2",
            "1.0.0",
        ])

        if select is None:
            sys.exit()
        elif "c" in pair[select]:
            asign = "com.mojang.minecraft.Minecraft"
        elif "a" in pair[select] or "b" in pair[select]:
            asign = "net.minecraft.client.Minecraft"
        else:
            asign = "net.minecraft.client.Minecraft"
        
        fp = current / f"{pair[select]}.jar"

        if select == "Alpha v1.1.1": 
            if easygui.buttonbox("This version had issue of Gamma\nDo you want to launch it?", "Warning", ["Yes", "No"]) == "No":
                sys.exit()
        
        cmd = f'{jbin} -Xmx1024M -Xms1024M -cp "launchwrapper-1.6.jar";"asm-all-4.1.jar";"jopt-simple-4.5.jar";"lwjgl.jar";"lwjgl_util.jar";"jinput.jar";"{pair[select]}.jar" -Djava.library.path="{current / "natives"}" -Dnet.java.games.input.librarypath="{current / "natives"}" -Djava.util.Arrays.useLegacyMergeSort=true -Dsun.java2d.opengl=true -Dorg.lwjgl.librarypath="{current / "natives"}" {asign} --tweakClass net.minecraft.launchwrapper.AlphaVanillaTweaker'
        if fp.exists():
            os.chdir(current)
            subprocess.Popen(cmd, shell=False, cwd=current)
            sys.exit()
        else:
            download(f"https://github.com/7alide/sal/raw/refs/heads/main/versions/{links[select]}.jar", f"{pair[select]}.jar")
            os.chdir(current)
            subprocess.Popen(cmd, shell=False, cwd=current)
            sys.exit()
    
    case "About":
        tkinter.messagebox.showinfo("About", f"Version: {jsoncheck().metadata['ver']}\nhttps://github.com/7alide/sal\nCopyright©️ 2026 7alide")

    case "Join Organisation":
        webbrowser.open("https://github.com/7alide")
    
    case "Exit":
        sys.exit()
    
    case None:
        sys.exit()