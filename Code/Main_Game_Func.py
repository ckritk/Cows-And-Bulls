from tkinter import *
from tkinter import ttk,messagebox,END
from random import randrange
import mysql.connector as c
import datetime as dt
from CowsAndBulls.ProgrammableTimerApp import ProgrammableTimerApp

def Main_Game_Func():
    from CowsAndBulls.stfunc import stfunc

    root=Tk()
    root['bg']='lavender'
    root.geometry('780x540')

    def START():

        def Start():
            if cncombo.get(): starttime = dt.datetime.time(dt.datetime.now())
            else: return

                      
            n=int(cncombo.get())

            def new_func(n):   
                cnlbl.destroy();cncombo.destroy();cncmd.destroy(); tlbl.destroy(); stcmd.destroy()

                restart=Button(root,text='RESTART',font=("Cambria",14),width=13,fg='lavender',bg='navy',command=lambda : new_func(n));
                #restart.place(x=532,y=70)

                timer=ProgrammableTimerApp(root,682,58)
                timer.start_timer()

                if n in (3,4): mn=11
                elif n in (5,6,7): mn=16
                elif n in (8,9,10): mn=26
                            
                code=str(randrange(0,10))
                while len(code)<n:
                    x=str(randrange(0,10))
                    if x not in code: code+=x
                #print(code)
                tno=[1,True]

                style = ttk.Style()
                style.configure("mystyle.Treeview", font=("Cambria",14))
                style.configure("mystyle.Treeview.Heading", font=("Cambria",15,'bold'))

                columns= (' ','Trial','Cows','Bulls')
                wth=[40,170,100,100]
                tree = ttk.Treeview(root, columns=columns, show='headings',height=20,style='mystyle.Treeview')
                for i in range(len(columns)):
                                    tree.heading(columns[i],text=columns[i])
                                    tree.column(columns[i],width=wth[i])
                tree.place(x=80,y=80)

                tentry=Entry(root,font=("Californian FB",14),bd=3,width=15); tentry.place(x=533,y=310)

                def START__(): 
                        timer.remove_timer_display(); tree.destroy(); tentry.destroy(); ok.destroy(); back.destroy(); restart.destroy(); START()

                                
                def OK():
                    if tentry.get().isdigit() and len(tentry.get())==n and tno[0]<mn and tno[1]:
                        cows=bulls=0; Cows, Bulls=[],[]
                        for i in code:
                            if i in tentry.get():
                                if tentry.get()[code.index(i)]==i: Cows+=[i]
                                else : Bulls+=[i]
                        #print(Cows,'-------',Bulls)

                        for i in Cows:
                            if i in Bulls:
                                for j in range(Bulls.count(i)): Bulls.remove(i)

                        tree.insert('',END,values=[tno[0],tentry.get(),len(Cows),len(Bulls)])
                        tno[0]=tno[0]+1
                        tentry.delete(0,END)
                                        
                        if len(Cows)==n:
                            stoptime = dt.datetime.time(dt.datetime.now())
                            timer.stop_timer()
                            dur=dt.datetime.combine(dt.date.today(), stoptime) - dt.datetime.combine(dt.date.today(), starttime) #, Time='+str(dur)+'
                            total_seconds = int(dur.total_seconds())
                            hours = total_seconds // 3600
                            minutes = (total_seconds % 3600) // 60
                            seconds = total_seconds % 60

                            # Format the time difference as a string in 'HH:MM:SS' format
                            tds= f'{hours:02}:{minutes:02}:{seconds:02}'
                            
                            tno[1]=False
                            db=c.connect(host='127.0.0.1',user='root',password='root',database='candb')
                            cur=db.cursor()
                            cur.execute('update data set Played=Played+1, Won=Won+1 where  NOD='+str(n)+';')
                            
                            cur.execute('select record from data where NOD='+str(n)+';')
                            x=cur.fetchone(); x_=x[0]
                            if x[0]==None or x[0]>=tno[0]: cur.execute('update data set record='+str(tno[0]-1)+' where NOD='+str(n)+';')
                            #print(tds)

                            cur.execute('select Time from data where NOD='+str(n)+';')
                            x=cur.fetchone()

                            if x[0]!=None: 

                                total_seconds = int(x[0].total_seconds())
                                hours = total_seconds // 3600
                                minutes = (total_seconds % 3600) // 60
                                seconds = total_seconds % 60

                                # Format the time difference as a string in 'HH:MM:SS' format
                                tds1= f'{hours:02}:{minutes:02}:{seconds:02}'

                            else: tds1='-'
                            
                            if x[0]==None or x[0]>dur: cur.execute('update data set Time="'+tds+'" where NOD='+str(n)+';')
                            messagebox.showinfo('','The Code is '+code+'.\nYou Win!!\n\nTime : '+tds+'\n\nBest Time : '+tds1+'\nRecord : '+str(x_))
                            db.commit()
                            db.close()
                                            
                        if tno[0]==mn+1:
                                messagebox.showinfo('','No trials left.You Lose.\nThe Code : '+code)
                                print(code)
                                db=c.connect(host='127.0.0.1',user='root',password='root',database='candb')
                                cur=db.cursor()
                                cur.execute('update data set Played=Played+1, Lost=Lost+1 where NOD='+str(n)+';')
                                db.commit()
                                db.close()
                
                ok=Button(root,text='OK',font=("Cambria",14),width=15,fg='lavender',bg='navy',command=OK); ok.place(x=532,y=370)
                tentry.bind("<Return>",lambda event : OK())
                
                back=Button(root,text="BACK",font=("Cambria",14),bg="navy",width=8,fg='lavender',command=START__); back.place(x=10,y=10)
            new_func(n)

        cnlbl=Label(root,text='Select Code Length :',bg='lavender',fg="navy",font=("Cambria",16),width=25); cnlbl.place(x=255,y=200)

        def Stfunc():
            root.destroy(); stfunc()

        excmd=Button(root,text='EXIT',font=("Cambria",14),width=8,fg='lavender',bg='navy',command=root.destroy); excmd.place(x=680,y=10)
        stcmd=Button(root,text='STATISTICS',font=('Cambria',14),width=13,fg='lavender',bg='navy',command=Stfunc); stcmd.place(x=530,y=10)

        tlbl=Label(root,text='Cows & Bulls',font=('Viner Hand ITC',35),bg='lavender',fg='navy'); tlbl.place(x=270,y=90)


        m=StringVar()
        cncombo=ttk.Combobox(root,width=16,textvariable=m,font=('Californian FB',15),state='readonly')
        cncombo['values']=('3','4','5','6','7','8','9','10')
        cncombo.place(x=315,y=250)

        cncmd=Button(root,text='PLAY',font=("Cambria",16),width=13,fg='lavender',bg='navy',command=Start); cncmd.place(x=325,y=320)

    START()
    root.mainloop()
