from flask import Flask, render_template, redirect, g
import shopify
import ConfigParser

parser = ConfigParser.SafeConfigParser()

parser.read('config.ini')
g.api_key = parser.get('key', 'api_key')
g.shop_api_key = parser.get('key', 'shop_api_key')
g.password = parser.get('key', 'password')

g.shop_url = "https://%s:%s@choc0bot.myshopify.com/admin" % (shop_api_key, password)
shopify.ShopifyResource.set_site(shop_url)

g.shop = shopify.Shop.current()

app = Flask(__name__)

@app.route('/')
def hello_world():
    world = 'wworld'
    return render_template('index.html', world=world)

@app.route('/install')
def authurl():
    redirect_uri = 'http://choc0bot.pythonanywhere.com/success'
    scope = 'read_products,write_products,read_orders,write_orders,read_script_tags,write_script_tags'
    nonce = 'az1234'

    auth_url = 'https://choc0bot.myshopify.com/admin/oauth/authorize?client_id='+ g.api_key +'&scope='+ scope +'&redirect_uri='+ redirect_uri +'&state='+ nonce +''

    return redirect(auth_url)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/collection')
def collection():
    dacollect = []
    collection = '166429377'
    products = shopify.Product.find(collection_id=collection)
    for c in products:
        dacollect.append([c.title,c.image.src])
    return render_template('collection.html', dacollect=dacollect)