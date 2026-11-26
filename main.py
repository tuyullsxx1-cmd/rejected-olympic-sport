import os

LINE = "Synchronized passive-aggressive dishwashing: two teammates, one sink, zero eye contact, judged on sigh volume and plate-clatter precision."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    print(LINE, file=f)
