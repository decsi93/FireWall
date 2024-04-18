This Python script fetches a list of malicious IP addresses from Abuse CH's IP blocklist and dynamically adds them to your Windows firewall rules,
blocking both outgoing and incoming connections to those IPs.

Features

Retrieves the latest IP blocklist from Abuse CH
Filters out comment lines in the CSV data
Uses multithreading for concurrent outgoing and incoming rule creation
Provides a .bat file for easy execution with the -a argument to activate blocking
Requirements

Python 3 (tested with 3.12 versions)
requests library (pip install requests)
subprocess library (included in standard library)
threading library (included in standard library)
Windows PowerShell (pre-installed on Windows systems)
Installation

Download or clone this repository.
Install the requests library using pip install requests.
Usage

Open a command prompt or terminal and navigate to the project directory.

Run the script with the -a (activate) argument:

Bash
So that Windows Task Scheduler can run it easily.
(On my machines it's set to run every 10 minutes (because the database get's refreshed every 5 minutes) after any user logs in) 
python main.py -a
Use code with caution.
The script will download the IP blocklist, create firewall rules for each IP, and block both outgoing and incoming connections to those IPs.

Important Notes

This script modifies your Windows firewall rules. Use caution and review the IP blocklist before activating it.
The script assumes the IP blocklist format from Abuse CH. Changes in the format might require script modifications.
Consider creating a scheduled task to automatically update the firewall rules periodically.
Contributing

We welcome contributions to this project! Feel free to fork the repository, make changes, and submit pull requests.
