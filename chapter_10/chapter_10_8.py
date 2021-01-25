#8
class Retail_Item:
    def __init__(self, desc_product, qty, price):
        self.desc_product = desc_product
        self.qty = qty
        self.price = price

product_1 = Retail_Item('Пиджак', 12, 59.95)
product_2 = Retail_Item('Дизайнерские джинсы', 40, 34.95)
product_3 = Retail_Item('Рубашка', 20, 24.95)

class CashRegister:
    def __init__(self):
        self.shop_list = []

    def purchase_item(self, argument):
        self.shop_list.append(argument.__dict__)
    
    def get_total(self):
        dict_summa = {}
        list_summa = []
        for thing in self.shop_list:
            for key, value in thing.items():
                dict_summa[key] = value
                if 'price' in dict_summa:
                    summa = dict_summa['price']
            list_shop.append(summa)
            result = sum(list_shop)
        print(result)
    
    def show_items(self):
        dict_clothes = {}
        list_clothes = []
        for thing in self.shop_list:
            for key, value in thing.items():
                dict_clothes[key] = value
                if 'desc_product' in dict_clothes:
                    clothes = dict_clothes['desc_product']
            list_clothes.append(clothes)
            result = '\n'.join(list_clothes)
        print(f'Выбранный вами ассортимент: \n{result}')

    def clear(self):
        self.shop_list.clear()


list_shop = CashRegister()
list_shop.purchase_item(product_1)
list_shop.purchase_item(product_2)
print(list_shop.shop_list)
list_shop.get_total()
list_shop.show_items()
list_shop.clear()
print(list_shop.shop_list)
