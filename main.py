import os

LINE = "Synchronized passive-aggressive dishwashing: two teammates, one sink, zero eye contact, judged on sigh volume and plate-clatter precision."

# Broadcast-plain, absurd underneath: the event must sound real until the judging criteria land.
assert LINE.count(":") == 1

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    print(LINE, file=f)
