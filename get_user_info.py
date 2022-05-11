from ln_oauth import auth, headers
import requests
{'localizedLastName': 'Kushwaha', 'profilePicture': {'displayImage': 'urn:li:digitalmediaAsset:C4D03AQG78STQbGwisA'}, 'firstName': {'localized': {'en_US': 'Akash'}, 'preferredLocale': {
    'country': 'US', 'language': 'en'}}, 'lastName': {'localized': {'en_US': 'Kushwaha'}, 'preferredLocale': {'country': 'US', 'language': 'en'}}, 'id': '0KT5ytYhhb', 'localizedFirstName': 'Akash'}


def user_info(headers):
    '''
    Get user information from Linkedin
    '''
    response = requests.get('https://api.linkedin.com/v2/me', headers=headers)
    user_info = response.json()
    return user_info


credentials = 'credentials.json'
access_token = auth(credentials)


{'Authorization': 'Bearer <ACCESS_TOKEN>',
 'cache-control': 'no-cache',
 'X-Restli-Protocol-Version': '2.0.0'}


if __name__ == '__main__':
    credentials = 'credentials.json'
    access_token = auth(credentials)  # Authenticate the API
    # Make the headers to attach to the API call.
    headers = headers(access_token)
    user_info = user_info(headers)  # Get user info
    print(user_info)
