from httplib2 import Http
from json import dumps

#
# Hangouts Chat incoming webhook quickstart
#
def main():

    key = ''
    url = 'https://chat.googleapis.com/v1/spaces/AAAAVtjo5fA/messages?key='
    url = url + key;
    bot_message = {
        'text' : ' @JMANGAS worklog is empty!'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()

