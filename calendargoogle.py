from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE='client_secret_998000070089-urmi8lfnd7q0984n7kbigrg4cvl95u1c.apps.googleusercontent.com'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)