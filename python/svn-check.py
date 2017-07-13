import subprocess
import os

cmdout = subprocess.Popen("svn checkout https://adc.luxoft.com/svn/ODSTUDENTS/AYakovleva/", shell = True, stdout = subprocess.PIPE).stdout.read()
print(cmdout)

os.chdir("D:/tryingSVN/python/AYakovleva")

file = open('text.txt', 'a')
file.write('\n\nThis is python code.')
file.close()


cmdout = subprocess.Popen("svn status", shell = True, stdout = subprocess.PIPE).stdout.read()
print(cmdout)

cmdout = subprocess.Popen("svn add text.txt", shell = True, stdout = subprocess.PIPE).stdout.read()
print(cmdout)

cmdout = subprocess.Popen("svn commit -m \"new text added\"", shell = True, stdout = subprocess.PIPE).stdout.read()
print(cmdout)

