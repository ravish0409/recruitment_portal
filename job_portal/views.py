 
from django.shortcuts import render,redirect
from .models import Job, Candidate
from .forms import JobSearchForm, CandidateProfileForm
import json
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
    show_alert = False
    if request.method == 'POST':
        form = CandidateProfileForm(request.POST)
        if form.is_valid():
            skills=request.POST['skills']
            name=request.POST['name']
            email=request.POST['email']
            with open("job_portal/registered_candidates.json", 'r') as file:
                data: dict = json.load(file)
            for i in data["users"]:
                if i["email"]==email:
                    show_alert=True
                    cname=i['name']
                    break
            if show_alert:
                if cname!=name:
                    cname=name+" or "+cname
                message=f"Mr. {cname}\nyour application is under process"
                return render(request,'candidate_profile.html',{'message':message,'show_alert': show_alert})
            data["users"].append({"email":email,"name":name})
            with open("job_portal/registered_candidates.json", 'w') as file:
                json.dump(data,file,indent=2)
            form.save()
            return redirect('job_search')   
    else:
        form = CandidateProfileForm()

    return render(request, 'candidate_profile.html', {'form': form,'show_alert': show_alert})