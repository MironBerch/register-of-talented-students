from django.shortcuts import render
from reporting.models import Contest
from django.shortcuts import render, redirect
from django.views import View
from reporting.forms import ContestForm
from django.shortcuts import get_object_or_404


class ContestCreateView(View):
    def get(self, request):
        form = ContestForm()

        context = {
            'form': form,
        }

        return render(request, 'reporting/new_report.html', context)

    def post(self, request):
        form = ContestForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('list')

        return redirect('create')


class ReportListView(View):
    def get(self, request):
        contests = Contest.objects.all()
        
        context = {
            'contests': contests,
        }
        
        return render(request, 'reporting/report_list.html', context)


class ContestUpdateView(View):
    def get(self, request, id):
        contest = Contest.objects.get(id=id)
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


class ContestDeleteView(View):
    def get(self, request, id):
        contest = Contest.objects.get(id=id)
        
        context = {
            'contest': contest,
        }

        return render(request, 'reporting/delete_report.html', context)

    def post(self, request, id):
        contest = Contest.objects.get(id=id)
        contest.delete()
        return redirect('list')