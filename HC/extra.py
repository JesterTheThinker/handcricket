def click1():
    user_choice_value == 0

def click2():
    user_choice_value == 1
    
def click3():
    user_choice_value == 2

def click4():
    user_choice_value == 3
    
def click5():
    user_choice_value == 4
    
def click6():
    user_choice_value == 5
    
    
     
button1 = ttk.Button(root, command=click1())
button1.pack(pady=20)

button2 = ttk.Button(root, command=click2())
button2.pack(pady=10)

button3 = ttk.Button(root, command=click3())
button3.pack(pady=10)

button4 = ttk.Button(root, command=click4())
button4.pack(pady=10)

button5 = ttk.Button(root, command=click5())
button5.pack(pady=10)

button6 = ttk.Button(root, command=click6())
button6.pack(pady=10)