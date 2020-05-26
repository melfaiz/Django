from django.http import HttpResponse
from django import http
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from decimal import *

from .models import Point

from .forms import ChartForm

import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

def qs_to_arr(qs):
    """ QuerySet to DataFrame """

    array = []
    for item in qs:
        array.append(item.x)

    return array

def ChartView(request):

    if request.method == 'POST':

        form = ChartForm(request.POST)
      
        if form.is_valid():
            form.save()
            messages.success(request, 'Point successfully added')
            return http.HttpResponseRedirect('/')
    else:
        form = ChartForm()

    context ={
        'form' : form,
        'query' : Point.objects.all()
    }

    return render(request, "chart.html",context)

def delPoint(request):

    try:
        Point.objects.latest('id').delete()
        messages.success(request, 'Point successfully deleted')

    except Point.DoesNotExist:
        messages.warning(request, 'No point existing')    
    
    return redirect('home')


def predict(request):

    qs = Point.objects.all()
    y = qs_to_arr(qs)
    y = np.array(y)

    x = np.arange(0, len(y), 1).reshape((-1, 1))

    model = LinearRegression()

    kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
    gp.fit(x, y)

    model.fit(x, y)

    x_pred = x[-1]+1
    y_pred = model.predict(x_pred.reshape(-1, 1) )

    print("Prediction for",x_pred,"is",y_pred)

    Point.objects.create(x=y_pred.item())

    return redirect('home')