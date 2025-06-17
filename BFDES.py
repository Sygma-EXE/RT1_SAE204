#############################################################################################
#I like having a simple interface for the thing i make, even if this is useless" - Sygma.EXE#
#############################################################################################

import os
import questionary

choice = questionary.select(
    '\n'
    '+-------------------------------------+\n'
    '|   __________________ _____ _____    |\n'
    '|   | ___ \  ___|  _  \  ___/  ___|   |\n'
    '|   | |_/ / |_  | | | | |__ \ `--.    |\n'
    '|   | ___ \  _| | | | |  __| `--. \   |\n'
    '|   | |_/ / |   | |/ /| |___/\__/ /   |\n'
    '|   \____/\_|   |___/ \____/\____/    |\n'
    '+-------------------------------------+\n'
    '| Please choose what type of BFDES you|\n'
    '|            want to use?             |\n'
    '+-------------------------------------+\n',
    choices=[
    '[ 1 - Brute Force CPU Thread  ]',
    '[ 2 - Brute Force CPU Process ]',
    '[ 3 - Brute Force GPU CUDA    ]',
    '[ 4 - Test Version CUDA       ]'
    ]
).ask()

if choice == '[ 1 - Brute Force CPU Thread  ]':
    print(" Starting BFDEScputhread.py...")
    print("+-------------------------------------+")
    os.system("python3 BFDEScputhread.py")
elif choice == '[ 2 - Brute Force CPU Process ]':
    print(" Starting BFDEScpuprocess.py...")
    print("+-------------------------------------+")
    os.system("python3 BFDEScpuprocess.py")
elif choice == '[ 3 - Brute Force GPU CUDA    ]':
    print(" Starting BFDESgpucuda.py...")
    print("+-------------------------------------+")
    os.system("python3 BFDESCUDA/BFDESgpucuda.py")
elif choice == '[ 4 - Test Version CUDA       ]':
    print(" Starting CUDAtest.py...")
    print("+-------------------------------------+")
    os.system("python3 BFDESCUDA/CUDAtest.py")