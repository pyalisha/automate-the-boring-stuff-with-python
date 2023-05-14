from plyer import notification
import time

if __name__ == '__main__':

    while True:
        notification.notify(
            title = 'Take a break',
            message= 'You have been sitting for an hour',
            app_icon= 'C:\\Users\\alisha.khan\\Downloads\\walking.ico',
            timeout = 5
        )
        time.sleep(60*60) #1200 sec timer i.e.1hr

