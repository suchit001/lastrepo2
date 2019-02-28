from django.shortcuts import render
from .forms import *
# Create your views here.


def sample_create_view(request):
    bud_form = BudgetForm()
    cap_form = CapitalForm()
    Sal = Salary
    in1 = Invest1
    in2 = Invest2
    consum = Consumable


    if request.POST:
        bud_form = BudgetForm(request.POST)
        cap_form = CapitalForm(request.POST)
        sal_form = Salary(request.POST)
        in1 = Invest1(request.POST)
        in2 = Invest2(request.POST)
        consum = Consumable(request.POST)



        if bud_form.is_valid() and cap_form.is_valid() and sal_form.is_valid() and in1.is_valid() and in2.is_valid() and consum.is_valid() :
            form1 = bud_form.save()
            form2 = cap_form.save(commit=False)
            form3 = sal_form.save(commit=False)
            form4 = in1.save(commit=False)
            form5 = in2.save(commit=False)
            form6 = consum.save(commit=False)


            form2.Budget_id  =  form3.Salary_id = form4.invest1_id = form5.invest2_id = form6.consum_id= form1
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            form6.save()
            bud_form = BudgetForm()
            cap_form = CapitalForm()


        else:
            print(bud_form.errors, len(bud_form.errors))
            print(cap_form.errors, len(cap_form.errors))
            print(sal_form.errors, len(sal_form.errors))
            print(in1.errors, len(in1.errors))
            print(in2.errors, len(in2.errors))
            print(cap_form.errors, len(cap_form.errors))



    context = {'form1' : bud_form,
               'form2': cap_form,
               'form3': Sal,
               'form4': in1,
               'form5': in2,
               'form6': consum
               }
    return render(request, "student_dashboard/student_budget.html", context)