import retail_store as rs

def item_cgry_lst():
    print('Below are the item categories available in store right now')
    add_dict=rs.data_read_file()
    for k in add_dict:
        print(k)

def item_lst(itm_catg):
    add_dict=rs.data_read_file()
    if itm_catg not in add_dict:
        print('Please provide correct Item Category from above list given')
    add_lst=add_dict[itm_catg]
    print('Below are the items availabe for sale with prices')
    for dct in add_lst:
        for k,v in dct.items():
            print(k+': '+str(v))
            
def first_item(shp_lst):
    buy_lst=[]
    if len(shp_lst.split(',')) != 2:
        print('Please enter correct details with item name comma separated by quantity')
    buy_lst.append(shp_lst.split(','))
    return buy_lst

item_cgry_lst()
n=0
str1=''
buy_lst=[]
while n < 100:
    if n > 0:
        str1='one more'    
    item_ctgry=input('Please enter '+str1+' item category you would like to shop: ')
    if item_ctgry.upper() == 'NO':
        break
    item_lst(item_ctgry)
    item_qty=input('Now provide the Item with quantity to buy\nExample: apple,2\n')
    buy_lst=buy_lst+first_item(item_qty)
    i=0
    while i < 100:
        cntnty_chk=input('Would you like to buy one more item from same category? tyep YES or NO\n')
        if cntnty_chk.upper() == 'YES':
            item_qty=input('Now provide the Item with quantity to buy\nExample: apple,2\n')
            buy_lst=buy_lst+first_item(item_qty)
        else:
            break
        i=i+1
    n=n+1    
print(buy_lst)
