logo = '''
┌─────────────────────────────────────────────────┐
│ ██████╗███████╗ █████╗ ███████╗███████╗██████╗  │
│██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗ │
│██║     █████╗  ███████║███████╗█████╗  ██████╔╝ │
│██║     ██╔══╝  ██╔══██║╚════██║██╔══╝  ██╔══██╗ │
│╚██████╗███████╗██║  ██║███████║███████╗██║  ██║ │
│ ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ │
│                                                 │
│ ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗ │
│██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗│
│██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝│
│██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗│
│╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║│
│ ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝│
└─────────────────────────────────────────────────┘ '''

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

from os import system , name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')