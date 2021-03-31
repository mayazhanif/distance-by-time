import requests
import json
import pandas as pd
from time import sleep
from datetime import datetime
apikey="" #API KEY FROM mapquestapi
df = pd.DataFrame([["Time_of_Recording","Travel_Time"]])
hour=True
circle=0
while hour:
    response = requests.get('https://www.mapquestapi.com/directions/v2/route?key='+apikey+'&from=Denver%2C+CO&to=Boulder%2C+CO&outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false')
    if response.status_code == 200:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        distanceapi = json.loads(response.text)
        timenoted=distanceapi["route"]["realTime"]
        df2 = pd.DataFrame([[current_time,timenoted]])
        df=df.append(df2, ignore_index=True)
    print(df)
    sleep(300)
    ++circle
    if(circle==13):
        hour=False
