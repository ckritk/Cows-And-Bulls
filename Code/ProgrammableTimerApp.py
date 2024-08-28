from tkinter import Label
from datetime import timedelta

class ProgrammableTimerApp:
    def __init__(self, master, x_, y_):
        self.master = master
        self.running = False
        self.elapsed_time = timedelta(seconds=0)
        self.time_format = "{:02d}:{:02d}:{:02d}"

        self.display = Label(master, text="00:00:00", font=("Arial", 15), bg='lavender', fg='navy')
        self.display.place(x=x_, y=y_)

    def update_timer(self):
        if self.running:
            self.elapsed_time += timedelta(seconds=1)
            hours, remainder = divmod(self.elapsed_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            self.display.config(text=self.time_format.format(int(hours), int(minutes), int(seconds)))
            self.master.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def remove_timer_display(self):
        self.display.place_forget()
