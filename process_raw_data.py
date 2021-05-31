
import glob
import pandas as pd
import os

def readRawDataFiles():
    if os.path.exists("raw_data/iowa.csv")==False:
        all_files = glob.glob("raw_data/*")
        iowa_data_df = pd.DataFrame()
        for file_num,eachfile in enumerate(all_files): 
            iowa_data_df = iowa_data_df.append( pd.read_csv(eachfile,low_memory=False))
            print(f"Finished appending {file_num+1} files")
        iowa_data_df.to_csv("raw_data/iowa.csv",index=False)

def readWholeIowaData():
    return pd.read_csv("raw_data/iowa.csv",low_memory=False)

def main():
    pd.set_option('display.expand_frame_repr', False)
    # Read in the csv files from raw data directory
    readRawDataFiles()
    
    iowa_data_df = readWholeIowaData()
    print(iowa_data_df.shape)
    iowa_data_df = iowa_data_df.drop_duplicates()
    print(iowa_data_df.shape)
    
    iowa_data_df['sampleDate']= pd.to_datetime(iowa_data_df['sampleDate']).dt.date
    #iowa_data_df['analyte'] = iowa_data_df['analyte'].str.replace('(AS ','(as ')
    

    #print("\n".join(list(iowa_data_df.name.unique())))
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    #print(iowa_data_df.name.value_counts())
    
    #iowa_data_df_with_chlorophyll = iowa_data_df.loc[iowa_data_df['analyte'] == "Chlorophyll a, free of pheophytin"]
    iowa_data_df_with_chlorophyll = iowa_data_df[iowa_data_df['analyte'].str.contains('Chlorophyll', case=False)]
    print(iowa_data_df_with_chlorophyll.shape)
    unique_sites = iowa_data_df_with_chlorophyll.name.unique()
    for num,each_water_body_name in enumerate(unique_sites):
        iowa_data_df_each_water_body_name = iowa_data_df.loc[iowa_data_df['name'] == each_water_body_name]
        iowa_data_df_each_water_body_name = iowa_data_df_each_water_body_name.sort_values(by = 'sampleDate')
        #print(iowa_data_df_each_water_body_name[['sampleDate', 'analyte','result']])
        unique_analytes = list(iowa_data_df_each_water_body_name.analyte.unique())
        column_names = []
        column_names.extend(unique_analytes)
        new_df = pd.DataFrame(columns = column_names)
        for index, row in iowa_data_df_each_water_body_name.iterrows():
            new_df.append(pd.Series(name=row["sampleDate"]))
            new_df.loc[row["sampleDate"],row["analyte"]] = row["result"]
        
        if new_df.shape[0]>100:
            new_df.to_csv(f"raw_data/{each_water_body_name}.csv",sep = '\t')
            print(f"Processing data for {len(unique_sites)} {num+1} {each_water_body_name} {new_df.shape}")
        else:
            print(f"Skipping {each_water_body_name}")
            os.system(f"rm \"raw_data/{each_water_body_name}.csv\"")
        #print(iowa_data_df_each_water_body_name.analyte.value_counts())
        #print(f"Total analytes {len(list(iowa_data_df_each_water_body_name.analyte.unique()))}")
        
        #print(iowa_data_df_each_water_body_name.shape)
        #print(iowa_data_df_each_water_body_name.pivot(index='sampleDate', columns='analyte'))
    
    


if __name__ == "__main__":
    main()