def messages(msg):
    if msg == 'greater_than_stock':
        return 'Quantity ordered is greater than the stock'
    elif msg == 'not_stock':
        return 'There are no products in stock :('
    elif msg == 'low_stock':
        return 'Low stock level'