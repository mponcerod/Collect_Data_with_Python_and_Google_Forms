from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive   
import pandas as pd

# Initializing a GoogleAuth Object
gauth = GoogleAuth()

# Creates local webserver and auto handles authentication
gauth.LocalWebserverAuth()

# Creates GoogleDrive instance with authenticated GoogleAuth instance
drive = GoogleDrive(gauth)

# Initialize GoogleDriveFile instance with file id
# Download the file as excel file and read it as a dataframe using pandas
file_object = drive.CreateFile({'id': 'FILE_ID'})
file_object.GetContentFile('FILE_NAME.xlsx',
         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# Read the excel file as a dataframe and print it
df = pd.read_excel('FILE_NAME.xlsx')
print(df)

# Add new column
df["Pagado"] = "No"

# Save the modified dataframe back to excel file
df.to_excel("FILE_NAME_mod.xlsx", index=False)

# Upload back to Drive (replaces file)
file_object.SetContentFile("FILE_NAME_mod.xlsx")
file_object.Upload()