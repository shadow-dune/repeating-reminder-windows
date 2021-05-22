# show a notification every 1500 seconds to take a break
from win10toast import ToastNotifier
from time import sleep

toast = ToastNotifier()

while True:
    #Edit this line to change the title and description of the notification
    toast.show_toast("Reminder", "Take a break!")
    #Edit this line to change the delay (in seconds)
    sleep(1500)
