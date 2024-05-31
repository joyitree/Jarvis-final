'''This file includes voice assitant config features 
crate an .env file in the root directory 
and place all the config/sesitive info there
install decouple module to access contents of .env file'''


from decouple import config

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')
ASSISTANT_NAME = config('ASSISTANT_NAME')
OPENWEATHER_APP_ID = config('OPENWEATHER_APP_ID')
NEWS_API_KEY = config('NEWS_API_KEY')
TMDB_API_KEY = config('TMDB_API_KEY')