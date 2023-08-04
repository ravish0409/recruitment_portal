 
from django.shortcuts import render,redirect
from .models import Job, Candidate
from .forms import JobSearchForm, CandidateProfileForm

def home(request):
    return render(request, 'home.html')

skills=0
def job_search(request):
    global skills
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            skills = form.cleaned_data['skills']
            experience = form.cleaned_data['experience']

     
            jobs = Job.objects.all()
            if location:
                jobs = jobs.filter(location__icontains=location)
            if skills:
                jobs = jobs.filter(skills_required__icontains=skills)
            if experience:
                jobs = jobs.filter(experience_level__icontains=experience)

            return render(request, 'job_search.html', {'jobs': jobs, 'form': form})
    else:
        jobs=None
        if skills:
            jobs = Job.objects.all()
            jobs=jobs = jobs.filter(skills_required__icontains=skills)
            
        form = JobSearchForm()
    
    return render(request, 'job_search.html', {'jobs': jobs,'form': form})

def candidate_profile(request):
    global skills
    if request.method == 'POST':
        form = CandidateProfileForm(request.POST)
        if form.is_valid():
            skills=request.POST['skills']
            form.save()
            return redirect('job_search')   
    else:
        form = CandidateProfileForm()

    return render(request, 'candidate_profile.html', {'form': form})