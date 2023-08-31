# Recruitment Portal
 
The project is a recruitment startup's web portal developed using Django, a popular Python web framework. The primary goal of the portal is to connect companies with potential candidates for various job roles, such as software engineers, product managers, and data scientists.

## Key features of the project:

### Home Page

The home page serves as the landing page for the portal. It provides a warm welcome message and encourages users to explore job opportunities and create candidate profiles. The home page also contains two prominent buttons:

- __Job Search__: This button leads users to the job search page, where they can search for job opportunities based on specific criteria.

- __Create Candidate Profile__: This button directs users to the candidate profile creation page, where they can showcase their skills and experience.

Feel free to customize the content and style to match your project's design and requirements.



![image](https://github.com/ravish0409/recruitment_portal/assets/109892241/c12a2922-5bfc-40c8-ac1c-294bab458526)

### Job Search

Users have the ability to input their desired skills, preferred locations, and relevant experience levels using the provided search form. This functionality empowers them to fine-tune their job search according to their individual preferences.

- __Search Results:__ The outcomes of the search are presented in a user-friendly list format. For each job listing, essential particulars, including job title, location, description, necessary skills, and experience level, are presented.

- __Matching Algorithm:__ The search algorithm adeptly matches the criteria input by the user with job listings stored in the database. This leads to the presentation of pertinent opportunities that align with the user's specific preferences.


![image](https://github.com/ravish0409/recruitment_portal/assets/109892241/23a585b9-0c0d-46c5-b2a2-61edf8997cc6)

### Candidate Profile

Users can create their profiles by completing the provided form, which includes fields for their name, email, skills, and experience. The submitted information is intended to be stored in a database in a complete project, facilitating companies in reviewing and matching potential candidates.

- __Job Search Integration:__ Upon submitting their profile details, users are seamlessly redirected to the Job Search page. There, they gain access to a curated list of job opportunities tailored to their skills. This integration significantly enhances the user experience by promptly presenting relevant job options.

- __Duplicate Profile Alert:__ To thwart duplicate submissions, a built-in mechanism detects if a candidate's information has already been submitted. In such instances, the user is promptly notified through an alert message, preventing redundancy and streamlining the profile creation process.


![image](https://github.com/ravish0409/recruitment_portal/assets/109892241/285602a6-e9f1-4761-9fa2-4a7378a4fb42)



## $$ to run this project in your localhost: simply copy and paste this in cmd

```bash

git clone https://github.com/ravish0409/recruitment_portal.git
cd recruitment_portal
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

```

