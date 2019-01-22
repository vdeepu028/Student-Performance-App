import tkinter
import tkinter.messagebox
import tkinter.ttk

class code1:
    
    def event_store(self):

        # To check whether the columns are filled properly !!!!!

        if self.textbox1.get()=="" or self.textbox2.get()=="" or self.textbox3.get()=="":
            tkinter.messagebox.showinfo("ERROR","all columns are mandatory to be filled properly according to the need")

        else:

            # Storing the event records in a file by file handling process
            self.file=open("eventlog.txt","a")
            self.file.write(self.textbox1.get())
            self.file.write("\n")
            self.file.write(self.textbox2.get())
            self.file.write("\n")
            self.file.write(self.textbox3.get())
            self.file.write("\n***********\n")
            # To give message to the user that event is added
            tkinter.messagebox.showinfo("info","EVENT ADDED SUCCESSFULLY!!!")
            self.file.close()
            self.event_win.destroy()
            
            
        
    def __init__(self):

        self.event_win = tkinter.Tk()

        # code1 window properties
        self.event_win.title(" ADD EVENT")
        self.event_win.geometry("280x200")
        self.event_win.resizable(0, 0)

        # Declaration of variables
        self.lb1 = tkinter.Label(self.event_win, text="Name of event")
        self.textbox1 = tkinter.Entry(self.event_win)
        self.textbox2 = tkinter.Entry(self.event_win)
        self.lb2 = tkinter.Label(self.event_win, text="Event Description")
        self.lb3 = tkinter.Label(self.event_win, text="Event Date")
        self.textbox3 = tkinter.Entry(self.event_win)
        self.bt1 = tkinter.Button(self.event_win, text="ADD EVENT",command=self.event_store)

        # Packing of Variables in a grid
        self.bt1.grid(row=3, column=1)
        self.lb1.grid(row=0, column=0)
        self.textbox1.grid(row=0, column=1)
        self.lb2.grid(row=1, column=0)
        self.textbox2.grid(row=1,column=1)
        self.lb3.grid(row=2,column=0)
        self.textbox3.grid(row=2,column=1)
        self.event_win.mainloop()
#---------------------------------------------------------------------------------------------
        
class code2:
    
    def participant_store(self):

        # To check whether the columns are filled properly !!!!!
        if self.textbox1.get()=="" or self.cb1.get()=="":
            tkinter.messagebox.showinfo("ERROR","all columns are mandatory to be filled properly according to the need")
            
        else:
            # To store the data input by the participant in a file
            self.file=open("participant_log.txt","a")
            self.file.write(self.textbox1.get())
            self.file.write("\n")
            self.file.write(self.textbox2.get())
            self.file.write("\n")
            self.file.write(self.textbox4.get())
            self.file.write("\n")
            self.file.write(self.cb1.get())
            self.file.write("**********\n")
            # To give message to the user that he is added in the event
            tkinter.messagebox.showinfo("info","YOU ARE ADDED SUCCESSFULLY IN "+str(self.cb1.get())+" EVENT")
            self.file.close()
            self.memb_win.destroy()

    
    def __init__(self):

        self.memb_win = tkinter.Tk()

        # code2 window properties
        self.memb_win.title(" ADD PARTICIPANT")
        self.memb_win.geometry("280x200")
        self.memb_win.resizable(0, 0)

        
        # Declaration of variables
        self.lb1 = tkinter.Label(self.memb_win,text="Name of Participant")
        self.textbox1 = tkinter.Entry(self.memb_win)
        self.lb2 = tkinter.Label(self.memb_win, text="Select Event")

        # Adding values to combobox using the record stored in file eventlog
        self.file=open("eventlog.txt","r")
        self.list1=[]

        while True:
            self.event_name=self.file.readline()
            if self.event_name=="":
                break
            self.des=self.file.readline()
            self.date=self.file.readline()
            self.sep=self.file.readline()
            self.list1.append(self.event_name)
        self.list1.sort()
        

        self.cb1 = tkinter.ttk.Combobox(self.memb_win,values=tuple(self.list1),state="readonly")
        self.lb3=tkinter.Label(self.memb_win,text="Rank of participant")
        self.textbox2 = tkinter.Entry(self.memb_win)
        self.lb4=tkinter.Label(self.memb_win,text="Enter your Email-ID")
        self.textbox4= tkinter.Entry(self.memb_win)
        self.bt1 = tkinter.Button(self.memb_win, text="ADD PARTICIPANT",command=self.participant_store)

        # Packing of Variables
        self.lb1.grid(row=0,column=0)
        self.textbox1.grid(row=0,column=1)
        self.lb3.grid(row=1,column=0)
        self.textbox2.grid(row=1,column=1)
        self.lb4.grid(row=2,column=0)
        self.textbox4.grid(row=2,column=1)
        self.lb2.grid(row=3,column=0)
        self.cb1.grid(row=3,column=1)
        self.bt1.grid(row=4,column=1)
        self.memb_win.mainloop()

#-------------------------------------------------------------------------------------------


