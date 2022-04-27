from tkinter import *
import speedtest
from PIL import ImageTk


test = speedtest.Speedtest()
ping_result = test.results.ping

root = Tk()
root.title('Chibong Internet Speedtest')
root.geometry('550x500')
root.resizable(False, False)

canvas = Canvas(width = 200, height = 200, bg = 'White')
canvas.pack(expand = YES, fill = BOTH)

bg = ImageTk.PhotoImage(file='bg.png')
canvas.create_image(10, 10, image=bg, anchor=NW)

def start_btn():
    root.title('Loading Server List...(I am Chibong btw)')
    Download_speed_label.config(text='I am Chibong btw')
    test.get_servers()
    root.title("Choosing Best Server...(feel PROUD to use CHIBONG's speed test app")
    Download_speed_label.config(text="Choosing Best server...(feel PROUD to use CHIBONG's speed test app")
    best = test.get_best_server()
    root.title('Performing Download Test...(TIP : USE your BRAIN)')
    Download_speed_label.config(text='Performing Download Test...(TIP :(USE your BRAIN)')
    download_result = test.download()
    Download_speed_label.config(text='Performing Upload Test...(Fun fact: Speedtests were invented by ME, no cap)')
    root.title('Performing Upload Test...(Fun fact: Speedtests were invented by ME, no cap)')
    upload_result = test.upload()
    ping_result = test.results.ping

    Download_speed_label.config(text=f'Download speed: {download_result / 1024 / 1024:.2f} Mbps')
    Upload_speed_label.config(text=f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbps")
    ping_label.config(text=f'Ping: {ping_result:.2f} ms')
    root.title('Chibong Internet Speedtest')

Download_speed_label = Label(root, bg='White', fg='black', width=50, font=('Arial', 15))
Download_speed_label.pack(side = "top")
Upload_speed_label = Label(root, bg='White', fg='black', width = 50, font=('Arial', 15))
Upload_speed_label.pack(side = "top")


if ping_result > 10:
    ping_label = Label(root, bg='White',fg = "green",  width = 50, font=('Arial', 15))
elif ping_result < 10:
    ping_label = Label(root, bg='White',fg = "red",  width = 50, font=('Arial', 15))
    ping_label.pack(side = "top")

start_btn = Button(root,text = "start speedtest", bg = "green",font =("Arial",15),width=30, command = start_btn)
start_btn.pack (side='top')

root.mainloop()
