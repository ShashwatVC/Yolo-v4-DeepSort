# listener.py

import subprocess

process = subprocess.Popen(['python', 'object_tracker.py'], stdout=subprocess.PIPE)
# stdout, stderr = process.communicate() # not useful for this example cause communicate will wait for the process to finish

while process.poll() is None:
    result = process.stdout.readline().decode()
    print(result.strip())