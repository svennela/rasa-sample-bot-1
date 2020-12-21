# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import requests
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionWelcome(Action):
  def name(self):
    return "action_greeting"

  def run(self, dispatcher, tracker, domain):
    print ("--- action_greeting ----")  
    dispatcher.utter_message(template="action_greeting")
    return []


class ActionJoke(Action):
  def name(self):
    return "action_joke"

  def run(self, dispatcher, tracker, domain):
    request = requests.get('http://api.icndb.com/jokes/random').json()  # make an api call
    print ("----------------------action joke-----------")
    print (request)
    joke = request['value']['joke']  # extract a joke from returned json response
    dispatcher.utter_message(joke)  # send the message back to the user
    return [] 
    ## "Chuck Norris does not teabag the ladies. He potato-sacks them."
    #return static_joke  

class ActionFacilitySearch(Action):
    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        facility = tracker.get_slot("facility_type")
        address = "3000 Hydes, St, Delhi !!!!"
        dispatcher.utter_message(text = "Here is the address of the {}:{}".format(facility,address))

        return [SlotSet("address",address)]    