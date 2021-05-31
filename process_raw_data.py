
import glob
import pandas as pd

def readRawDataFiles():
    all_files = glob.glob("raw_data/*")
    iowa_data_df = pd.DataFrame()
    for file_num,eachfile in enumerate(all_files): 
        iowa_data_df = iowa_data_df.append( pd.read_csv(eachfile,low_memory=False))
        print(f"Finished appending {file_num+1} files")
    print(iowa_data_df.head(5))

def main():
    # Read in the csv files from raw data directory
    readRawDataFiles()


if __name__ == "__main__":
    main()