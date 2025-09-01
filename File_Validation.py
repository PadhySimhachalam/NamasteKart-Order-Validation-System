import datetime as dt
import csv


def get_product_dict():
    """Returning dictionary of product_id → price"""
    product_dict = {}
    with open('D:\\Python Programming\\Namastekart Project\\master_data\\product_master.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_dict[row['product_id']] = row['price']

    return product_dict


def get_product_id():
    """Returning list of all product_ids"""
    productid_list = []
    with open('D:\\Python Programming\\Namastekart Project\\master_data\\product_master.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            productid_list.append(row['product_id'])
    return productid_list


def product_id_validation(pid, products):
    """Checking if product_id exists in master"""
    return pid in products


def sales_amount_validation(order):
    """Validating sales = quantity × price"""
    product_dict = get_product_dict()
    if order['product_id'] in product_dict:
        return (
            int(product_dict[order['product_id']]) * int(order['quantity']) == int(order['sales'])
        )
    return False


def date_validation(date_str):
    """Validating that order_date is not in the future"""
    orders_date = dt.datetime.strptime(date_str, '%Y-%m-%d').date()
    today_date = dt.date.today()
    return orders_date <= today_date


def check_empty(order):
    """Returning list of empty columns in an order"""
    empty_cols = []
    for col, val in order.items():
        if not val or val.strip() == '':
            empty_cols.append(col)
    return empty_cols


def check_city(city):
    """Allowing only certain valid cities"""
    return city in ['Mumbai', 'Bangalore']
