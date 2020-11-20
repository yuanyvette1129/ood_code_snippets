

class Product:

    def __init__(self,product_id,price):
    	"""
    	contains two attributes: product_id and price
    	"""
        self.product_id = product_id
        self.price = price

    def getPrice(self):
    	"""
    	return the price of the product
    	"""
        return self.price



class Variation():

    def __init__(self,parent,children):
    	"""
    	contains two attributes: a list of parent categories and a list of children categories. 
    	"""
        self.parent = parent   
        self.children = children   

    def getAverageFamilyPrice(self):
    	"""
    	return the average price for parent and children categories
    	"""
        child_prices = [c.getPrice() for c in self.children]
        parent_prices = [p.getPrice() for p in self.parent]
        return sum(child_prices+parent_prices)/(len(child_prices)+len(parent_prices))

# test

snowboots = Product('112',30)
rainboots = Product('113',50)
boots = Product('11',20)
variation = Variation([boots],[snowboots,rainboots])
print(snowboots.getPrice())
print(rainboots.getPrice())
print(boots.getPrice())
print(variation.getAverageFamilyPrice())


	
