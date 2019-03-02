from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404

from project.models import project_details
from student.models import Std_details
from users.models import CustomUser
from django.template import RequestContext



from .forms import research_fellow_form, student_details_form, project_form, \
    time_frame_form, Edit_project_details, Edit_time_frame


def display_form1(request):
    res_form = research_fellow_form
    stu_form = student_details_form
    pro_form = project_form
    tim_form = time_frame_form

    if request.POST:
        # res_form = research_fellow_form(request.POST)
        # stu_form = student_details_form(request.POST)
        pro_form = project_form(request.POST)
        tim_form = time_frame_form(request.POST)
       # sho_form = show_date(request.POST)

        if  pro_form.is_valid() \
                and tim_form.is_valid():
            #form3 = res_form.save(commit=False)
            #form4 = stu_form.save(commit=False)
            form5 = pro_form.save(commit=False)
            form6 = tim_form.save()
            #form7 = sho_form.save(commit=False)

            form5.Time_frame_id = form6
            student = Std_details.objects.filter(
                student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
            student = student[0]
            form5.stud_id = student

            student.st_project_status += 1

            form5.save()
            student.save()

            return redirect('student:student_dashboard')
            # res_form = research_fellow_form
            # stu_form = student_details_form
            # pro_form = project_form
            # tim_form = time_frame_form

        # form7 = sho_form.save(commit=False)
        # form7.save()

    context = {
               'form3': res_form,
               'form4': stu_form,
               'form5': pro_form,
               'form6': tim_form,
               }

    return render(request, "project/submission_form1.html", context)

def edit_form1(request):
    # project = project_details.objects.get(stud_id=Std_details.objects.get(student_id =CustomUser.objects.get(username = request.user.username)))
    # time_frame = project.Time_frame_id
    # pro_form = Edit_project_details(
    #     initial={
    #         'enroll_period' : project.enroll_period,
    #         'period_of_data' : project.period_of_data,
    #         'budget_estimate' : project.budget_estimate,
    #         'choose_fund' : project.choose_fund,
    #         'sample_size' : project.sample_size,
    #     }
    # )
    # time_form = Edit_time_frame(
    #     initial={
    #         'study_coll_period' : time_frame.study_coll_period,
    #         'retro_period' : time_frame.retro_period,
    #         'patient_part' : time_frame.patient_part,
    #         'data_analysis' : time_frame.data_analysis,
    #         'Thesis_submis' : time_frame.Thesis_submis,
    #     }
    # )
    #
    # project = project_details.objects.get(stud_id=Std_details.objects.get(student_id =CustomUser.objects.get(username = request.user.username)))
    #
    # if request.POST:
    #     pro_form = project_form(request.POST)
    #     tim_form = time_frame_form(request.POST)
    #     if pro_form.is_valid() and tim_form.is_valid():
    #         project = project_details.objects.get(
    #             stud_id=Std_details.objects.get(student_id=CustomUser.objects.get(username=request.user.username)))
    #         project.enroll_period = pro_form.cleaned_data['enroll_period']
    #         project.period_of_data = pro_form.cleaned_data['enroll_period']
    #         project.budget_estimate = pro_form.cleaned_data['budget_estimate']
    #         project.choose_fund = pro_form.cleaned_data['choose_fund']
    #         project.sample_size = pro_form.cleaned_data['sample_size']
    #
    #
    #         time_frame = project.Time_frame_id
    #
    #         time_frame.study_coll_period = time_form.cleaned_data['study_coll_period']
    #         time_frame.retro_period = time_form.cleaned_data['retro_period']
    #         time_framepatient_part = time_form.cleaned_data['patient_part']
    #         time_frame.data_analysis = time_form.cleaned_data['data_analysis']
    #         time_frame.Thesis_submit = time_form.cleaned_data['Thesis_submis']
    #
    #
    #
    #         project.save()
    #         time_frame.save()
    #         return redirect('student:student_dashboard')
    # context = {
    #     'form5': pro_form,
    #     'form6': time_form,
    # }
    #
    # return render(request, "project/edit_form1.html", context)

    project = project_details.objects.get(
        stud_id=Std_details.objects.get(student_id=CustomUser.objects.get(username=request.user.username)))
    time_frame = project.Time_frame_id
    pro_form = Edit_project_details(instance=project,)
    pro_form.fields['PI_id'].disabled = True
    time_form = Edit_time_frame(instance=time_frame)

    if request.POST:
        pro_form = project_form(request.POST,instance=project)
        tim_form = time_frame_form(request.POST,instance=time_frame)
        if pro_form.is_valid() and tim_form.is_valid():

            pro_form.save()
            tim_form.save()
            return redirect('student:student_dashboard')
    context = {
        'form5': pro_form,
        'form6': time_form,
    }

    return render(request, "project/edit_form1.html", context)

# todo later
# def display_form2(request):
#     std_form = study_design_form
#     ste_form = step_study_form
#     st2_form = step_study_form2
#     st3_form = step_study_form3
#
#
#
#     if request.POST:
#         std_form = study_design(request.POST)
#         ste_form = step_study_form(request.POST)
#         st2_form = step_study_form2(request.POST)
#         st3_form = step_study_form3(request.POST)
#
#         if std_form.is_valid() and ste_form.isvalid() and st2_form.is_valid() and st3_form.is_valid():
#             form1 = study_design.save(commit=False)
#             form2 = step_study_form.save(commit=False)
#             form3 = step_study_form2.save(commit=False)
#             form4 = step_study_form3.save(commit=False)
#
#
#             form1.save()
#             form2.save()
#             form3.save()
#             form4.save()
#
#
#         # form7 = sho_form.save(commit=False)
#         # form7.save()
#
#     context = {'form1': std_form,
#                'form2': ste_form,
#                'form3':st2_form,
#                'form4':st3_form,
#                }
#     return render(request, "form/submission_form2.html", context)

# def display_comp_report(request):
#     com_form = completion_report_form
#     co2_form = completion_report_form2
#     co3_form = completion_report_form3
#     co4_form = completion_report_form4
#     co5_form = completion_report_form5
#     co6_form = completion_report_form6
#
#     if request.POST:
#         com_form = completion_report_form(request.POST)
#         co2_form = completion_report_form2(request.POST)
#         co3_form = completion_report_form3(request.POST)
#         co4_form = completion_report_form4(request.POST)
#         co5_form = completion_report_form5(request.POST)
#         co6_form = completion_report_form6(request.POST)
#
#         if com_form.is_valid() and co2_form.is_valid() and co3_form.is_valid() and co4_form.is_valid() and co5_form.is_valid() and co6_form.is_valid():
#             form1 = completion_report_form.save(commit=False)
#             form2 = completion_report_form2.save(commit=False)
#             form3 = completion_report_form3.save(commit=False)
#             form4 = completion_report_form4.save(commit=False)
#             form5 = completion_report_form5.save(commit=False)
#             form6 = completion_report_form6.save(commit=False)
#
#
#             form1.save()
#             form2.save()
#             form3.save()
#             form4.save()
#             form5.save()
#             form6.save()
#
#
#
#         # form7 = sho_form.save(commit=False)
#         # form7.save()
#
#     context = {'form1': com_form,
#                'form2':co2_form,
#                'form3':co3_form,
#                'form4':co4_form,
#                'form5':co5_form,
#                'form6':co6_form,
#                }
#     return render(request, "form/completion_form.html", context)
#
# def display_prog_report(request):
#     pro_form = progress_report_form
#     pr2_form = progress_report_form2
#     pr3_form = progress_report_form3
#     pr4_form = progress_report_form4
#     pr5_form = progress_report_form5
#
#
#     if request.POST:
#         pro_form = progress_report_form(request.POST)
#         pr2_form = progress_report_form2(request.POST)
#         pr3_form = progress_report_form3(request.POST)
#         pr4_form = progress_report_form4(request.POST)
#         pr5_form = progress_report_form5(request.POST)
#
#
#         if pro_form.is_valid() and pr2_form.is_valid() and pr3_form.is_valid() and pr4_form.is_valid() and pr5_form.is_valid():
#             form1 = progress_report_form.save(commit=False)
#             form2 = progress_report_form2.save(commit=False)
#             form3 = progress_report_form3.save(commit=False)
#             form4 = progress_report_form4.save(commit=False)
#             form5 = progress_report_form5.save(commit=False)
#
#
#
#             form1.save()
#             form2.save()
#             form3.save()
#             form4.save()
#             form5.save()
#
#
#
#
#         # form7 = sho_form.save(commit=False)
#         # form7.save()
#
#     context = {'form1': pro_form,
#                'form2':pr2_form,
#                'form3':pr3_form,
#                'form4':pr4_form,
#                'form5':pr5_form,
#
#                }
#     return render(request, "form/progress_form.html", context)
#
#
#
# # testing purpose
#
# # def display_index(request):
# #     pinv = Principal_investigator.objects.all()
# #     context = {
# #         'pinv' : pinv,
# #
# #     }
# #     return render(request,'form/whh.html',context)
# #s
# #
#
