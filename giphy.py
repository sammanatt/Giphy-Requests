import requests

##################################################################
# Giphy Search - Provides first url for search result from keyword
##################################################################
giphy = ""
def giphy_request(giphy_search_query):
    # Request
    # GET http://api.giphy.com/v1/gifs/search
    try:
        response = requests.get(
            url="http://api.giphy.com/v1/gifs/search",
            params={
                "api_key": "dc6zaTOxFJmzC",
                "limit": "1",
                "fmt": "json",
                "q": str(giphy_search_query),
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
        giphy_response_json = response.json()['data']
        for d in giphy_response_json:
            global giphy
            giphy = d['bitly_gif_url']
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


##################################################################
# Giphy Search -- Random result from searched keyword
##################################################################
giphy = ""
def giphy_random(giphy_search_query):
    # Request
    # GET http://api.giphy.com/v1/gifs/search
    #http://api.giphy.com/v1/stickers/random?api_key=dc6zaTOxFJmzC&tag=oops
    #http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC

    try:
        response = requests.get(
            url="http://api.giphy.com/v1/gifs/random",
            params={
                "api_key": "dc6zaTOxFJmzC",
                "limit": "1",
                "fmt": "json",
                "tag": str(giphy_search_query),
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
        giphy_response_json = response.json()['data']
        global giphy
        giphy = giphy_response_json['url']
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

