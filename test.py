import time
import requests

while True:
    requests.post('https://api.hamsterkombatgame.io/clicker/tap', json={"count": 1, "availableTaps": 7985, "timestamp": int(time.time(
    ))}, headers={'authorization': 'Bearer 1721404196118KUrtNIJOPHRKbWUQsDhytjGuEKpEJ1wtDprAiDpqsB63dZyxev87W1xQHFYJYFC66749177065'})
    time.sleep(3600)
