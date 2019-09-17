import subprocess
import os
def testu():
#    while True:
    print(os.popen('ls').read())
    #print(os.spawnl(os.P_DETACH, "python3 commentbot/python_scripts/comments_bot.py &"))
    subprocess.call('ls')
    p = subprocess.Popen(["python3", "            commentbot/python_scripts/comments_bot.py", "&"], stdout=subprocess.PIPE)
    print(p.communicate())
    #exec('comments_bot.py')
    print("test 0K")