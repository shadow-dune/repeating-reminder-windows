# show a notification every 1500 seconds to take a break
from win10toast import ToastNotifier
from time import sleep

toast = ToastNotifier()

while True:
    toast.show_toast("Reminder", "Take a break!")
    sleep(1500)