import requests


def web_scrap():
    response = requests.get('https://www.google.com/')

    if response.ok:
        print('OKAY')
        return f'{response}'
        #return 'OKAY'
        #return response.text
    else:
        print('Bad Reponse')
        return 'Bad Reponse'
    
if __name__ == '__main__':
    web_scrap()
    response = requests.get('https://www.google.com/')
    print(response)