# Introducing System Administration with Python
# Number 16

'''Exercise 1: Using os.system'''
# import os
# os.system("ls")

'''Exercise 2: Using subprocess.run'''
import subprocess
# subprocess.run("ls")

'''Exercise 3: Using subprocess.run with two arguments'''
# subprocess.run(["ls","-l"])

'''Exercise 4: Using subprocess.run with three arguments'''
# subprocess.run(["ls","-l","readme.md"])

'''Exercise 5: Retrieving system information'''
# command="uname"
# commandargument="-a"
# print(f'Gathering system information with command: {command} {commandargument}')
# subprocess.run([command,commandargument])

'''Exercise 6: Retrieving information about disk space'''
command='ps'
commandargument='-x'
print(f'Gathering system information with command: {command} {commandargument}')
subprocess.run([command,commandargument])