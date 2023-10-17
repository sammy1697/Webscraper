import requests

import time

import csv

 

# Function to fetch job details from the API

def get_job_details(query, page=1, date_posted="month"):

    # API endpoint

    url = "https://jsearch.p.rapidapi.com/search"

 

    # Parameters for the API request

    querystring = {"query": query, "page": page, "date_posted": date_posted}

 

    # Headers for the API request

    headers = {"X-RapidAPI-Key": "c331737b57mshe8b45ccffc8e3b3p1ef88ajsnddc8a9e36f22", "X-RapidAPI-Host": "jsearch.p.rapidapi.com"}

 

    # Making a GET request to the API and handling any potential errors

    try:

        response = requests.get(url, headers=headers, params=querystring)

        response.raise_for_status()

    except requests.exceptions.HTTPError as errh:

        print ("HTTP Error:", errh)

    except requests.exceptions.ConnectionError as errc:

        print ("Error Connecting:", errc)

    except requests.exceptions.Timeout as errt:

        print ("Timeout Error:", errt)

    except requests.exceptions.RequestException as err:

        print ("Oops: Something Else", err)

 

    # Converting the response to JSON

    json_result = response.json()

 

    # Extracting the 'data' field from the response

    query_result = json_result.get("data", [])

    print(query_result)

    job_details = []

    # Iterating over each job in the 'data' field

    for change in query_result:

        # Extracting the necessary fields from each job

        job_detail = {

            "title": change.get("job_title", ""),

            "location": f"{change.get('job_city', '')}, {change.get('job_state', '')}, {change.get('job_country', '')}",

            "coordinates": f"{change.get('job_latitude', '')}, {change.get('job_longitude', '')}",

            "Remote": change.get("job_is_remote", ""),

            "no_experience_required": change.get("no_experience_required", ""),

            "required_experience_in_months": change.get("required_experience_in_months", ""),

            "job_employment_type": change.get("job_employment_type", ""),

            "salary": change.get("job_min_salary", ""), "description": change.get("job_description", ""),

            "job_link": change.get("job_google_link", ""), "Date": change.get("job_posted_at_datetime_utc", "")

        }

        # Adding the job details to our list

        job_details.append(job_detail)

 

    return job_details

 

# Function to print the details of each job

def print_job_details(job_details):

    # Printing the number of jobs found

    print(f"Number of jobs found: {len(job_details)}")

 

    # Printing the details of each job

    for job in job_details:

        print(f"\nJob title: {job['title']}")

        print(f"Job location: {job['location']}")

        print(f"Job coordinates: {job['coordinates']}")

        print(f"Is Job Remote: {job['Remote']}")

        print(f"Is Experience Required: {job['no_experience_required']}")

        print(f"Required Experience: {job['required_experience_in_months']}")

        print(f"Employement Type: {job['job_employment_type']}")

        print(f"Job salary: {job['salary']}")

        print(f"Job link: {job['job_link']}")

        print(f"Date posted: {job['Date']}")

        print(f"description: {job['description']}")
 

# Function to write job details to a CSV file

def write_to_csv(job_details, filename):

    # Specify the fieldnames for the CSV

    fieldnames = ["title", "location", "coordinates", "Remote", "no_experience_required", "required_experience_in_months", "job_employment_type", "salary", "job_link", "description", "Date"]

 

    # Open the CSV file in write mode

    with open(filename, mode='w', newline='') as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

 

        writer.writeheader()

        for job in job_details:

            writer.writerow(job)

 

# Main function to call other functions

def main():

    # Job titles to be searched

    job_titles = ["Sustainable Finance Analyst", "Energy Storage Specialist",

                   "Renewable Energy Engineer", "Energy Policy Advisor",

                   "Energy Systems Analyst", "Energy Policy Analyst",

                   "Urban Energy Planner", "Renewable Energy Consultant",

                   "Energy Management Consultant", "Energy Data Scientist",

                   "Wind Power Engineer", "Renewable Enegry Specialist", "Solar Energy Technician",

                   "Hydroelectric Power Analyst", "Biomass Energy Consultant", "Geothermal Energy Expert"

                   "Energy Efficiency Consultant", "Smart Grid Engineer", "Energy Storage Specialist", "Clean Energy Project Manager",

                   "Carbon Reduction Specialist", "Climate Change Mitigation Advisor", "Greenhouse Gas Emissions Analyst", "Low-Carbon Technology Consultant",

                   "Circular Economy Strategist", "Sustainable Transportation Planner", "Eco-Friendly Practices Consultant", "Carbon Offset Analyst",

                   "Urban Planner", "Green Infrastructure Specialist", "Sustainable Architecture Designer", "Urban Development Consultant", "Smart Cities Analyst",

                   "Eco-Friendly Building Designer", "Urban Regeneration Expert", "Low Impact Design Consultant", "Urban Mobility Planner", "Resilient Cities Strategist",

                   "Sustainable Business Manager", "Green Finance Analyst", "Corporate Sustainability Specialist", "Impact Investing Advisor"

                   "Environmental Economist", "Public-Private Partnership Coordinator", "Sustainable Supply Chain Manager", "Social Responsibility Consultant",

                  "Sustainable Investment Analyst", "Circular Economy Business Strategist", "Sustainable Construction Manager", "Resilience Planning Specialist",

                  "Green Building Materials Expert", "Energy-Efficient Building Designer", "Energy Project Manager", "Energy Technology Analyst", "Energy Policy Developer",

                  "Renewable Energy Targets Analyst", "Energy Regulations Specialist", "Public-Private Cooperation Specialist", "Sustainable Banking Manager",

                  "Green Bonds Analyst", "ESG (Environmental, Social, Governance) Analyst", "Climate Finance Specialist"]

 

    # Looping over job titles

    for job_title in job_titles:

        job_details = get_job_details(f"{job_title} in Switzerland")

 

        # Printing job details

        print_job_details(job_details)

 

        # Write to CSV

        write_to_csv(job_details, f"{job_title.replace(' ', '_')}_job_details.csv")

 

        # Wait for 10 seconds before the next request

        time.sleep(10)

 

# Ensures main() is run when this script is run directly

if __name__ == "__main__":

    main()
