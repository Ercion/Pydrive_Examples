'''
Created on Fri Jul 3 2020

@author: Ercan Karacelik

'''

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    #gauth.LocalWebserverAuth()
    gauth.LocalWebserverAuth("localhost", [3000, 8080])
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

# get google folder or file id
'''
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == "your_folder"):
      fileID = file['id']
'''

#Create file in google drive and set content for file
fileName='Hello.txt'
file1 = drive.CreateFile({'title': fileName})
file1.SetContentString('Hello')
file1.Upload() # Files.insert()


#Upload file to google drive
file1 = drive.CreateFile()
file1.SetContentFile('pydrive_lib_test.py') # file name you want to upload
file1.Upload()


#Delete File that is under the specific folder
folder_id='your_folder_id'
#fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList() - Get list all fies under the root
file_list1 = drive.ListFile({'q': " '{0}' in parents and trashed=false".format(folder_id)}).GetList() #Get list all fies under the specific file 
for file1 in file_list1:
    print('title: %s, id: %s' % (file1['title'],file1['id']))
    file1.Delete()

#Upload File inside google drive folder
folder_id='your_folder_id'
file2=drive.CreateFile({"parents":[{"kind":"drive#fileLink","id":folder_id}]})
file2.SetContentFile('pydrive_lib_test.py')
file2.Upload()

#Download file from google drive folder
folder_id='your_folder_id'
file_list1 = drive.ListFile({'q': " '{0}' in parents and trashed=false".format(folder_id)}).GetList()
for file1 in file_list1:
    print('title: %s, id: %s' % (file1['title'],file1['id']))
    file1.GetContentFile(file1['title'])
    permissions = file1.GetPermissions() #List Permission
    print(permissions)
    
    
# To create a new folder
folder_name = "ercan_pydrive_folder"
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
fileID = None
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if file['title'] == folder_name:
      fileID = file['id']

if fileID is None:
    folder = drive.CreateFile({'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()