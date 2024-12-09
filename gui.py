from tkinter import *
import csv

class GUI:
    '''
    This class creates labels, radio buttons, and text inputs, saves votes to a
    a text file, catches potential errors that might come up, allows the user
    to select a candidate, enter ID and submit their vote.
    '''
    def __init__(self, window):
        self.window = window
        self.john_votes = 0
        self.jane_votes = 0

        
        self.frame_id = Frame(self.window)
        self.label_id = Label(self.frame_id, text='ID:')
        self.input_id = Entry(self.frame_id)
        self.label_id.pack(side='left')
        self.input_id.pack(anchor='w', padx=10, pady=10)
        self.frame_id.pack()

        
        self.frame_candidates = Frame(self.window)
        self.radio_label = Label(self.frame_candidates, text='CANDIDATES:')
        self.radio_answer = IntVar()
        self.radio_answer.set(0)  
        self.radio_john = Radiobutton(self.frame_candidates, text="John", variable=self.radio_answer, value=1)
        self.radio_jane = Radiobutton(self.frame_candidates, text='Jane', variable=self.radio_answer, value=2)
        self.radio_label.pack(side='left')
        self.radio_john.pack(side='left')
        self.radio_jane.pack(side='left')
        self.frame_candidates.pack()

        
        self.button_submit = Button(self.window, text='Submit Vote', command=self.submit_vote)
        self.button_submit.pack(padx=20, pady=20)

        
        self.frame_message = Frame(self.window)
        self.label_message = Label(self.frame_message, text='Please fill out all fields.')
        self.label_message.pack()
        self.frame_message.pack()

    def submit_vote(self):
        '''
        This function catches all types of user inputs for the voting
        such as duplicate votes, user validation, correct user number,
        and that a candidate is selected
        
        Makes sure ID is valid and stores vote accordingly in votes file
       
        '''
        voter_id = self.input_id.get().strip()
        selected_candidate = self.radio_answer.get()

        
        if voter_id == '':
            self.label_message.config(text='Enter an ID.', fg='red')
            return
        elif not voter_id.isdigit():
            self.label_message.config(text='ID must be a valid number.', fg='red')
            return
        try:
            with open('votes.csv', 'r') as file:
                votes = file.readlines()
                for vote in votes:
                    if f'Voter ID: {voter_id},' in vote:
                        self.label_message.config(text='User already voted.', fg='red')
                        return
        except FileNotFoundError:
            pass
            

        if selected_candidate == 0:
            self.label_message.config(text='Select a candidate.')
            return
        
        if selected_candidate == 1:
            candidate = 'John'
            self.john_votes += 1
        elif selected_candidate == 2:
            candidate = 'Jane'
            self.jane_votes += 1

        
       
        
        self.store_vote(voter_id, candidate)

        
        self.input_id.delete(0, END)
        self.radio_answer.set(0)

        self.label_message.config(text=f'Vote for {candidate} recorded!', fg='green')

    def store_vote(self, voter_id: int, candidate: str):
        '''
        Stores the candidate and voter_id in the votes.csv file
        
        
        :param voter_id: identifier thats unique for each voter
        :param candidate: the candidates name that is voted for
        
        
        '''

        with open('votes.csv', 'a') as file:                 
            file.write(f'Voter ID: {voter_id}, Candidate: {candidate}\n')


