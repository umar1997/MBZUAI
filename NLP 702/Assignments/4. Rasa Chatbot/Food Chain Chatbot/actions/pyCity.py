import difflib
import pandas as pd


def isRealCity(city_name, df):
    lowerCityList = set(list(df['lowerCity']))
    city_name = city_name.lower()
    
    closestNames = difflib.get_close_matches(city_name, lowerCityList, n=3)
    isSame = False
    for cn in closestNames:
        if cn == city_name:
            isSame = True
    
    return isSame, closestNames

def isRealRest(rest_name, df):
    lowerRestList = set(list(df['lowerNames']))
    rest_name = rest_name.lower()
    
    closestNames = difflib.get_close_matches(rest_name, lowerRestList, n=3)
    isSame = False
    for cn in closestNames:
        if cn == rest_name:
            isSame = True
    
    return isSame, closestNames

def getCityRecommendations(city_name, df):
    temp = df.loc[df['lowerCity'] == city_name]
    return list(set(temp['lowerNames']))


def getCityCuisines(city_name, df):
    temp = df.loc[df['lowerCity'] == city_name]
    categories = list(temp['cleanCategories'])
    allCategories = []
    for cat in categories:
        allCategories += eval(cat)
    return list(set(allCategories))


def getRestaurantInfo(city_name, restaurant_name, df):
    temp = df.loc[(df['lowerCity'] == city_name) &((df['lowerNames'] == restaurant_name))]
    temp = temp.reset_index()
    temp = temp.loc[0]
    s = temp['name'] + "\nAddress: " + temp['address'] + "\nWebsite: " + temp["websites"]
        # print(s)
    return s

def getRestaurantCuisines(city_name, restaurant_name, df):
    temp = df.loc[(df['lowerCity'] == city_name) &((df['lowerNames'] == restaurant_name))]
    temp = temp.reset_index()
    temp = temp.loc[0]
    s = temp['name'] + "\n" + temp['categories']
    # print(s)
    return s