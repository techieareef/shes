import subprocess
import zipfile
import time
import psutil
import os
from pathlib import Path
import shutil
from tkinter import *
def updatetask(text):
    var.set(text)
    canvas.update_idletasks()
def troubleshoot():
    global canvas,text_data
    if canvas is not None:
        canvas.config(height=0, width=0)
        canvas.delete("all")
        button1.destroy()
        button2.destroy()
    button1.destroy()
    button2.destroy()
    canvas.config(height=0, width=0)
    canvas.delete("all")
    # # canvas = Canvas(width=300, height=300, bg='white')
    # # canvas.pack(expand=YES, fill=BOTH)
    canvas = Canvas(window, bg="white", width=1100, height=350, bd=0, relief='ridge',
                     highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)

    print("trouble shoot started")
    updatetask("Starting the Troupleshoot...")

    # text_data.config(text="hello world")
    dir_cur = os.path.dirname(os.path.realpath(__file__))
    ## If file exists, delete it ##
    if os.path.isdir(dir_cur+'/Tools'):
        # os.remove(dir_cur+"/Tools")
        shutil.rmtree(dir_cur+'/Tools')
    if os.path.isfile(dir_cur+'/soujhehome.zip'):

        os.remove(dir_cur+'/soujhehome.zip')
    # time.sleep(1)
    # var.set("                     ")
    # window.update_idletasks()

    time.sleep(1)
    updatetask("Tools dir added...              ")


    ## Show an error ##
    dir_cur = os.path.abspath(os.path.dirname(__file__))
    dirnew = dir_cur + '\\Tools'
    p = Path(dirnew)
    updatetask("Adding Folder Structure Data...                     ")
    if not (p.exists() and p.is_dir()):  # create Log dir if one does not exist
        os.makedirs(dirnew)
    log = open('Tools/Folder_Details.txt', 'w')
    log.write('\n\n\n================Folder Structure =============\n\n')
    log.flush()  # <-- here's something not to forget!
    c = subprocess.Popen(['dir', '/S'], stdout=log, stderr=log, shell=True)
    log.close()
    time.sleep(1)
    updatetask("Checking Cpu Status...                 ")
    # gives an object with many fields
    log1 = open('Tools/cpu file.txt', 'w')
    log1.write(("\n\n==================================cpu utilization=======================\n\n\n"))
    log1.flush()
    log1.write("\n\n\n===========convert that object ======================\n\n\n")
    log1.write(str(psutil.virtual_memory()))


    log1.write("\n\n\n===========cpu process listings======================\n\n\n")
    procs = list(psutil.process_iter())
    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs=('pid', 'name', 'cpu_percent'))


        current_process = psutil.Process(pid=pinfo['pid'])
        # print(current_process)
        #
        pinfo["cpu_info"] = current_process.cpu_percent(interval=0.1)
        # processes_info.append(pinfo)

        log1.write(str(pinfo) + '\n')

    # cpu utilization
    log1.write("\n\n\n===========CPU present utilization ======================\n\n\n")
    log1.write("Present CPU process utilization: " + str(psutil.cpu_percent()))
    log1.close()
    updatetask("Collecting the Information...                    ")
    # print("==========================wait=======================")
    time.sleep(1)
    dir_cur1 =dir_cur+"/Const"
    fantasy_zip = zipfile.ZipFile(str(dir_cur) + '\soujhehome.zip', 'a')

    for folder, subfolders, files in os.walk(dir_cur):

        for file in files:
            if file.endswith('.log') or file.endswith('.db') or file.endswith('.json'): #or file.endswith('.jpg') or file.endswith('.png'):
                fantasy_zip.write(os.path.join(folder, file),
                                  os.path.relpath(os.path.join(folder, file), dir_cur),
                                  compress_type=zipfile.ZIP_DEFLATED)
            # if file.endswith('.json'):
            #     fantasy_zip.write(os.path.join(folder, file),
            #                       os.path.relpath(os.path.join(folder, file), dir_cur+"/Const"),
            #                       compress_type=zipfile.ZIP_DEFLATED)
            if file.endswith('.txt'):
                fantasy_zip.write(os.path.join(folder, file),
                                  os.path.relpath(os.path.join(folder, file), str(dir_cur) + '\Tools'),
                                 compress_type=zipfile.ZIP_DEFLATED)


    fantasy_zip.close()
    updatetask("Successfully compleated...                 ")
    time.sleep(2)
    window.destroy()
def close_support():
    # print("close support called")
    try:
        window.destroy()
    except:
        try:
            os.system("taskkill /f /im Troubleshoot.exe 1>nul")
        except:
            window.destroy()
window = Tk()

window.state('zoomed')
window.title('Trouble shooting started....')
global button1,button2
canvas=None
var = StringVar()
var.set('hello')



# canvas = Canvas(width=300, height=300, bg='white')
canvas = Canvas(window, bg="white", width=1100, height=350, bd=0, relief='ridge',
                     highlightthickness=0)
canvas.pack(expand=YES, fill=BOTH)
l = Label(canvas, textvariable = var, bg='white')
l.place(x=50,y=50)

button1 = Button(window, text="Start Trouble shoot", command=lambda:troubleshoot() , anchor=W,bg="white",activebackground="#33B5E5")
button1.place(x=10,y=10)

button2 = Button(window, text="Exit Trouble shoot", command=lambda:close_support() , anchor=W,bg="white",activebackground="#33B5E5")
button2.place(x=150,y=10)



window.protocol("WM_DELETE_WINDOW", close_support)
window.mainloop()