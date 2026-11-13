raw_transactions = [
    {"txn_id": "T101", "user_id": "U1", "amount": 500,
     "location": "NY", "history": ["NY", "NY"]},
    {"txn_id": "T102", "user_id": "U2", "amount": 12000,
     "location": "NY", "history": ["NY"]},
    {"txn_id": "T103", "user_id": "U1", "amount": 100,
     "location": "London", "history": ["NY", "NY"]},
]



def update_price(input_price: int, percentage: int) -> float:
    return input_price * (1 + percentage / 100)

# def add_restock(stock_count : int , new_key:str) -> None :
    
def last_sold(input_dict: dict) -> dict:
    for k in input_dict:
        input_dict[k].setdefault("last_sold", "Never")

    return input_dict


inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

def check_conditions(input_dict: dict, category: str) -> dict:
    last_sold_checked = last_sold(input_dict)

    for items in last_sold_checked.values():
        if items["stock_count"] == 0:
            items["restock_urgent"] = True

        if items["category"].lower() == category.lower():
            items["price"] = update_price(items["price"], 10)
            print("price updated")

    return last_sold_checked      


result = check_conditions(inventory, "Electronics")
for i in result:
    print(i)
 
# for items in inventory.values():
#     if items["stock_count"] == 0:
#         items["restock_urgent"] = True
#         continue
#     if items["category"] == "Electronics":
#         items["price"] = update_price(items["price"], 1.10)
#         print ('price added')


    


