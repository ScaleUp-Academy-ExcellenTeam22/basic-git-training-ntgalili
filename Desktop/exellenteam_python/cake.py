

def get_recipe_price(prices,optional=[],**ingredients):
    result=0
    for product in ingredients:
        if product not in optional:
            result+=prices[product]*ingredients[product]
    return result


#print(get_recipe_price(prices={'c':5,'a':3},c=10,a=1,optional=['a']))

