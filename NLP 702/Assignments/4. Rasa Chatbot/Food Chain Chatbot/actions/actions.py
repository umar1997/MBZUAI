# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction

import pandas as pd
from actions.pyCity import isRealCity, isRealRest
from actions.pyCity import getCityCuisines, getCityRecommendations,  getRestaurantInfo, getRestaurantCuisines

#####################################################################
df = pd.read_csv('./data/FastFoodCleaned.csv')

#####################################################################


def printList(listOptions):
    x = ' \n'.join([str(i+1) + '. ' + v for i, v in enumerate(listOptions)])
    return x

class ActionGetCity(Action):

    def name(self) -> Text:
        return "action_get_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        user_city_text = tracker.latest_message.get("text")
        ent = tracker.latest_message["entities"][0]['entity']
        if ent == 'cities':
            user_city_ent = tracker.latest_message["entities"][0]['value']
        else:
            print('Why is the Entity a {} here?'.format(ent))

        isSame, closestNames = isRealCity(user_city_ent, df)
        if user_city_ent==closestNames[0]:
            dispatcher.utter_message(text=f"You chose {user_city_ent}")
            recommendations = getCityRecommendations(user_city_ent, df)
            recommendations = printList(recommendations)
            dispatcher.utter_message(text=f"Restaurants recommendations in your city are \n{recommendations}\nPlease type in correct spellings!")
            return [SlotSet("cities", [user_city_ent] )]
        else:
            closestNames = printList(closestNames)
            dispatcher.utter_message(text=f"{closestNames}\n")
            return [FollowupAction('utter_askcorrectcity')]

        return []


class ActionGetRestaurant(Action):
    
    def name(self) -> Text:
        return "action_get_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city_not_given = False
        try:
            user_city = tracker.get_slot("cities")[0]
        except:
           city_not_given = True 

        if city_not_given:
            dispatcher.utter_message(text=f"For that we will first need some information.")
            return [FollowupAction('utter_requestcity')]
            
        else:
            restaurantRecommendations = getCityRecommendations(user_city, df)
            recommendations = printList(restaurantRecommendations)
            dispatcher.utter_message(text=f"Restaurants recommendations in your city are \n{recommendations}\nPlease type in correct spellings!")
        

        return []


class ActionChooseRestaurant(Action):
    
    def name(self) -> Text:
        return "action_choose_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city_not_given = False
        try:
            user_city = tracker.get_slot("cities")[0]
        except:
           city_not_given = True 

        if city_not_given:
            dispatcher.utter_message(text=f"For that we will first need some information.")
            return [FollowupAction('utter_requestcity')]        
        else:
            user_rest = tracker.get_slot("restaurant")
            user_rest_text = tracker.latest_message.get("text")
            
            isSame, closestNames = isRealRest(user_rest_text, df)
            if isSame:
                dispatcher.utter_message(text=f"Your have chosen {user_rest_text}")
                dispatcher.utter_message(text=f"Would you like to check out the restaurant's cuisines? or the restaurant's information?")
                return [SlotSet("restaurant", [user_rest_text])]
            else:
                dispatcher.utter_message(text=f"Sorry that is not a name of a restaurant!")
                return [FollowupAction('utter_goodbye')]
        return []

class ActionGetInfo(Action):
    
    def name(self) -> Text:
        return "action_get_restaurant_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city_not_given = False
        rest_not_given = False
        try:
            user_city = tracker.get_slot("cities")[0]
        except:
           city_not_given = True 

        if city_not_given:
            dispatcher.utter_message(text=f"For that we will first need some information.")
            return [FollowupAction('utter_requestcity')]  
        else:
            try:
                user_rest= tracker.get_slot("restaurant")[0]
            except:
                rest_not_given = True 
            
            if rest_not_given:
                return [FollowupAction('action_get_restaurant')]
            else:
                s = getRestaurantInfo(user_city, user_rest, df)
                dispatcher.utter_message(text=f"{s}")
           
        return []


class ActionGetCuisine(Action):
    
    def name(self) -> Text:
        return "action_get_restaurant_cuisine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city_not_given = False
        rest_not_given = False
        try:
            user_city = tracker.get_slot("cities")[0]
        except:
           city_not_given = True 

        if city_not_given:
            dispatcher.utter_message(text=f"For that we will first need some information.")
            return [FollowupAction('utter_requestcity')]  
        else:
            try:
                user_rest= tracker.get_slot("restaurant")[0]
            except:
                rest_not_given = True 
            
            if rest_not_given:
                return [FollowupAction('action_get_restaurant')]
            else:
                s = getRestaurantCuisines(user_city, user_rest, df)
                dispatcher.utter_message(text=f"{s}")
           
        return []
