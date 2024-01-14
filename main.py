import subprocess
from PyInquirer import prompt
from wifipwd import wifiPassword


data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

question = [
    {
        "type": "list",
        "name": "wifi",
        "message": "Choose the wifi whose password you want to see",
        "choices": profiles,
    }
]
answer = prompt(question)
wifiName = answer["wifi"]
results = wifiPassword(wifiName)

try:
    print("{:<30}|  \033[92m{:<}\033[00m".format(wifiName, results))

except IndexError:
    print("{:<30}|  {:<}".format(wifiName, ""))
