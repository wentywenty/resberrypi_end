import os
def getcpu():
    cmd=os.popen('vcgencmd measure_temp').readline()
    temp=float(cmd.replace("temp=","").replace("C\n",""))
    return temp
if _name_=='_main_':
    cpu=getcpu()
    print("temp=",cpu)
