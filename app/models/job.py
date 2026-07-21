import datetime 
from datetime import timezone 
from enum import Enum

class ApplicationStatus(Enum):
    APPLIED = 1
    SAVED = 2
    ASSESSMENT = 3    
    INTERVIEW = 4
    REJECTED = 5
    OFFER = 6
    WITHDRAWN = 7
    ACCEPTED = 8 

class Job:
    
    def __init__(self, company_name, role, location, url, status, date_added):
        self.company_name = company_name
        self.role = role              
        self.location = location
        self.url = url
        self.status = ApplicationStatus.SAVED
        self.date_added = datetime.now(timezone.utc)

    @property
    def company_name(self):
        return self._company_name 
    
    @property
    def role(self):
        return self._role

    @property 
    def location(self):
        return self._location

    @property 
    def url(self):
        return self._url
  
    @company_name.setter
    def company_name(self, name):
        if not isinstance(name,str):
            raise TypeError("Company name must be text")
        if name == "   " or name == "":
            raise ValueError("Company name not found")
        self._company_name = name

    @role.setter
    def role(self, position):
        if not isinstance(position,str):
            raise TypeError("Role is not a text")
        if position == "   " or position == "":
            raise ValueError("Role does not exist")
        self._role = position

    @location.setter
    def location(self, place):
        if not isinstance(place,str):
            raise TypeError("Location is not in text format")
        if place == "    " or place == "":
            raise ValueError("A location is not stated")
        self._location = place

    @url.setter
    def url(self, link):
        if not isinstance(link,str):
            raise TypeError("Link is not in a readable format")
        if link == "   " or link == "":
            raise ValueError("Link does not exist")
        if not link.startswith("https://") and not link.startswith("http://"):
            raise ValueError("Link does not start with http or https") 
        self._url = link

    def __str__(self):
        return f'Job({self.company_name},{self.role},{self.location},{self.url},{self.status},{self.date_added})'

job = Job(
    company_name = "Lockheed Martin",
    role = "Mechanical Design Engineer", 
    location = "London",
    url = "https://www.gradcracker.com/search/mechanical-manufacturing/engineering-graduate-jobs",
    status = ApplicationStatus.APPLIED,
    date_added = datetime.now(timezone.utc)
)

print(job) 
