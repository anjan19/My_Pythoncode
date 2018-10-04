
def data_read_file():
    d_list=[]
    d_dict={}
    with open('D:\Anjan\GCP\PythonProject\FileToWrite.txt','r') as fh:
    
        for line in fh:
            if line.split(',')[0] in d_dict:
                d_list.append({line.split(',')[1]:float(line.split(',')[2])})
                d_dict[line.split(',')[0]]=d_list
            else:
                d_list=[{line.split(',')[1]:float(line.split(',')[2])}]
                d_dict[line.split(',')[0]]=d_list        
        fh.close()
        return d_dict


def data_write_file(i_dict):
    d_dict=i_dict
    with open('D:\Anjan\GCP\PythonProject\FileToWrite.txt','w') as fh:           
        for k,v in d_dict.items():
            for d in v:
                for k1,v1 in d.items():
                    fh.write(k+','+k1+','+str(v1)+'\n')
        fh.close()     

def add_item(itm_typ,itm_nm,itm_prc):
    add_dict=data_read_file()
    #print(add_dict) 
    add_lst=[]
    itm_chk=False
    if itm_typ in add_dict:
        add_lst=add_dict[itm_typ]
        for dct in add_lst:
            for k in dct:
                if k == itm_nm:
                    itm_chk=True
                    break        
        #print(itm_chk)
        if itm_chk == True:
            print(itm_nm+': This item is already exists in store')
        else:
            add_dict[itm_typ]=add_lst+[{itm_nm:itm_prc}]
            print(itm_nm+': is successfully added to store')
    else:
        add_dict[itm_typ]=[{itm_nm:itm_prc}]
        print(itm_nm+' with '+itm_typ+' item category is successfully added to store')   
    data_write_file(add_dict)

def update_item(itm_typ,itm_nm,itm_prc):
    add_dict=data_read_file()
    add_lst=[]
    itm_chk=False
    if itm_typ in add_dict:
        add_lst=add_dict[itm_typ]
        for dct in add_lst:
            if itm_nm in dct:
                itm_chk=True
                add_lst.remove(dct)
                add_lst.append({itm_nm:itm_prc})
                add_dict[itm_typ]=add_lst
                print(itm_nm+': is successfully updated in store')
        if itm_chk == False:
            print(itm_nm+': is not availbale in store,Check and provide correct item name')
    else:
        print(itm_typ+': This item category is not available in  store')
    data_write_file(add_dict)

update_item('phone','redmi1',3500.0)     
        
def delete_item(itm_typ,itm_nm,itm_prc):
    add_dict=data_read_file()
    add_lst=[]
    itm_chk=False
    if itm_typ in add_dict:
        add_lst=add_dict[itm_typ]
        for dct in add_lst:
            if itm_nm in dct:
                itm_chk=True
                add_lst.remove(dct)
                add_dict[itm_typ]=add_lst
                print(itm_nm+': is successfully deleted from store')
        if itm_chk == False:
            print(itm_nm+': is not availbale in store,Check and provide correct item name')
    else:
        print(itm_typ+': This item category is not available in  store')
    data_write_file(add_dict)
    
delete_item('vegetable','tomoto',20.0) 
