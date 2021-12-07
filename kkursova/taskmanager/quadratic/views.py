from django.shortcuts import render
from .models import Quadratics
from .forms import QuadraticsForm



def getRoots(a, b, c):
    from cmath import sqrt
    a, b, c = float(a), float(b), float(c)
    d = pow(b, 2) - (4 * a * c)
    return (-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)


def quadratic(request):
    error = ''
    form = QuadraticsForm()
    context={'form': form}
    if request.method == 'POST':
        form = QuadraticsForm(request.POST)
        coefs = form.data['a'], form.data['b'], form.data['c']
        roots = getRoots(*coefs)
        context = {
        'form': form,
        'error': error,
        'root1': roots[0],
        'root2': roots[1],
        }
        if form.is_valid():
            form.save()
    
    return render(request, 'quadratic/quadratic.html', context)

