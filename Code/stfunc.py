from tkinter import *
import mysql.connector as c

def stfunc():
    from CowsAndBulls.Main_Game_Func import Main_Game_Func
    
    window = Tk()
    window['bg'] = 'lavender'
    window.geometry('780x540')

    db = c.connect(host='127.0.0.1', user='root', password='root', database='candb')
    cur = db.cursor()
    cur.execute('select nod, played, won, lost, record, time from data')
    recs = cur.fetchall()
    db.close()

    a = 'CL\n\n3\n\n4\n\n5\n\n6\n\n7\n\n8\n\n9\n\n10'
    b = 'Played'
    C = 'Won'
    d = 'Lost'
    e = 'Record'
    g = 'Best Time'
    f = '|\n' * 30

    for rec in recs:
        b += '\n\n' + str(rec[1])
        C += '\n\n' + str(rec[2])
        d += '\n\n' + str(rec[3])
        e += '\n\n' + str(rec[4])
        g += '\n\n' + str(rec[5])

    lblt = Label(window, text=a, font=("Cambria", 16), bg='lavender', fg='navy')
    lblt.place(x=55, y=70)
    lblp = Label(window, text=b, font=("Cambria", 16), bg='lavender', fg='navy')
    lblp.place(x=150, y=70)
    lblw = Label(window, text=C, font=("Cambria", 16), bg='lavender', fg='navy')
    lblw.place(x=280, y=70)
    lbll = Label(window, text=d, font=("Cambria", 16), bg='lavender', fg='navy')
    lbll.place(x=390, y=70)
    lblr = Label(window, text=e, font=("Cambria", 16), bg='lavender', fg='navy')
    lblr.place(x=498, y=70)
    lblr = Label(window, text=g, font=("Cambria", 16), bg='lavender', fg='navy')
    lblr.place(x=630, y=70)

    lbll1 = Label(window, text=f, font=("Cambria", 10), bg='lavender', fg='slate blue')
    lbll1.place(x=116, y=60)
    lbll2 = Label(window, text=f, font=("Cambria", 10), bg='lavender', fg='slate blue')
    lbll2.place(x=243, y=60)
    lbll3 = Label(window, text=f, font=("Cambria", 10), bg='lavender', fg='slate blue')
    lbll3.place(x=353, y=60)
    lbll4 = Label(window, text=f, font=("Cambria", 10), bg='lavender', fg='slate blue')
    lbll4.place(x=461, y=60)
    lbll4 = Label(window, text=f, font=("Cambria", 10), bg='lavender', fg='slate blue')
    lbll4.place(x=593, y=60)

    def bk():
        window.destroy()
        Main_Game_Func()

    bkcmd = Button(window, text='BACK', font=("Cambria", 14), width=8, fg='lavender', bg='navy', command=bk)
    bkcmd.place(x=10, y=10)
