import ctypes
import os

add_int = ctypes.CDLL(os.getcwd()+"/add_int.so")

print(add_int.add(4,7))
