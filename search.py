import requests
from rich import print
from rich.table import Table
from rich.console import Console

dom = 'outfitters.com.pk'

req = requests.get(f'https://{dom}/products.json?limit=20000000')

inp = input('(empty has all products)Input Product Title: ')

table_l = []
tab = Table(title=f'Products of {dom}')

for prod in req.json()['products']:
    table_d = {}
    if inp == '':
        table_d['title']=prod['title']
        table_d['type']=prod['product_type']
        table_d['price']=f"{str(prod['variants'][0]['price']).split('.')[0]}Rs"
        table_d['handle']=prod['handle']
        table_l.append(table_d)
    elif prod['title'].__contains__(inp):
        table_d['title']=prod['title']
        table_d['type']=prod['product_type']
        table_d['price']=f"{str(prod['variants'][0]['price']).split('.')[0]}Rs"
        table_d['handle']=prod['handle']
        table_l.append(table_d)

if len(table_l) == 0:
    print('[red1]Query is empty![/red1]')
else:
    tab.add_column("Index", justify="center", style="red")
    tab.add_column("Title", justify="center", style="cyan", no_wrap=True)
    tab.add_column("Type", justify="center", style="magenta")
    tab.add_column("Price", justify="center", style="green")
    tab.add_column("Link", justify='center', style='orange3', no_wrap=True)
    
    for i,item in enumerate(table_l):
        tab.add_row(str(int(i)+1),item['title'],item['type'],item['price'],f"https://{dom}/products/{item['handle']}")
    
    cons = Console()
    cons.print(tab)