import subprocess
import platform

def clear():
    '''Function that clears the terminal screen.'''
    if platform.system() == 'Windows':
        subprocess.run('cls', shell = True)
    else:
        subprocess.run('clear', shell = True)