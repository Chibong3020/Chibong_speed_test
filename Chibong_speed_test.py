import tkinter as tk
import speedtest

test = speedtest.Speedtest()
ping_result = test.results.ping

screen = tk.Tk()
screen.title('Chibong Internet Speedtest')
screen.geometry('500x500')
screen.config(bg='yellow')

def start_btn():
    screen.title('Loading Server List...(I am Chibong btw)')
    Download_speed_label.config(text='I am Chibong btw')
    test.get_servers()
    screen.title("Choosing Best Server...(feel PROUD to use CHIBONG's speed test app")
    Download_speed_label.config(text="Choosing Best server...(feel PROUD to use CHIBONG's speed test app")
    best = test.get_best_server()
    screen.title('Performing Download Test...(TIP : USE your BRAIN)')
    Download_speed_label.config(text='Performing Download Test...(TIP :(USE your BRAIN)')
    download_result = test.download()
    Download_speed_label.config(text='Performing Upload Test...(Fun fact: Speedtests were invented by ME, no cap)')
    screen.title('Performing Upload Test...(Fun fact: Speedtests were invented by ME, no cap)')
    upload_result = test.upload()
    ping_result = test.results.ping

    Download_speed_label.config(text=f'Download speed: {download_result / 1024 / 1024:.2f} Mbps')
    Upload_speed_label.config(text=f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbps")
    ping_label.config(text=f'Ping: {ping_result:.2f} ms')
    screen.title('Chibong Internet Speedtest')

Download_speed_label = tk.Label(screen, bg='yellow', fg='black', width=50, font=('Arial', 15))
Download_speed_label.pack(side = "top")
Upload_speed_label = tk.Label(screen, bg='yellow', fg='black', width = 50, font=('Arial', 15))
Upload_speed_label.pack(side = "top")


if ping_result > 10:
    ping_label = tk.Label(screen, bg='yellow',fg = "green",  width = 50, font=('Arial', 15))
elif ping_result < 10:
    ping_label = tk.Label(screen, bg='yellow',fg = "red",  width = 50, font=('Arial', 15))
    ping_label.pack(side = "top")

start_btn = tk.Button(screen,text = "start speedtest", bg = "green",font =("Arial",15),width=30, command = start_btn)
start_btn.pack (side='top')

screen.mainloop()