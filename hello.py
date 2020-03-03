# # # #
# # # #
# # # # def questions():
# # # #
# # # #     global canvas6,login,canvas4,canvas8,doctor_image,master,back_button
# # # #     if canvas5 is not None:
# # # #         canvas5.config(height=0, width=0)
# # # #         canvas5.delete("all")
# # # #     if canvas4 is not None:
# # # #         canvas4.config(height=0, width=0)
# # # #         canvas4.delete("all")
# # # #     if canvas8 is not None:
# # # #         canvas8.config(height=0, width=0)
# # # #         canvas8.delete("all")
# # # #     # if canvas6 is not None:
# # # #     #     canvas6.config(height=0, width=0)
# # # #     #     canvas6.delete("all")
# # # #     back.append(5)
# # # #     login=1
# # # #     #doctor_img.config(state="disabled", cursor="wait")
# # # #     toprightmostpart()
# # # #     canvas6 = Canvas(root, bg="white", width=100, height=100, bd=0, relief='ridge', highlightthickness=0)
# # # #     canvas6.place(x=100, y=475)
# # # #     canvas1 = Canvas(root, bg="white", width=root.winfo_screenwidth(), height=20, highlightbackground="black",
# # # #                      highlightthickness=5)
# # # #     canvas1.place(x=0, y=0)
# # # #     canvas1.create_text(root.winfo_screenwidth() / 2, 15, fill="black", font="Times 12 italic bold", text=" Medical Request Details")
# # # #     # master = Canvas(root, bg="black", width=500, height=200, bd=0, relief='ridge')
# # # #     # master.place(x=350, y=200)
# # # #     # Create a frame for the canvas and scrollbar(s).
# # # #     frame2 = tk.Frame(canvas7)
# # # #     frame2.grid(row=3, column=1, sticky=tk.NW)
# # # #            # Add a canvas in that frame.
# # # #     canvas = tk.Canvas(frame2)
# # # #     canvas.grid(row=0, column=0)
# # # #
# # # #     # Create a vertical scrollbar linked to the canvas.
# # # #     vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
# # # #     vsbar.grid(row=0, column=1, sticky=tk.NS)
# # # #     canvas.configure(yscrollcommand=vsbar.set)
# # # #
# # # #     # Create a horizontal scrollbar linked to the canvas.
# # # #     hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
# # # #     hsbar.grid(row=1, column=0, sticky=tk.EW)
# # # #     canvas.configure(xscrollcommand=hsbar.set)
# # # #
# # # #     # Create a frame on the canvas to contain the buttons.
# # # #     shipdetails_frame = tk.Frame(canvas, bg="Black", bd=2)
# # # #
# # # #     # Add the buttons to the frame.
# # # #     getQuestions(shipdetails_frame)
# # # #     # Create canvas window to hold the shipdetails_frame.
# # # #     canvas.create_window((0,0), window=shipdetails_frame, anchor=tk.NW)
# # # #
# # # #     shipdetails_frame.update_idletasks()  # Needed to make bbox info available.
# # # #     bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
# # # #     # print('canvas.bbox(tk.ALL): {}'.format(bbox))
# # # #
# # # #     # Define the scrollable region as entire canvas with only the desired
# # # #     # number of rows and columns displayed.
# # # #     w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
# # # #
# # # #     dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
# # # #     canvas.configure(scrollregion=bbox, width=dw, height=dh)
# # # #
# # # #     back_button = HoverButton(canvas6, image=photo_image9, width=80, height=backButton_height, bg="white",
# # # #                               borderwidth=0,
# # # #                               font=('Helvetica', '15'), command=backpage, cursor="hand2")
# # # #     back_button.place(x=10, y=25)
# # # #     #
# # # #     # label3 = tk.Label(root, text="Frame3 Contents", bg=LABEL_BG)
# # # #     # label3.grid(row=4, column=0, pady=5, sticky=tk.NW)
# # # #     #
# # # #     # frame3 = tk.Frame(master, bg="Blue", bd=2, relief=tk.GROOVE)
# # # #     # frame3.grid(row=5, column=0, sticky=tk.NW)
# # # #
# # # # def getQuestions(master):
# # # #     catQuestion = [i.questionaries for i in allQuestions if i.cat_name == symptomVariable.get()]
# # # #     i = 10
# # # #     if len(catQuestion[0]) > 0:
# # # #         for ques in catQuestion[0]:
# # # #             # for ques in quest:
# # # #             Label(master, font="Times 13", text=ques.name, bg="white", fg="blue", width=50).place(x=100, y=i)
# # # #             if ques.qus_type == 1:
# # # #                 var = StringVar()
# # # #                 Entry(master, textvariable=var, bd=3, width=11, font=font_size).place(x=500, y=i)
# # # #
# # # #                 entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(ques.ques_answers[0].ans_id) + "-" + str(
# # # #                     ques.qus_type)] = var
# # # #             elif ques.qus_type == 2:
# # # #                 a = 500
# # # #                 varRad = StringVar()
# # # #                 varRad.set(0)
# # # #                 for radPick in ques.ques_answers:
# # # #                     Radiobutton(master, text=radPick.name, variable=varRad, value=radPick.ans_id).place(x=a, y=i)
# # # #                     a = a + 100
# # # #                     entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(radPick.name) + "-" + str(
# # # #                         ques.qus_type)] = varRad
# # # #
# # # #             i = i + 40
# # # #         # Label(canvas7, font="Times 13", text="Other Information", bg="white", fg="blue", width=50).place(x=100, y=i)
# # # #         # OtherVariable = StringVar()
# # # #         # Text(canvas7, bd=3, width=11,height=2, font=font_size).place(x=500, y=i)
# # #
# # # from tkinter import *
# # # import tkinter as tk
# # # import database_Server as db
# # # canvas=None
# # # parent = Tk()
# # # canvas = tk.Canvas(parent, width=1000, height=100)
# # # canvas.create_oval(10, 10, 20, 20, fill="red")
# # # canvas.create_oval(200, 200, 220, 220, fill="blue")
# # #
# # #
# # # def getQuestions(canvas7):
# # #     print("im innnnnn")
# # #     entries = {}
# # #     allQuestions = db.getQuestions()
# # #     catQuestion = [i.questionaries for i in allQuestions if i.cat_name == "General accident"]
# # #     i = 10
# # #     if len(catQuestion[0]) > 0:
# # #         # canvas7.grid(row=0, column=0, sticky=N + S + E + W)
# # #         for ques in catQuestion[0]:
# # #             # for ques in quest:
# # #             Label(canvas, font="Times 13", text=ques.name, bg="white", fg="blue", width=50).grid(row=i + 1,
# # #                                                                                               column=15)
# # #             if ques.qus_type == 1:
# # #                 var = StringVar()
# # #                 Entry(canvas, textvariable=var, bd=3, width=11).grid(row=i,column=40)
# # #
# # #                 entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(ques.ques_answers[0].ans_id) + "-" + str(
# # #                     ques.qus_type)] = var
# # #             elif ques.qus_type == 2:
# # #                 a = 500
# # #                 varRad = StringVar()
# # #                 varRad.set(0)
# # #                 for radPick in ques.ques_answers:
# # #                     Radiobutton(canvas, text=radPick.name, variable=varRad, value=radPick.ans_id).grid(row=a + 1,
# # #                                                                                               column=40)
# # #                     a = a + 5
# # #                     entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(radPick.name) + "-" + str(
# # #                         ques.qus_type)] = varRad
# # #
# # #             i = i + 40
# # #
# # #
# # # getQuestions(canvas)
# # # canvas.grid(row=0, column=0)
# # #
# # # scroll_x = tk.Scrollbar(parent, orient="horizontal", command=canvas.xview)
# # # scroll_x.grid(row=1, column=0, sticky="ew")
# # #
# # # scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
# # # scroll_y.grid(row=0, column=1, sticky="ns")
# # #
# # # canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set,scrollregion=canvas.bbox("all"))
# # # # scrollbar.config(command=text.yview)
# # #
# # #
# # #
# # #
# # # mainloop()
# #
# # from tkinter import *
# # master = Tk()
# # import database_Server as db
#
# # def getQuestions(canvas7):
# #     print("im innnnnn")
# #     entries = {}
# #     allQuestions = db.getQuestions()
# #     catQuestion = [i.questionaries for i in allQuestions if i.cat_name == "General accident"]
# #     i = 10
# #     if len(catQuestion[0]) > 0:
# #         canvas7.grid(row=0, column=0, sticky=N + S + E + W)
# #         for ques in catQuestion[0]:
# #             # for ques in quest:
# #             Label(canvas7, font="Times 13", text=ques.name, bg="white", fg="blue", width=50).place(x=100, y=i)
# #             if ques.qus_type == 1:
# #                 var = StringVar()
# #                 Entry(canvas7, textvariable=var, bd=3, width=11).place(x=500, y=i)
# #
# #                 entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(ques.ques_answers[0].ans_id) + "-" + str(
# #                     ques.qus_type)] = var
# #             elif ques.qus_type == 2:
# #                 a = 500
# #                 varRad = StringVar()
# #                 varRad.set(0)
# #                 for radPick in ques.ques_answers:
# #                     Radiobutton(canvas7, text=radPick.name, variable=varRad, value=radPick.ans_id).place(x=a, y=i)
# #                     a = a + 100
# #                     entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(radPick.name) + "-" + str(
# #                         ques.qus_type)] = varRad
# #
# #             i = i + 40
# #
# #         # Label(canvas7, font="Times 13", text="Other Information", bg="white", fg="blue", width=50).place(x=100, y=i)
# #         # OtherVariable = StringVar()
# #         # Text(canvas7, bd=3, width=11,height=2, font=font_size).place(x=500, y=i)
# #     # canvas7.config(yscrollcommand=scrollbar.set)
# #     # scrollbar.config(command=canvas7.yview)
# # canvas = Canvas(master)
# # canvas.grid(row=0,column=0)
# # hbar = Scrollbar(master, orient=HORIZONTAL)
# # hbar.config(command=canvas.xview)
# # hbar.grid(row=1, column=0, sticky=E+W)
# # vbar = Scrollbar(master, orient=VERTICAL)
# # vbar.config(command=canvas.yview)
# # vbar.grid(row=0,column=1,sticky=N+S)
# # Label(canvas,"duihgughdug").grid(row=5,column=2)
# # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set,scrollregion=(0, 0, 1000, 1000))
# # # getQuestions(canvas)
# # master.mainloop()
#
# # from tkinter import *
# # master = Tk()
# # # import database_Server as db
# #
# # w = Canvas(master, width=50, height=200,
# #            borderwidth=0,
# #            highlightthickness=0,
# #            background='white'
# #           )
# # w.place(x=100,y=100)
# # label_msg = Label(w, font="Times 13", text="bugyguguhhbighuyg", bg="blue",  width=50)
# # label_msg.place(x=20, y=5)
# # hbar=Scrollbar(master,orient=HORIZONTAL)
# # hbar.pack(side=BOTTOM,fill=X)
# # hbar.config(command=w.xview)
# # w.config(xscrollcommand=hbar.set,scrollregion=(0, 0, 1000, 1000))
# # master.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# # listbox = Listbox(root)
# # listbox.pack()
# listbox = Label(root, font="Times 13", text="bugyguguhhbighuyg", bg="blue", width=50)
# # listbox.place(x=20, y=5)
# listbox.pack()
# a=10
# for i in range(100):
#     # listbox.insert(END, i)
#     listbox = Label(root, font="Times 13", text="bugyguguhhbighuyg", bg="blue", width=50)
#     listbox.place(x=20, y=a)
#     a+=20
# # attach listbox to scrollbar
# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
#
# mainloop()
import tkinter as tk  # python 3
# import Tkinter as tk  # python 2
import database_Server as db
class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.canvas =tk.Canvas(root, width=200, height=100, bg="white", bd=0, relief='ridge', highlightthickness=0) #tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.hsb = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.hsb.set,yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()


    def populate(self):
        varRad = tk.StringVar()
        varRad.set(0)
        entries = {}
        allQuestions = db.getQuestions()
        catQuestion = [i.questionaries for i in allQuestions if i.cat_name == 'General accident']
        i = 10
        if len(catQuestion[0]) > 0:
            # canvas7.grid(row=0, column=0, sticky=N + S + E + W)
            for ques in catQuestion[0]:
                # for ques in quest:
                tk.Label(self.frame, font="Times 13", text=ques.name, bg="white", fg="blue", width=50).grid(row=i, column=1)
                if ques.qus_type == 1:
                    var = tk.StringVar()
                    tk.Entry(self.frame, textvariable=var,bg="white", bd=3, width=30).grid(row=i, column=25)

                    entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(ques.ques_answers[0].ans_id) + "-" + str(
                        ques.qus_type)] = var
                elif ques.qus_type == 2:
                    a = 25
                    # varRad = tk.StringVar()
                    varRad.set(0)
                    for radPick in ques.ques_answers:
                        # varRad.set(0)
                        tk.Radiobutton(self.frame, text=radPick.name, variable=varRad,bg="white", value=radPick.ans_id).grid(row=i, column=a)
                        a = a + 10
                        entries[str(ques.q_id) + "-" + str(ques.name) + "-" + str(radPick.name) + "-" + str(
                            ques.qus_type)] = varRad

                i = i + 40



        '''Put in some fake data'''
        # a=0
        # for ques in catQuestion[0]:
        #     tk.Label(self.frame, text="%s" % a, width=3, borderwidth="1",
        #              relief="solid").grid(row=a, column=0)
        #     t=str(ques.name) %a
        #     tk.Label(self.frame, text=t).grid(row=a, column=1)
        #     a+=1
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()

    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()