"""import subprocess

cmdout = subprocess.Popen("dir", shell = True, stdout = subprocess.PIPE).stdout.read()

print(cmdout)
"""

import subprocess

text = '1'
proc = subprocess.Popen("prog1", 
                        stdout = subprocess.PIPE,
                        stdin = subprocess.PIPE)
proc.stdin.write(text.encode())
proc.stdin.close()
cmdout = proc.stdout.read()

print(cmdout)
proc.wait()
"""
for(i = '1'; i < '5'; i++) {
    proc = subprocess.Popen("prog1", 
                        stdout = subprocess.PIPE,
                        stdin = subprocess.PIPE)
    proc.stdin.write(i.encode())
    proc.stdin.close()
    cmdout = proc.stdout.read()

    print("cmdout ")
    proc.wait()
    
}
"""
