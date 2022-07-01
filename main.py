import time
import threading
import logging
import tkinter as tk
import tkinter.scrolledtext as ScrolledText
import api_weather_request
from api_weather_request import WeatherStatus
class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

class myGUI(tk.Frame):

    # This class defines the graphical user interface

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.build_gui()

    def build_gui(self):
        # Build GUI
        self.root.title('Songlyz API-weather System Interface')
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')

        # Add text widget to display logging info
        st = ScrolledText.ScrolledText(self, state='disabled')
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='w', columnspan=4)

        # Create textLogger
        text_handler = TextHandler(st)

        # Logging configuration
        logging.basicConfig(filename='test.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s')

        # Add the handler to logger
        logger = logging.getLogger()
        logger.addHandler(text_handler)

def api_to_log_display():
    msg1 = "Area :", x.city, 'DateTime String:', x.get_time()
    logging.info(msg1)

    msg2 = f"Current Weather : {x.current_data_weather['weather'][0]['description']}"
    logging.info(msg2)

    msg3 = f'T : {x.current_data_weather["main"]["temp"]} celcius,' \
           f' P : {x.current_data_weather["main"]["pressure"]} hPa,' \
           f' H : {x.current_data_weather["main"]["humidity"]} %'
    logging.info(msg3)

    msg4 = f'Wind Speed : {x.current_data_weather["wind"]["speed"]},' \
           f' Wind Degree : {x.current_data_weather["wind"]["deg"]}'
    logging.info(msg4)

    msg5 = "---------------------------------------------------"
    logging.info(msg5)

def worker1():
    while True:
        x.change_city("Bangkok")
        x.request_data()
        api_to_log_display()
        time.sleep(5)


def main():

    root = tk.Tk()
    myGUI(root)

    t1 = threading.Thread(target=worker1, args=[])
    t1.start()

    root.mainloop()
    t1.join()


x = WeatherStatus("Bangkok") #intial
main()