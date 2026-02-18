# Collect_Data_with_Python_and_Google_Forms

I am collaborating in the organization of an Acroyoga community gathering named **EH SuperJam** which takes places at Garaio Lake in Euskal Herria every September. The aim of this project is to collect data from Google Forms using Google Cloud and Python. This is an example on how we can collect data from the server from different years and generate a dashboard with relevant information of the event and it fluctioations.

## Main steps

The main steps performed here are:

1. Create a Google Forms
2. Public the Google Forms and get a link: <https://docs.google.com/forms/d/e/1FAIpQLSdx2o3_rcR4EIxI8SXwgLvrRABhs6AUMLAlE0zkDMySNGXHkQ/viewform?usp=publish-editor>. The form was create for this project, the one used in the event cannot be accessed.
3. Go to Google Developer Console to:
   1. Create a project.
   2. Enable the API.
   3. Create our credentials.
      1. Google Auth platform > Clients > Create Client > Application Type > Select Desktop app > Create > Save the downloaded JSON file
   4. Enable sharing of the sheet to our email address associated with the credentials.
4. Create a Github project
5. Create a virtual environment using `uv`.
6. Develop .py files.


## Create a virtual environment using `uv`

Following the guidelines in <https://docs.astral.sh/uv>. I create a virtual environment to work in the project.

```
# 1. Install uv

# 2. Create a virtual environment
uv venv

# 3. Initialize the project
uv init 

# 4. Install libraries
uv add ***
```
