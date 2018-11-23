import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        f_n_content = f_n.read()
        obj = json.loads(f_n_content)
    if obj and 'orders' in obj.keys():
        old_orders = obj['orders']
    else:
        old_orders = []
    new_order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    # мы не перезаписываем, а добавляем заказ к списку более ранних
    old_orders.append(new_order)
    dict_to_json = {'orders': old_orders}
    with open('orders.json', 'w') as f_n:
        f_n.write(json.dumps(dict_to_json, indent=4))


if __name__ == '__main__':
    write_order_to_json('12345', 1, 50.09, 'Felix', '2018-11-22')
    write_order_to_json('12346', 2, 10.76, 'John', '2018-11-23')
    write_order_to_json('12381', 1, 20.00, 'Frank', '2018-11-23')
    write_order_to_json('12762', 1, 10.06, 'Dennis', '2018-11-23')
