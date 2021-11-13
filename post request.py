# importing the requests library
import requests
  
# defining the api-endpoint 
API_ENDPOINT = "http://ec2-34-247-37-135.eu-west-1.compute.amazonaws.com:5000/handle"
  

  
# data to be sent to api
data_Bat= { "type":"Single Battery",
"org_id":"rmFT75nxhWsHSkTpo"
,"bem_id":"PyTBT56vqaPt22mZ2",
"email":"fatima.om11@gmail.com ",
"Start":1635778688185,
"End":1636383488185
} 
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data_Bat)
  
# extracting response text 
pastebin_url = r.text
print(pastebin_url)
