import datetime 
from datetime import datetime, timezone 
from enum import Enum

class ApplicationStatus(Enum):
    Applied = 1
    Saved = 2
    Assessment = 3    
    Interview = 4
    Rejected = 5
    Offer = 6
    Withdrawn = 7
    Accepted = 8 

class Job:
    status = ApplicationStatus()
    date_added = datetime.now()

    def __init__(self, comapny_name, role, location, salary, url, recruiter_email, recruiter_name, source):
        self.company_name = company_name
        self.role = role              
        self.location = location
        self.salary = salary
        self.url = url
        self.recruiter_email = recruiter_email
        self.recruiter_name = recruiter_name
        self.source = source


job = Job(
    company_name = "Lockheed Martin",
    role = "Mechanical Design Engineer", 
    location = "London",
    salary = "£34,500",
    job_description = "Place Holder Text",
    url = "https://www.gradcracker.com/search/mechanical-manufacturing/engineering-graduate-jobs",
    status = ApplicationStatus.APPLIED,
    date_added = datetime.now(timezone.gmt),
    recruiter_email = "john.doe@martin.co.uk",
    recruiter_name = "John Doe",
    source = "Gradcracker"
)
