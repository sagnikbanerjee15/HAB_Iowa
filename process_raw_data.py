
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
    #print("\n".join(list(iowa_data_df.name.unique())))
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    #print(iowa_data_df.name.value_counts())
    
    iowa_data_df_Bloody_Run_Creek_Site_1_BR01 = iowa_data_df.loc[iowa_data_df['name'] == 'Bloody Run Creek Site #1 (BR01)']
    iowa_data_df_Bloody_Run_Creek_Site_1_BR01 = iowa_data_df_Bloody_Run_Creek_Site_1_BR01.sort_values(by = 'sampleDate')
    #print(iowa_data_df_Bloody_Run_Creek_Site_1_BR01.shape)
    print(iowa_data_df_Bloody_Run_Creek_Site_1_BR01[['sampleDate', 'analyte','result']])
    print(list(iowa_data_df_Bloody_Run_Creek_Site_1_BR01.analyte.unique()))
    print(f"Total analytes {len(list(iowa_data_df_Bloody_Run_Creek_Site_1_BR01.analyte.unique()))}")
    
    print(iowa_data_df_Bloody_Run_Creek_Site_1_BR01.pivot(index='sampleDate', columns='analyte', values='result'))
    print(iowa_data_df_Bloody_Run_Creek_Site_1_BR01.shape)
    #print(iowa_data_df_Bloody_Run_Creek_Site_1_BR01_water_temperature)
    
    


if __name__ == "__main__":
    main()