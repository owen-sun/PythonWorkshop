'''
Created on Jul 28, 2017

@author: zgsun
'''

if __name__ == '__main__':
    fruit=("apple","banana","pear",2, True);
    print(fruit);
    
    print(fruit.index("banana"));
    print("watermellon" in fruit);
    print(fruit[0:3]);
    print(fruit[-2]);
    #k=0;
    #while(k < len(fruit)):
        #print(fruit[k]);
        #k=k+1;
    i=0;
    for i in range(len(fruit)):
        print(fruit[i]);
    a,b,c,d,e=fruit;
    print(a,b,c,d,e);