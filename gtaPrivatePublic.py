import psutil
import time

PROCNAME = "GTA5.exe"
running = 1

while running:
    print('Please select a command to run!\n S: runs the script\n Q: exits the script')
    sel = input('Enter a command ')

    #Main script part
    if sel.lower() == "s":

        #Seach for PID of PROCNAME exe
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
            #Print and suspend the task specified in PROCNAME
                print(proc.ppid())

                proc.suspend()
                print("Paused")

                time.sleep(15)

                proc.resume()
                print("Resumed")
                break

    #Quitting script    
    elif sel.lower() == "q":
        running = 0