# inactivity.py

import ctypes


# Define the structure for LASTINPUTINFO
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]


def check_idle_duration():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))

    # Get the current tick count (time since the system started)
    millis = ctypes.windll.kernel32.GetTickCount()

    # Calculate the idle time in seconds
    idle_time = (millis - lii.dwTime) / 1000.0
    return idle_time
