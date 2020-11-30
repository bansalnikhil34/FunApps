import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="!!!! Please Drink Water !!!",
            message="Benefits of drinking water" \
                    "It may improve memory and mood." \
                    "It can help reduce sugar cravings and aid weight maintenance." \
                    "It may improve exercise performance" \
                    "It may reduce headaches and migraines",
            app_icon="/home/local/SIRIONLABS/nikhil.bansal/Desktop/python/FunApps/DrinkWater/icon.ico",
            timeout=10
        )
        time.sleep(60*60)
