import subprocess


def wifiPassword(name):
    try:
        results = (
            subprocess.check_output(
                ["netsh", "wlan", "show", "profile", name, "key=clear"]
            )
            .decode("utf-8")
            .split("\n")
        )
    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(name, "ENCODING ERROR"))

    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        return results[0]
    except IndexError:
        return ""
