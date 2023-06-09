import requests


def get_json_data(url,params):
    '''
    Funkcija dohvaca json podatke s url-a i s definiranim parametrima

    Ako se dogodila greska, tj. status code nije bio 200 ili se dogodio exception,
    funkcija vraca None.
    '''
    try: 
        response=requests.get(url,params=params)
        if response.status_code != 200: 
            print(f'Error, status code{response.status_code}, response {response.text}')
            return None
        return response.text
    except Exception as e:
        print(e)
        return None
    


def test():
    parameters={'latitude':45.81,'longitude':15.98,'hourly':'temperature_2m'}
    
    json_text=get_json_data('https://vrijeme.hr/hrvatska_n.xml',params=parameters)

    print (json_text)

if __name__=='__main__': 
    test()

