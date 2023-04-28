import pandas as pd

# Create new csv with stratified samples 
def stratified_random_sample(path):
    
    # read csv
    dashboard_df = pd.read_csv(path, sep=',', index_col=False, dtype='unicode')
    
    # filter for minute long clips 
    dashboard_df['Duration'] = pd.to_numeric(dashboard_df['Duration'], errors='coerce')
    dashboard_df = dashboard_df[dashboard_df["Duration"] > 60]
    
    # filter for audiomoths containg enough clips (i.e. > 2000) (29 Successful Audiomoths)
    df_group = dashboard_df.groupby("AudioMothCode").filter(lambda df: df['FileName'].count() > 2000)
    
    # extract hour mark from Comment column 
    def extract_hour(time):
        return int(time.split('at ')[1].split(':')[0])
    
    # apply extract_hour (24 hour clips)
    dashboard_df_hour= df_group.assign(Hour = df_group['Comment'].apply(extract_hour))
    
    # sample one clip from each strata group (ex. strata audiomoth AM-1 in Hour 0)
    df_csv = dashboard_df_hour.groupby(['AudioMothCode','Hour']).sample(n=1)
    
    df_csv.to_csv('stratified_random_sample.csv', sep=',')
    
    # check if csv has (29 Successful Audiomoths) * (24 clips)
    if (df_csv.shape[0] == len(df_groups.index.values) * 24):
        return True 
    else:
        return False
    
    