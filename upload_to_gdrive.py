import pandas as pd
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']
FOLDER_ID = '1u0ZN37F6kPWhDkUTgX5H0GRGQqa6_9RI'

def get_google_drive_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)

def download_audio(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        return True
    return False

def upload_to_drive(service, file_path, folder_id):
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata,
                                media_body=media,
                                fields='id,webViewLink').execute()
    return file.get('webViewLink')

def process_csv_file(csv_file, service):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # Add new column for Google Drive links
    df['gdrive_audio_url'] = ''
    
    # Process each row
    for index, row in df.iterrows():
        audio_url = row['url']
        filename = f"downloads/{os.path.basename(audio_url)}"
        
        print(f"Processing {filename}...")
        
        # Download the audio file
        if download_audio(audio_url, filename):
            # Upload to Google Drive
            gdrive_link = upload_to_drive(service, filename, FOLDER_ID)
            df.at[index, 'gdrive_audio_url'] = gdrive_link
            
            # Remove local file after upload
            #os.remove(filename)
        else:
            print(f"Failed to download {audio_url}")
    
    # Save updated CSV
    output_file = f"updated_{os.path.basename(csv_file)}"
    df.to_csv(output_file, index=False)
    print(f"Updated CSV saved as {output_file}")

def main():
    service = get_google_drive_service()
    
    # Process all three CSV files
    csv_files = ['files_1.csv', 'files_2.csv', 'files_3.csv']
    for csv_file in csv_files:
        print(f"\nProcessing {csv_file}...")
        process_csv_file(csv_file, service)

if __name__ == '__main__':
    main()
