from reporting.models import Contest
from django.shortcuts import render, redirect
from django.views import View
from reporting.forms import ContestForm
from django.contrib.auth.mixins import LoginRequiredMixin
from reporting.export import export_contest_to_excel
import mimetypes
# import os module
import os
from django.http.response import HttpResponse


class ContestCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ContestForm()

        context = {
            'form': form,
        }

        return render(request, 'reporting/create_report.html', context)
    
    def post(self, request):
        form = ContestForm(request.POST or None)

        if form.is_valid():
            contest = form.save()
            contest.contest_creater = request.user
            contest.save()
            return redirect('list')

        return redirect('create')


class ContestListView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            contests = Contest.objects.all().order_by('-id')
        else:
            contests = Contest.objects.filter(contest_creater=request.user).order_by('-id')

        context = {
            'contests': contests,
        }
        
        return render(request, 'reporting/report_list.html', context)


class ContestUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        contest = Contest.objects.get(id=id)

        if not (request.user==request.user.is_superuser or request.user==contest.contest_creater):
            return redirect('list')
        form = ContestForm(request.POST or None, instance=contest)

        context = {
            'form': form,
        }

        return render(request, 'reporting/update_report.html', context)

    def post(self, request, id):
        contest = Contest.objects.get(id=id) 
        form = ContestForm(request.POST or None, instance=contest)

        if form.is_valid():
            form.save()
            return redirect('list')
        
        return redirect('list')


class ContestDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        contest = Contest.objects.get(id=id)

        if not (request.user==request.user.is_superuser or request.user==contest.contest_creater):
            return redirect('list')
        
        context = {
            'contest': contest,
        }

        return render(request, 'reporting/delete_report.html', context)

    def post(self, request, id):
        contest = Contest.objects.get(id=id)
        contest.delete()
        return redirect('list')


class ContestDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        contest = Contest.objects.get(id=id)

        context = {
            'contest': contest,
        }

        return render(request, 'reporting/detail_report.html', context)


class ContestExportView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'reporting/export_report.html')
    
    def post(self, request):
        if request.user.is_superuser:
            contests = Contest.objects.all().order_by('-id')
        else:
            contests = Contest.objects.filter(contest_creater=request.user).order_by('-id')

        export_contest_to_excel(contests)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = 'учёт.xlsx'
        filepath = BASE_DIR + '/media/' + filename
        mime_type, _ = mimetypes.guess_type(filepath)

        with open(filepath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=mime_type)
            response['Content-Disposition'] = 'inline; filename=export.xlsx' # + os.path.basename(filepath)
            return response