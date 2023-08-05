The project is a recruitment startup's web portal developed using Django, a popular Python web framework. The primary goal of the portal is to connect companies with potential candidates for various job roles, such as software engineers, product managers, and data scientists.

Key features of the project:

Home Page: The home page serves as the landing page for the portal. It provides a warm welcome message and encourages users to explore job opportunities and create candidate profiles. The home page also contains two prominent buttons, "Job Search" and "Create Candidate Profile," leading users to the respective pages for these actions.


![image](https://github.com/ravish0409/recruitment_portal/assets/109892241/c12a2922-5bfc-40c8-ac1c-294bab458526)

Job Search: The job search page allows users to search for job listings based on specific criteria. Users can enter skills, locations, and experience levels to narrow down their job search. The search results are displayed in a list format, showing important details such as job title, location, description, skills required, and experience level for each job listing.

![image](https://github.com/ravish0409/recruitment_portal/assets/109892241/23a585b9-0c0d-46c5-b2a2-61edf8997cc6)

Candidate Profile: The candidate profile page enables users to create and showcase their profiles. Users can enter their name, email, skills, and experience in the provided form. While the current implementation does not save the data to the database, in a complete project, the information would be stored, allowing companies to review and match potential candidates.

it redirect after you enter your details to Job Search page and show all the jobs that are match with your skills.

![image](https://github.com/ravish0409/recruitment_portal/assets/109892241/285602a6-e9f1-4761-9fa2-4a7378a4fb42)



$$ to run this project in your localhost: simply copy and paste this in cmd

git clone https://github.com/ravish0409/recruitment_portal.git

cd recruitment_portal

python -m venv env

env\Scripts\activate

pip install -r requirements.txt

python manage.py runserver


