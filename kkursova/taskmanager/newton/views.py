from django.shortcuts import render
from sympy import *
from scipy.misc import derivative
from .forms import NewtonsForm


def make_f(f):
    x = symbols('x')
    return lambda a: eval(f).subs(x, a)


def newtonMethod(f, x0, eps):
    x0, eps = float(x0), float(eps)
    f = make_f(f)
    # print(f(1))
    while True:
        x1 = x0 - f(x0) / derivative(f, x0) 
        t = abs(x1 - x0)
        if t < eps:
            break
        x0 = x1
    return x0
    
    
def newton(request):
    error = ''
    form = NewtonsForm()
    context={'form': form}
    if request.method == 'POST':
        form = NewtonsForm(request.POST)
        data = form.data['f'], form.data['x0'], form.data['eps']
        # print(data)
        root = newtonMethod(*data)
        context = {
        'form': form,
        'error': error,
        'root': root,
        }
        if form.is_valid():
            form.save()

    return render(request, 'newton/newton.html', context)
