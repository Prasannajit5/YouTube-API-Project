from googleapiclient.discovery import build

api_key = 'AIzaSyAFE8BMzeq8rkztWAfIfP_Hr4bSINBVaXE'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='Tseries'
    )

response = request.execute()

print(response)
