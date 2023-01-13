from tkinter import *
from tkinter import filedialog
import pandas as pd
import os
pd.options.mode.chained_assignment = None # default='warn'


def insertRow(row_number, df, row_value):
    # Upper part of dataframe
    df1=df[0:row_number]
    
    # Lower part of dataframe
    df2=df[row_number:]
    
    # Insert the row in the upper part of the dataframe and concatenate
    
    
    df1.loc[row_number,:] = row_value
    df_result = pd.concat([df1, df2])
    
    # Redo index labels
    
    df_result.index = [*range(df_result.shape[0])]
    
    # Return new dataframe
    
    return df_result

def analyzeFile():
    filepath = filedialog.askopenfilename(initialdir="Z:\\DATA",
                                          title="Choose your measurement log",
                                          filetypes=((".csv","*.csv"),("all files","*.*")))
    df = pd.read_csv(filepath)
    
    # Clean the data output to include only slice and length 
    
    df_clean = df[['Slice','Length']]
  
    
    # Cull the bad rows
    #If a row below is less than the row above
    #Then delete all rows where the value is greater than or equal to the current row value until you reach the new row index
    cullable_indices = []
    for i in range(0,len(df_clean)-1):
        if df_clean.Slice[i] >= df_clean.Slice[i+1]:
            critical_slice = df_clean.Slice[i+1]
            for j in range(0,i+1):
                if df_clean.Slice[j] >= df_clean.Slice[i+1]:
                    cullable_indices.append(j)
                    
    
    df_clean = df_clean.drop(cullable_indices)
    print(df_clean)
    df_clean = df_clean.reset_index(drop=True)
    print(df_clean)



    
    # Replicate row lengths for missing slices
    # Make sure that a row for each time slice exists.
    # If you need to insert a row, copy the length from the previous row
     
    df_cleaner = df_clean
    
    print(range(1,int(df_clean.Slice.iloc[-1])))

    for k in range(1,int(df_clean.Slice.iloc[-1])):
        if not k in df_clean['Slice'].values:
            df_cleaner = insertRow((k-1),df_cleaner,[k,df_cleaner.Length[k-2]])
            
            
    # Output the cleaned csv file
    output_directory = os.path.dirname(filepath)
    basename = os.path.basename(filepath).split('.',1)[0]
    outputname = basename+"_cleaned.csv"
    output_path = output_directory + "//" + outputname
    df_cleaner.to_csv(output_path, encoding='utf-8')

    print("Finished Processing File")
    
    # DESTROY THE SELECTION BUTTON
    # window.destroy()

            
    
if __name__ == '__main__':
    window = Tk()
    button = Button(window, text="Click here to open your measurement log!", command=analyzeFile)
    button.pack(fill = X)
    window.mainloop()       
    