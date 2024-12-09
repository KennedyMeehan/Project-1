from tkinter import Tk
from gui import GUI

def main():
    '''
    This function creates the gui window and ensures it is not resizeable
    '''
    window = Tk()
    window.title('Voting System')
    window.geometry('300x200')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
