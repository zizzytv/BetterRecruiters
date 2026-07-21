import datetime 
from datetime import timezone 
from enum import Enum

date_added = datetime.now()

class ApplicationStatus(Enum):
    Applied = 1
    Saved = 2
    Assessment = 3    
    Interview = 4
    Rejected = 5
    Offer = 6
    Withdrawn = 7
    Accepted = 8 

status = ApplicationStatus()

class Job:
    def __init__(self, company_name, role, location, salary, job_description, url, status, recruiter_email, recruiter_name, source):
        self.company_name = company_name
        self.role = role              
        self.location = location
        self.salary = salary
        self.job_description = job_description
        self.url = url
        self.status = status
        self.recruiter_email = recruiter_email
        self.recruiter_name = recruiter_name
        self.source = source
    
    @property
    def company_name(self):
        return self._company_name 
    
    @company_name.setter
    def company_name(self, name):
        if not isinstance(value, (int, string)):
            raise TypeError("Company name must be text")
    if value = "":
        raise ValueError("Company name not found")
    self._company_name = value


job = Job(
    company_name = "Lockheed Martin",
    role = "Mechanical Design Engineer", 
    location = "London",
    salary = "£34,500",
    job_description = "Place Holder Text",
    url = "https://www.gradcracker.com/search/mechanical-manufacturing/engineering-graduate-jobs",
    status = ApplicationStatus.APPLIED,
    date_added = datetime.now(timezone.utc),
    recruiter_email = "john.doe@martin.co.uk",
    recruiter_name = "John Doe",
    source = "Gradcracker"
)
