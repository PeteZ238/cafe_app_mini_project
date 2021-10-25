import subprocess
import platform
import tabulate
import modules.print_statements as print_statements

def clear():
    '''Function that clears the terminal screen.'''
    if platform.system() == 'Windows':
        subprocess.run('cls', shell = True)
    else:
        subprocess.run('clear', shell = True)

