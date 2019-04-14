# 
# GUI界面
# 功能： 根据给定的时间，查找课程名，

from tkinter import *
from tkinter.ttk import Treeview
import tkinter.messagebox
import json
import re

tageOptions = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
stundenOptions = [x for x in range(0,24)]
minutenOptions = [x for x in range(0,60)]

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.amLabel = Label(self, text='am')
        self.amLabel.grid(row= 0 , column= 0, sticky= EW)
        #天 下拉菜单
        tageVariable = StringVar()
        tageVariable.set('Tag auswählen')
        self.tageOptionsMenu = OptionMenu(self, tageVariable, *tageOptions)
        self.tageOptionsMenu.grid(row= 0 , column= 1, sticky= EW)
        self.tageOptionsMenu.configure(width=20)

        self.vonLabel = Label(self, text='von')
        self.vonLabel.grid(row= 1 , column= 0, sticky= EW)
        #小时 下拉菜单
        anfangsStundeVariable = StringVar()
        anfangsStundeVariable.set('Stunde auswählen')
        self.anfangsStundenOptionsMenu = OptionMenu(self, anfangsStundeVariable, *stundenOptions)
        self.anfangsStundenOptionsMenu.grid(row= 1 , column= 1, sticky= EW)
        self.anfangsStundenOptionsMenu.configure(width=20)

        #分钟 下拉菜单
        anfangsMinutenVariable = StringVar()
        anfangsMinutenVariable.set('minute auswählen')
        self.anfangsMinutenOptionsMenu = OptionMenu(self, anfangsMinutenVariable, *minutenOptions)
        self.anfangsMinutenOptionsMenu.grid(row= 1 , column= 2, sticky= EW)
        self.anfangsMinutenOptionsMenu.configure(width=20)
        
        self.bisLabel = Label(self, text='bis')
        self.bisLabel.grid(row= 2 , column= 0, sticky= EW)
        #小时 下拉菜单
        endeStundeVariable = StringVar()
        endeStundeVariable.set('Stunde auswählen')
        self.endeStundenOptionsMenu = OptionMenu(self, endeStundeVariable, *stundenOptions)
        self.endeStundenOptionsMenu.grid(row= 2 , column= 1, sticky= EW)
        self.endeStundenOptionsMenu.configure(width=20)

        #分钟 下拉菜单
        endeMinutenVariable = StringVar()
        endeMinutenVariable.set('minute auswählen')
        self.endeMinutenOptionsMenu = OptionMenu(self, endeMinutenVariable, *minutenOptions)
        self.endeMinutenOptionsMenu.grid(row= 2, column= 2, sticky= EW)
        self.endeMinutenOptionsMenu.configure(width=20)

        #课程展示组件
        self.vsBar = Scrollbar(self.master)
        self.vsBar.grid(row=0,column =4, sticky= NS) 
        self.tree = Treeview(self.master, columns=('c1', 'c2', 'c3'), show="headings")
        self.vsBar.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsBar.set)

        self.tree.grid(row= 0, column= 3, sticky= NSEW)
        self.tree.column('c1', width=400, anchor='center')
        self.tree.column('c2', width=100, anchor='center')
        self.tree.column('c3', width=250, anchor='center')
        self.tree.heading('c1', text='Kurs')
        self.tree.heading('c2', text='Lehrer')
        self.tree.heading('c3', text='Zeitraum')

        #确认按键
        self.doneButton = Button(self, text = 'done', command=lambda: self.checkTheList(self.tree, tageVariable.get(), anfangsStundeVariable.get(), anfangsMinutenVariable.get(), endeStundeVariable.get(), endeMinutenVariable.get()))  
        self.doneButton.grid(row= 4 , column= 1, sticky= EW)
        #退出按键
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row= 4 , column= 2, sticky= EW)
    
    def checkTheList(self, treeBox, tag, aStunde, aMinute, eStunde, eMinute):
        try:
            if treeBox.get_children() is not None:
                treeBox.delete(*treeBox.get_children())
            if tag and aStunde and aMinute and eStunde and eMinute:
                f = open("TU_Spider/fachbereich_list.json", 'r', encoding='GBK')
                pattern = re.compile(r'.*}')
                for line in f.readlines():
                    #print(pattern.search(line).group(0))
                    dic = json.loads(pattern.search(line).group(0))
                    if tag[0:2] in dic['zeitraum']: 
                        zeit = re.findall(r'\[[0-9]{2}:[0-9]{2}\]', dic['zeitraum']) #z.B. zeit = ['[09:50]', '[16:05]']
                        if int(zeit[0][1:3]) > int(aStunde) or ( int(zeit[0][4:6]) >= int(aMinute) and int(zeit[0][1:3]) == int(aStunde) ):
                            if int(zeit[1][1:3]) < int(eStunde) or ( int(zeit[1][4:6]) <= int(eMinute) and  int(zeit[1][1:3]) == int(eStunde)):
                                treeBox.insert("", 1, text="" ,values=(dic['name'], dic['lehrer'], dic['zeitraum']))
        finally:
            f.close()

app = Application()
# 设置窗口标题:
app.master.title('TU Assist')
# 设置窗口大小
app.master.geometry('1200x300')
app.master.resizable(False,False)
# 主消息循环:
app.mainloop()