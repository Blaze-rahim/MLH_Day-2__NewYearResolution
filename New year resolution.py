from plyer import notification
import time

def message():
    title = "HELLO ABDUL"
    message = "Keep Coding You Are Doing Great"
    notification.notify(title= title,
                        message= message,
                        app_icon = None,
                        timeout= 10,
                        toast=False)

while(True):
    message()
    time.sleep(1800)