import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# using glob module to read csv files from  folder
# reading folder - archive/crime
count=0
li = []
c,x = 0,[]
d,y = 0,[]

# here we runing loop on  csv files
for filename in glob.iglob('/home/admin123/Data_Validation/archive/crime/**/*.csv',recursive = True):
    
    # cheching file size
    if os.stat(filename).st_size == 0:
        os.remove(filename)
        d+=1
        y.append(d)
        print('File is empty',filename)
    else:
        fileSize = os.path.getsize(filename)
        print(fileSize,"Its a file size of",filename)
        c += 1
        x.append(c)
        
    
    # reading csv file
    df = pd.read_csv(filename)
    li.append(df)
    
    # deleting empty and NaN rows
    df.dropna(inplace = True)
    
    # uniqeness check (if there is any duplicate data so drop that row)
    df.drop_duplicates(inplace = True)
    
    # Range check - if data is negative so drop that row
    a = df.select_dtypes(include = ['int64','float64'])
    cl=[]
    for i in a.columns:
        for x_ in a.index:
            if a.loc[x_, i] < 0:
                df.drop(x_, inplace = True)
    
    # delete if no of columns is not equal to no of columns in each row
    no_of_columns = len(df.columns)
    for i in df.index:
        col_in_row = df.loc[i]
        if len(col_in_row) != no_of_columns:
            df.drop(i,inplace=True)
    
    # check the data type od columns
    for data_t in df:
        data_type =  df[data_t].dtypes
        # print(data_type)
        
    df.to_csv(filename,index=False)
    count+=1
    

# creating graph
font1 = {'family':'serif','color':'darkred','size':12}
font2 = {'family':'serif','color':'darkred','size':12}
font3 = {'family':'serif','color':'blue','size':20}

plt.title("File Analysis",fontdict = font3)
plt.xlabel("Correct_File",fontdict = font1)
plt.ylabel("Defected_File",fontdict = font2)
plt.grid(True, linewidth= 1, linestyle="--") 
plt.plot(x,"o-")
plt.plot(y,"*-")
plt.show()
    
   


