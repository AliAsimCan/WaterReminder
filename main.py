import time
from plyer import notification

if __name__== '__main__':
    while True:
        notification.notify(
            title = "**PLEASE DRİNK WATER NOW!!",
            message = "DRİNKİNG WATER Helps to Maintain the Balance of Body Fluids.",
            timeout = 10
            )
        time.sleep(60*60)
