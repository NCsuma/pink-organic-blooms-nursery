class FlowerItem:
    id = None
    name = None
    image_name = None
    information = None
    price = None

    def __init__(self,id,name,image_name,information,price):
        self.id = id
        self.name = name
        self.image_name = image_name
        self.information = information
        self.price = price