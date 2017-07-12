"""import subprocess
cmdout = subprocess.Popen("dir", shell = True, stdout = subprocess.PIPE).stdout.read()
print(cmdout)

text = '5'
proc = subprocess.Popen(
    './double',stdout=subprocess.PIPE,
    stdin=subprocess.PIPE)
proc.stdin.write(text.encode())
proc.stdin.close()
result = proc.stdout.read()
print (result)
proc.wait()
"""

import subprocess

def funcRead(x):
        proc = subprocess.Popen("prog1", 
                        stdout = subprocess.PIPE,
                        stdin = subprocess.PIPE)
        
        proc.stdin.write(text[num].encode())
        proc.stdin.close()
        cmdout = proc.stdout.read()

        file.write(text[num] +'\t' + cmdout.decode() + '\n')
        return cmdout


errors = 0
i=0
text = ['1', '2', '5']
file = open('report.txt', 'w')
while (i != 10):
    num = 0
    while (num < 3):
        cmdout = funcRead(num)        

        print(cmdout)
        if (cmdout == b'toto'):
            errors += 1
        num += 1
    
    i += 1
file.write('\n' + 'Error\'s amount\n' + str(errors))    
file.close()

