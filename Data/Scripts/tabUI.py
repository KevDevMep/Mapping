import tab as T
import pandas as pd
import tkinter as tk

def yearSet():
    try:
        if year.get() < 1976 or year.get() > 2024 or year.get() % 2 == 1:
            print('Year must be even and in bounds')
        else:
            T.df = pd.read_csv('1976-2024-house.tab', dtype={'runoff':str, 'special':str, 'writein':str, 'unofficial':str, 'fusion_ticket':str})
            T.df = T.setUp(T.df, year.get())
            set_.set(True)
            print('Set')
    except:
        print('Error')

def export():
    if set_.get():
        if tag.get().strip():
            T.toForm(tag.get().strip())
            T.toFormNY(tag.get().strip())
            T.df.to_csv(f'house_{year.get()}.csv')
            print('Export')
        else:
            print('Tag can not be Empty')
    else:
        print('Not Set')

root = tk.Tk()
root.title('Tab')
tag = tk.StringVar(value='Export')
f1 = tk.StringVar()
f2 = tk.StringVar()
year = tk.IntVar(value=2024)
set_ = tk.BooleanVar()

tk.Label(root, text='Year').grid(row=0, column=0)
tk.Spinbox(root, textvariable=year, from_=1976, to_=2024, increment=2).grid(row=1, column=0)
tk.Button(root, text='Set', command=yearSet).grid(row=1, column=1)
tk.Label(root, text='Tag').grid(row=2, column=0)
tk.Entry(root, textvariable=tag).grid(row=3, column=0)
tk.Button(root, text='Export', command=export).grid(row=4, column=0)
tk.Checkbutton(root, text='Set', variable=set_, onvalue=True, offvalue=False, state='disabled').grid(row=4, column=1)

root.mainloop()
