import pandas
import requests


# Loads URLs into a Pandas Dataframe

dataframe= pandas.read_csv('urls.csv')
counter = 0
for url in dataframe['urls']:

    try:

        response = requests.get(url, allow_redirects=False)

        status = response.status_code
        
    except: 
        
        status = "0"
        

    dataframe.at[counter, 'Status'] = status

    

    counter = counter + 1

dataframe['Status'] = dataframe['Status'].astype(int)

# Prints out terminal


print(dataframe)

#Saves in CSV

dataframe.to_csv('Statuscodes.csv')

    
