import openai
import webbrowser
import urllib.request

states = ['test']
for i in states:
  prompt = i
  response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
  )
  for i in range(len(response['data'])):
    url =response['data'][i]['url']
    urllib.request.urlretrieve(url,"./images/"+prompt+""+str(i)+".png")
