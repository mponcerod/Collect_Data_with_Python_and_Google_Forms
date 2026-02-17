# Collect_Data_with_Python_and_Google_Forms

I am collaborating in the organization of an Acroyoga community gathering named **EH SuperJam** which takes places at Garaio Lake in Euskal Herria every September. Traditionally, the event registrations are done via Google Forms and afterwards the information is copied to Google Sheet **manually**. 

The aim of this project is to collect data from Google Forms and add it into  Google Sheet file using Google Cloud and Python.

The main steps performed here are:

1. Create a Google Forms
2. Public the Google Forms and get a link: <https://docs.google.com/forms/d/e/1FAIpQLSdx2o3_rcR4EIxI8SXwgLvrRABhs6AUMLAlE0zkDMySNGXHkQ/viewform?usp=publish-editor>. The form was create for this project, the one used in the event cannot be accessed.
3. Go to Google Developer Console to:
   1. Create a project.
   2. Enable the API.
   3. Create our credentials.
   4. Enable sharing of the sheet to our email address associated with the credentials.
4. Python script using gspread and pandas 
