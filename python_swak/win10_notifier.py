# The provided Python script is a simple reminder application that uses the win10toast library to display Windows 10 toast notifications.
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()


def set_reminder():
    reminder_header = "Reminder Header\n"
    related_message = "Related Message\n"

    t = toaster.show_toast(
        title=f"{reminder_header}",
        msg=f"{related_message}",
    )


if __name__ == "__main__":
    set_reminder()
