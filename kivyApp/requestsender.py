import json
import urllib3

def post_request(name, description, price, qty , url):
    """Function that send post request to crud project
    
    Arguments:
        name {[str]} -- [name of product]
        description {[str]} -- [description of product]
        price {[int]} -- [price of product]
        qty {[int]} -- [quantity of product]
        url {[str]} -- [URL to send the post request]
    """    
    encoded_body = json.dumps(
        {   
        "name": name,
        "description": description,
        "price": price,
        "qty": qty,
        })

    http = urllib3.PoolManager()

    r = http.request('POST', 'http://localhost:5000/product',
                 headers={'Content-Type': 'application/json'},
                 body=encoded_body)

    print (r.read())


def delete_request(id, url):
    """Function that send delete request to crud project
    
    Arguments:
        id {[str]} -- [id of product to delete]
        url {[str]} -- [URL to send the post request]
    """    

    http = urllib3.PoolManager()
    r = http.request('DELETE', f'http://localhost:5000/product/{id}',
                 headers={'Content-Type': 'application/json'})

    print (r.read())

def get_request(id ,url):
    """Function that send get request to crud project
    
    Arguments:
        id {[str]} -- [id of product to get]
        url {[str]} -- [URL to send the post request]
    """    

    http = urllib3.PoolManager()
    r = http.request('GET', f'http://localhost:5000/product/{id}',
                 headers={'Content-Type': 'application/json'})

    new_product = json.loads(r.data)
    #print(y['name'])
    return product(new_product['name'], new_product['description'], new_product['price'], new_product['qty'])
    

class product:
    def __init__(self , name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

if (__name__ == "__main__"):
    #post_request("tv", "something to watch", 1500,50,"")
    prod = get_request(3,"")
    print(prod.name)