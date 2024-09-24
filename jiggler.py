# jiggler.py

import ctypes


def jiggle_mouse():
    # Use ctypes to simulate real mouse movement event
    INPUT_MOUSE = 0
    MOUSEEVENTF_MOVE = 0x0001

    class MOUSEINPUT(ctypes.Structure):
        _fields_ = [
            ("dx", ctypes.c_long),
            ("dy", ctypes.c_long),
            ("mouseData", ctypes.c_ulong),
            ("dwFlags", ctypes.c_ulong),
            ("time", ctypes.c_ulong),
            ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
        ]

    class INPUT(ctypes.Structure):
        _fields_ = [("type", ctypes.c_ulong), ("mi", MOUSEINPUT)]

    extra = ctypes.c_ulong(0)
    ii = INPUT(
        type=INPUT_MOUSE,
        mi=MOUSEINPUT(
            dx=1,
            dy=1,
            mouseData=0,
            dwFlags=MOUSEEVENTF_MOVE,
            time=0,
            dwExtraInfo=ctypes.pointer(extra),
        ),
    )
    ctypes.windll.user32.SendInput(1, ctypes.byref(ii), ctypes.sizeof(ii))
