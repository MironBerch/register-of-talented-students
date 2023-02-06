from django.shortcuts import render, redirect
from reporting.forms import ContestForm
from django.contrib.auth.mixins import LoginRequiredMixin
from reporting.export import export_contest_to_excel
import os
from reporting.services import get_all_contests, get_users_creation_contests, get_contest
from django.http import FileResponse
from core.views import View


class ContestCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ContestForm()

        context = {
            'form': form,
        }

        return render(request, 'reporting/create_report.html', context)
    
    def post(self, request):
        form = ContestForm(request.POST or None, files=request.FILES or None)

        if form.is_valid():
            contest = form.save()
            contest.contest_creater = request.user
            contest.save()
            return redirect('list')

        return redirect('create')


class ContestListView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            contests = get_all_contests()
        else:
            contests = get_users_creation_contests(request=request)

        context = {
            'contests': contests,
        }
        
        return render(request, 'reporting/report_list.html', context)


class ContestUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        contest = get_contest(id=id)

        if not (request.user.is_superuser==True or request.user==contest.contest_creater):
            return redirect('list')

        form = ContestForm(request.POST or None, instance=contest, files=request.FILES or None)

        context = {
            'form': form,
            'contest': contest,
        }

        return render(request, 'reporting/update_report.html', context)

    def post(self, request, id):
        contest = get_contest(id=id)
        form = ContestForm(request.POST or None, instance=contest, files=request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('list')
        
        return redirect('list')


class ContestDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        contest = get_contest(id=id)

        if not (request.user.is_superuser==True or request.user==contest.contest_creater):
            return redirect('list')
        
        context = {
            'contest': contest,
        }

        return render(request, 'reporting/delete_report.html', context)

    def post(self, request, id):
        contest = get_contest(id=id)
        contest.delete()
        return redirect('list')


class ContestDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        contest = get_contest(id=id)

        context = {
            'contest': contest,
        }

        return render(request, 'reporting/detail_report.html', context)


class ContestExportView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'reporting/export_report.html')
    
    def post(self, request):
        if request.user.is_superuser:
            contests = get_all_contests()
        else:
            contests = get_users_creation_contests(request=request)

        export_contest_to_excel(contests)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = 'export.xlsx'
        filepath = BASE_DIR + '/media/' + filename
        file = open(filepath, 'rb')
        response = FileResponse(file)
        return response