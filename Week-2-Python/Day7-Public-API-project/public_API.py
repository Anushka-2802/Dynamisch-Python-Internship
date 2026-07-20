'''
A Public API is an Application Programming Interface 
that is openly available for developers to access over the internet
It allows applications to communicate with external services 
and exchange data using HTTP methods such as GET, POST, PUT, and DELETE
'''

import requests

username = input("Enter GitHub Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    user = response.json()     # Dictionary

    print("\n========GitHub User Details==========")

    print("Name               :", user.get("name"))
    print("Username           :", user.get("login"))
    print("Bio                :", user.get("bio"))
    print("Company            :", user.get("company"))
    print("Location           :", user.get("location"))
    print("Public Repositories:", user.get("public_repos"))
    print("Followers          :", user.get("followers"))
    print("Following          :", user.get("following"))
    print("Profile URL        :", user.get("html_url"))
    print("Account Created On :", user.get("created_at"))

elif response.status_code == 404:
    print("User not found.")

else:
    print("API request failed.")