import os
from subprocess import STDOUT, check_call


check_call(['sudo', 'code', '--user-data-dir="~/.vscode-root"'], stderr = STDOUT)
check_call(['gnome-terminal'], stderr = STDOUT)
#check_call(['setsid', 'midori', '&'], stderr = STDOUT)
check_call(['midori', '&'], stderr = STDOUT)