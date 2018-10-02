def data_read_file():
    d_list=[]
    d_dict={}
    with open('C:/Python34/fruits.txt','r') as fh:
    
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
    with open('C:/Python34/fruits.txt','w') as fh:           
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
add_item('vegetable','tomoto',10.0) 
        
            
        
