import subprocess
import zipfile
import time
import psutil
import os
from pathlib import Path
import shutil

# global canvas, text_data
# if canvas is not None:
#     canvas.config(height=0, width=0)
#     canvas.delete("all")
#     button1.destroy()
#     button2.destroy()
# button1.destroy()
# button2.destroy()
# canvas.config(height=0, width=0)
# canvas.delete("all")
# # canvas = Canvas(width=300, height=300, bg='white')
# # canvas.pack(expand=YES, fill=BOTH)
# canvas = Canvas(window, bg="white", width=1100, height=350, bd=0, relief='ridge',
#                 highlightthickness=0)
# canvas.pack(expand=YES, fill=BOTH)

# print("trouble shoot started")
print("Starting the collection of necessary files ...")
#
# text_data.config(text="hello world")
dir_cur = os.path.dirname(os.path.realpath(__file__))
## If file exists, delete it ##
if os.path.isdir(dir_cur + '/Tools'):
    # os.remove(dir_cur+"/Tools")
    shutil.rmtree(dir_cur + '/Tools')
if os.path.isfile(dir_cur + '/Soujhe_Support_Details.zip'):
    os.remove(dir_cur + '/Soujhe_Support_Details.zip')
# time.sleep(1)
# var.set("                     ")
# window.update_idletasks()

time.sleep(1)
print("Tools dir created ...              ")

## Show an error ##
dir_cur = os.path.abspath(os.path.dirname(__file__))
dirnew = dir_cur + '\\Tools'
p = Path(dirnew)
print("Adding folder structure details...                     ")
if not (p.exists() and p.is_dir()):  # create Log dir if one does not exist
    os.makedirs(dirnew)
log = open('Tools/Folder_Details.txt', 'w')
log.write('\n\n\n================Folder Structure =============\n\n')
log.flush()  # <-- here's something not to forget!
c = subprocess.Popen(['dir', '/S'], stdout=log, stderr=log, shell=True)
log.close()
time.sleep(1)
print("Capturing CPU Stats...                 ")
# gives an object with many fields
log1 = open('Tools/cpu_dtls.txt', 'w')
log1.write(("\n\n==================================CPU utilization=======================\n\n\n"))
log1.flush()
log1.write(str(psutil.virtual_memory()))

log1.write("\n\n\n===========CPU Processes details======================\n\n\n")
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
log1.write("\n\n\n===========Current CPU Utilization ======================\n\n\n")
log1.write("System CPU Utilization : " + str(psutil.cpu_percent()))
log1.close()
print("Collecting the Config files...                    ")
# print("==========================wait=======================")
time.sleep(1)
dir_cur1 = dir_cur + "/Const"
fantasy_zip = zipfile.ZipFile(str(dir_cur) + '\Soujhe_Support_Details.zip', 'a')

for folder, subfolders, files in os.walk(dir_cur):

    for file in files:
        if file.endswith('.log') or file.endswith('.db') or file.endswith(
                '.json'):  # or file.endswith('.jpg') or file.endswith('.png'):
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
print("Successfully completed collecting required details...                 ")
time.sleep(2)
print("Please mail us the file : "+str(dir_cur)+"\Soujhe_Support_Details.zip")
time.sleep(2)
os._exit(0)
#os.system("taskkill /f /im Troubleshoot.exe 1>nul")