import queue
import threading
import time
import PySimpleGUI as sg

def long_operation_thread(seconds, gui_queue):
    print('Starting thread - will sleep for {} seconds'.format(seconds))
    time.sleep(seconds)                  # sleep for a while
    gui_queue.put('** Done **')  # put a message into queue for GUI


def the_gui():
    """
    Starts and executes the GUI
    Reads data from a Queue and displays the data to the window
    Returns when the user exits / closes the window
    """

    gui_queue = queue.Queue()  # queue used to communicate between the gui and the threads

    layout = [[sg.Text('Long task to perform example')],
              [sg.Output(size=(70, 12))],
              [sg.Text('Number of seconds your task will take'),
                  sg.Input(key='-SECONDS-', size=(5, 1)),
                  sg.Button('Do Long Task', bind_return_key=True)],
              [sg.Button('Click Me'), sg.Button('Join'), sg.Button('Exit')], ]

    window = sg.Window('Multithreaded Window', layout)

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read(timeout=100)
        if event in (None, 'Exit'):
            break
        elif event.startswith('Do'):
            try:
                seconds = int(values['-SECONDS-'])
                print(
                    'Thread ALIVE! Long work....sending value of {} seconds'.format(seconds))
                t = threading.Thread(target=long_operation_thread,
                                 args=(seconds, gui_queue,), daemon=True)
                t.start()
            except Exception:
                print('Error starting work thread. Bad seconds input: "%s"' %
                      values['-SECONDS-'])
        elif event == 'Click Me':
            print('Your GUI is alive and well')
        # --------------- Check for incoming messages from threads  ---------------
        elif event == 'Join':
            t.join()
        try:
            message = gui_queue.get_nowait()
        except queue.Empty:             # get_nowait() will get exception when Queue is empty
            message = None              # break from the loop if no more messages are queued up

        # if message received from queue, display the message in the Window
        if message:
            print('Got a message back from the thread: ', message)

    # if user exits the window, then close the window and exit the GUI func
    window.close()


if __name__ == '__main__':
    the_gui()
    print('Exiting Program')
