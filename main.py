from requests import get
from csv import reader
from subprocess import run
from threading import Thread

# source = Abuse CH
response = get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text
run(["powershell", "-Command", "netsh advfirewall firewall delete rule name='BadIP'"])

myCSV = reader(filter(lambda x: not x.startswith("#"), response.splitlines()))


def outgoing():
    for row in myCSV:
        ip = row[1]
        if ip != "dst_ip":
            run(["powershell", "-Command",
                 "netsh advfirewall firewall add rule name='BadIP' Dir=Out Action=Block RemoteIP=" + ip])


def incoming():
    for row in myCSV:
        ip = row[1]
        if ip != "dst_ip":
            run(["powershell", "-Command",
                 "netsh advfirewall firewall add rule name='BadIP' Dir=In Action=Block RemoteIP=" + ip])


t1 = Thread(outgoing())
t2 = Thread(incoming())
t1.start()
t2.start()
