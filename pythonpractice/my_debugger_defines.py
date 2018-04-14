from ctypes import *

# Let's map the Microsoft types to ctypes for clarity
WORD    = c_short
DWORD   = c_ulong
LPBYTE  = POINTER(c_ubyte)
LPSTR   = POINTER(c_char)
HANDLE  = c_void_p

# Constants
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# Structures for CreateProcessA() function
class STARTUPINFO(Structure):
    _fields_ = [
        ("cd",             DWORD),
        ("lpReserved",     LPSTR),
        ("lpReserved",     LPSTR),
        ("lpTitle",        LPSTR),
        ("dwX",            DWORD),
        ("dwY",            DWORD),
        ("dwXSize",        DWORD),
        ("dwYSize",        DWORD),
        ("dwXCountChars",  DWORD),
        ("dwYCountChars",  DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags",        DWORD),
        ("wShowWindow",     WORD),
        ("cbReserved2",     WORD),
        ("lpReserved2",   LPBYTE),
        ("hStdInput",     HANDLE),
        ("hStdOutput",    HANDLE),
        ("hStdError",     HANDLE),
    ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess",     HANDLE),
        ("hThread",      HANDLE),
        ("dwProcessId",   DWORD),
        ("dwThreadId",    DWORD),
    ]