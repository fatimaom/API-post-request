# importing the requests library
import requests
  
# defining the api-endpoint 
API_ENDPOINT ="http://localhost:5000/handle"
  

  
# data to be sent to api
data_Bat= { "start":1635778688185,
"end":1636383488185
} 
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data_Bat)
  
# extracting response text 
pastebin_url = r.text
print(pastebin_url)