# EVENT TREE VIEW CLASS
class code3:
    def __init__(self):
        self.treewin=tkinter.Tk()
        self.treewin.resizable(0,0)
        self.frame1=tkinter.Frame(self.treewin,height=680,width=1200)
        self.treewin.title(" EVENT RECORD ")
        self.t=tkinter.ttk.Treeview(self.frame1,selectmode="browse",columns=("Eventnm","descript","date"))
        self.t.column("#0",width=0)
        self.t.heading("Eventnm",text="EVENT NAME")
        self.t.heading("descript",text="DESCRIPTION")
        self.t.heading("date",text="DATE")
        self.rd=open("eventlog.txt","r")
        self.i=0
        ## READING DATA FROM eventlog.txt FILE -------
        while True:
            self.eventnm=self.rd.readline()
            if self.eventnm=="":
                break
            self.description=self.rd.readline()
            self.date=self.rd.readline()
            self.sep=self.rd.readline()
            ## INSERT VALUES IN TREEVIEW
            self.t.insert("",self.i,values=(self.eventnm,self.description,self.date))
            self.i=self.i+1
        
        self.t.pack(side="left")
        # Tree view scrollbar
        self.scrollbar=tkinter.ttk.Scrollbar(self.frame1,orient="vertical",command=self.t.yview)
        self.scrollbar.pack(side="right",fill="y")
        self.t.configure(yscrollcommand=self.scrollbar.set)
        self.frame1.pack()
        
        self.treewin.mainloop()
#-----------------------------------------------------------------------------------


class code4:

     def view(self):

        # To refresh the Tree-View
        for i in self.view.get_children():
            self.view.delete(i)

        # To read the file where data of participants are recorded
        self.file=open("participant_log.txt","r")
        self.i=0
        while True:
            self.name=self.file.readline()
            if self.name=="":
                break
            self.rank=self.file.readline()
            self.email=self.file.readline()
            self.event=self.file.readline()
            self.sep=self.file.readline()
            if self.event==self.cb1.get():
                # to insert the values in the tree-view
                self.view.insert("",self.i,values=(self.rank,self.name,self.email))
            self.i=self.i+1
                

     def __init__(self):

        # show_win window properties
        self.show_win=tkinter.Tk()
        self.show_win.resizable(0,0)
        self.show_win.title("CESS RECORD")

        # creation of frame and adding elements to it !!!
        self.frame1=tkinter.Frame(self.show_win,height=20,width=20)
        
        self.file=open("eventlog.txt","r")
        self.list1=[]
        
        while True:
            self.event=self.file.readline()
            if self.event=="":
                break
            self.desc=self.file.readline()
            self.date=self.file.readline()
            self.sep=self.file.readline()
            self.list1.append(self.event)
        self.list1.sort()

        self.cb1=tkinter.ttk.Combobox(self.frame1,values=tuple(self.list1))
        self.lb1=tkinter.Label(self.frame1,text="Enter the Event Name")
        self.bt1=tkinter.Button(self.frame1,text="VIEW",command=self.view)
        
        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)
        self.bt1.grid(row=1,column=1)
        self.frame1.pack()

        
        # Making of Tree-View to show records of the participants registered in particular event 
        self.view=tkinter.ttk.Treeview(self.show_win,selectmode="browse",columns=("rank","name","email"))
        self.view.column("#0",width=0)
        self.view.heading("rank",text="RANK")
        self.view.heading("name",text="NAME OF THE PARTICIPANT")
        self.view.heading("email",text="Email-ID")
        self.view.pack(side="left")

        # Tree view scrollbar
        self.scrollbar=tkinter.ttk.Scrollbar(self.show_win,orient="vertical",command=self.view.yview)
        self.scrollbar.pack(side="right",fill="y")
        self.view.configure(yscrollcommand=self.scrollbar.set)
        self.show_win.mainloop()

#---------------------------------------------------------------------------------------

def addEvent():
    x=code1()

def addMember():
    x=code2()

def showEvent():
    x=code3()

def showRecord():
    x=code4()


# MAIN WINDOW OF SOFTWARE IN WHICH MENU IS CREATED TO ACCESS VARIOUS  OPTIONS

main_win = tkinter.Tk()
main_win.resizable(0,0)
main_win.geometry("450x450")
mymenu = tkinter.Menu(main_win)
main_win.config(menu=mymenu)
sub1=tkinter.Menu(mymenu, tearoff=0)
mymenu.add_cascade(label="OPTIONS", menu=sub1)
sub1.add_command(label="ADD EVENTS", command=addEvent)
sub1.add_command(label="EVENT RECORD",command=showEvent)
sub1.add_command(label="ADD PARTICIPANT",command = addMember)
sub1.add_command(label="CESS RECORD",command=showRecord)
main_win.title(" CESS STUDENT PERFORMANCE")
label1 = tkinter.Label(main_win, text=" CESS DATABASE ", bg="mint cream", fg="black", font="HELVETICA 24")
label1.pack()
main_win.config(bg="misty rose")
pic = tkinter.PhotoImage(file="cess_logo.gif")
lbpic = tkinter.Label(main_win, image=pic, bg="misty rose")
lbpic.pack()
label2 = tkinter.Label(main_win, text=" MANAGEMENT ", bg="mint cream", fg="black", font="HELVETICA 24")
label2.pack()
main_win.mainloop()
