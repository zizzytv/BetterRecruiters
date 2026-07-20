
Describe the setup of the job model, job.py, set up and how it will run going forwards 

# Table of Setup

## Main

| Field           | Type       | Required?     | Description                                                 |
|-----------------|------------|---------------|-------------------------------------------------------------| 
| ID              | Integer    | Yes           | Unique ID of job page                                       |
| Company Name    | String     | Yes           | Stores the name of the company as a string                  |
| Role            | String     | Yes           | e.g Mechanical Design Engineer, Software Engineer, etc      |
| Location        | String     | Yes           | e.g Conventry, London, South East England, etc              |
| Salary          | String     | Yes           | e.g 35k, Compettive, Not Listed, 28,000, £43,000            |
| Job Description | String     | No            | AI-assisted scanning of the descripton                      |
| Url             | String     | No            | Link to job page directed, not third-party job listing      |
| Status          | String     | No            | e.g Applied, Rejected, Withdrawn, Saved, Waiting            |
| Date Added      | String     | No            | e.g 12/05/2026, 12th of September 2026, May 2024, 2026      |
| Email/Contacts  | String     | No            | e.g taylor.diamond@yahoo.ac.uk,sarah.rose@businessltd.co.uk |

## Application Status

| Field          | Type       | Description                                                                         |
|----------------|------------|-------------------------------------------------------------------------------------|
| Applied        | String     | Applied to the job, status will change to waiting period after a day                |
| Waiting        | String     | This status is transitional, waiting for the application to be moved on or rejected |
| Saved          | String     | No application was sent, just saved into a database                                 |
| Assessment     | String     | Moved to assessment process                                                         |
| Interview      | String     | Moved to interview process                                                          |
| Rejected       | String     | Application was rejected                                                            |
| Offer          | String     | Offer was given for the job                                                         |
| Withdrawn      | String     | Application was withdrawn                                                           |
| Accepted       | String     | Offer was accepted                                                                  |

