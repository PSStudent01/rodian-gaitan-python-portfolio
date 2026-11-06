
'''
Demonstrates a third-party package (colorama) installed with pip.
Requires colorama so installed by doing <pip install colorama>
'''

from colorama import init, Fore, Style

init()  # makes colors work on Windows terminals

print(Fore.BLUE + "This text is in blue!")
print(Fore.RED + "This text is in red!")
print(Style.RESET_ALL + "Returns back to normal text")
