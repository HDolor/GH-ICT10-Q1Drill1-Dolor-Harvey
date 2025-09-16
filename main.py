from pyscript import display, document
"""
def data(d): #Func
    document.getElementById('out').innerHTML = " "
    username=document.getElementById('username').value
    password=document.getElementById('pass').value
    #Inputs
    display(f'Your Username Is {username} and your password is {password}. Do you confirm?', target="out")

def add(a):
    document.getElementById('out').innerHTML= " "
    a=float(document.getElementById('num1').value)
    b=float(document.getElementById('num2').value)

    c={a+b}
    display(f'Sum is: {c}', target='out')\
"""
def trape(a):
    document.getElementById('out').innerHTML=" "
    a=float(document.getElementById('a').value)
    b=float(document.getElementById('b').value)#Bottom
    h=float(document.getElementById('h').value)#Height
    un=document.getElementById('un').value#Unit
    A=(((a+b)/2)*h)#Formula
    display(f'The Area is: {A} {un}',  target='out')