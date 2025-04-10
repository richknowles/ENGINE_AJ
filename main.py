from app.aj_driver import get_driver
from app.aj_sender import send_message
import pandas as pd

driver = get_driver()
input("Scan the QR code, then press Enter to begin...")

df = pd.read_csv("recipients.csv")
for _, row in df.iterrows():
    send_message(driver, row["number"], row["message"])
