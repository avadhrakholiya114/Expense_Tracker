from django.shortcuts import render, redirect
from .forms import Expense
from .models import exp
from django.db.models import Sum
import datetime


# Create your views here.

def index(request):
    exps = exp.objects.all()
    sum = exp.objects.aggregate(Sum("price"))
    print(sum)

    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = exp.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum("price"))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = exp.objects.filter(date__gt=last_month)
    month_sum = data.aggregate(Sum("price"))

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = exp.objects.filter(date__gt=last_week)
    week_sum = data.aggregate(Sum("price"))

    daybyday = exp.objects.filter().values('date').order_by().annotate(Sum("price"))
    print(daybyday)

    return render(request, 'index.html',
                  {'exps': exps, 'sum': sum, 'yearly_sum': yearly_sum, 'month_sum': month_sum, 'week_sum': week_sum})


# avadh7
def home(request):
    if request.method == 'POST':
        form = Expense(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    exp_form = Expense()
    return render(request, 'home.html', {'exp_form': exp_form})


def update(request, id):
    exps = exp.objects.get(id=id)
    exp_form = Expense(instance=exps)
    # print(exp_form)
    if request.method == 'POST':
        exps = exp.objects.get(id=id)
        # print(exps)
        exp_form = Expense(request.POST, instance=exps)
        # print(exp_form)
        if exp_form.is_valid():
            exp_form.save()
            return redirect('/')

    return render(request, 'edit.html', {'exp_form': exp_form})


def delete(request, id):
    exps = exp.objects.get(id=id)
    exps.delete()
    return redirect('/')
