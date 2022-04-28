from tkinter import messagebox
import nltk
from tkinter import *
from tkinter import filedialog



def result_picture():
    message = calculated_text.get(1.0, END).replace('\n', '')
    if message != '':
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        doc = nltk.word_tokenize(message)
        doc = nltk.pos_tag(doc)
        new_doc = []
        for item in doc:
            if item[1] != ',' and item[1] != '.':
                new_doc.append(item)
        #grammar taken here http://www.nltk.org/book_1ed/ch07.html and https://stackoverflow.com/questions/55766558/recursion-in-nltks-regexpparser
        grammar = r"""
         P: {<IN>}
         VP: {<V.*|MD>}
         NP: {<DT|PR.*|JJ|NN.*>+}
         PP: {<IN><NP>}
         VP: {<VB.*><NP|RB|PP|CLAUSE>+$}
         CLAUSE: {<NP><VP>}
         """
        cp = nltk.RegexpParser(grammar).parse(new_doc).draw()


def how_it_work():
    messagebox.askquestion("How it work?", "1. Input something(text) or open .txt file by clicking on button 'Open'.\n"
                                   "2. Click on button 'Send'.\n"
                                   "3. Waiting... Look at the picture.", type='ok')

def open_file():

    file_path = filedialog.askopenfilename()
    if file_path != "":
        f = open(file_path, 'r')
        calculated_text.delete(1.0, "end")
        calculated_text.insert(1.0, f.read())
        f.close()



root = Tk()
root.title("Lab №2")
root.resizable(width=False, height=False)
root.geometry("400x220+550+300")
label = Label(root, text='Input something↴').grid(row=2, column=1)
label1 = Label(root, text='          ').grid(row=2, column=0)
calculated_text = Text(root, height=5, width=40)
calculated_text.grid(row=3, column=1, sticky='nsew', columnspan=3)
label2 = Label(root, text=' ').grid(row=4, column=0)
b1 = Button(text="Create", width=10, command=result_picture).grid(row=5, column=2)
label3 = Label(root, text=' ').grid(row=6, column=0)
b2 = Button(text="How it work?", width=10, command=how_it_work).grid(row=1, column=3)
label4 = Label(root, text=' ').grid(row=0, column=3)
b3 = Button(text="Open", width=10, command=open_file).grid(row=1, column=1)
root.mainloop()
