import requests

from ln_oauth import auth, headers

credentials = 'credentials.json'
access_token = auth(credentials)  # Authenticate the API
headers = headers(access_token)  # Make the headers to attach to the API call.


def user_info(headers):
    '''
    Get user information from Linkedin
    '''
    response = requests.get('https://api.linkedin.com/v2/me', headers=headers)
    user_info = response.json()
    return user_info


# Get user id to make a UGC post
user_info = user_info(headers)
urn = user_info['id']

# UGC will replace shares over time.
api_url = 'https://api.linkedin.com/v2/ugcPosts'
author = f'urn:li:person:{urn}'
# enter the details of the post 
message = input("enter your caption for the post: ")
link_text = 'enter the detail about link'
link = 'enter the link'
# img = input("enter the name of image ") // dfzg

post_data = {
    "author": author,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": message
            },
            "shareMediaCategory": "ARTICLE",
            "media": [
                {
                    "status": "READY",
                    "description": {
                        "text": message
                    },
                    "originalUrl": link,
                    "title": {
                        "text": link_text
                    }
                }
            ]
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
    }
}

if __name__ == '__main__':
    r = requests.post(api_url, headers=headers, json=post_data)
    r.json()
