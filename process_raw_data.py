
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
        iowa_data_df.to_csv("raw_data/iowa.csv")

def readWholeIowaData():
    return pd.read_csv("raw_data/iowa.csv",low_memory=False)

def main():
    # Read in the csv files from raw data directory
    readRawDataFiles()
    
    iowa_data_df = readWholeIowaData()
    
    print("\n".join(list(iowa_data_df.name.value_counts())))


if __name__ == "__main__":
    main()