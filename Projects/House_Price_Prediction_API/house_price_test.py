import requests
import json

url = 'http://127.0.0.1:5000'

#create function function for posting data and getting result
def get_prediction(data):
    
    #post data
    response = requests.post(f'{url}/predict',json = data)

    #get results from API
    print('Prediction : ',response.json()['prediction'])

if __name__ == '__main__':

    # basic interface data collection and posting
    print('Enter Info :')
    bedrooms = int(input("Enter No of Bedrooms : "))
    bathrooms = int(input('Enter No of Bathrooms : '))
    sqft_liv = int(input('SQFT living : '))
    age_of_house = int(input('age of house : '))

    # create dictionary
    data = {'bedrooms' :bedrooms,'bathrooms': bathrooms,'sqft_living':sqft_liv,'age_of_house':age_of_house}
   
    #calling function
    get_prediction(data)
