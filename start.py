import shopify

shop_url = "https://%s:%s@choc0bot.myshopify.com/admin" % ('0cecd9ca5d3ecbff5d205b6905555632', 'f948522cb1cc9910750c06b266335ecd')
shopify.ShopifyResource.set_site(shop_url)

shop = shopify.Shop.current()

# Get a specific product
product = shopify.Product.find(3927988289)

print(product.title)

"""
# Create a new product
new_product = shopify.Product()
new_product.title = "Burton Custom Freestyle 151"
new_product.product_type = "Snowboard"
new_product.vendor = "Burton"
success = new_product.save() #returns false if the record is invalid
# or
if new_product.errors:
    #something went wrong, see new_product.errors.full_messages() for example

# Update a product
product.handle = "burton-snowboard"
product.save()

# Remove a product
product.destroy()

"""