from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import UserUtteranceReverted, FollowupAction, AllSlotsReset, Restarted
from fuzzywuzzy import process
from datetime import datetime
##########################################################################################
# User will interrupt the chat 
##########################################################################################

class askedBot(Action):
    def name(self) -> Text:
        return "action_asked_bot"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response='utter_iamabot')
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]


class YourResidence(Action):
    def name(self) -> Text:
        return "action_your_residence"

    def run(self, dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response='utter_residence')
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]


class Learningstyle(Action):
    def name(self) -> Text:
        return "action_learningstyle"

    def run(self, dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response='utter_learningstyle')
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]


class Killerphrases(Action):
    def name(self) -> Text:
        return "action_killerphrases"

    def run(self, dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response='utter_killerphrases')
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]


class ActionOutOfScoop(Action):
    def name(self) -> Text:
        return "action_out_of_scope"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response='utter_out_of_scope')
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]

class ActionNegation(Action):
    def name(self) -> Text:
        return "action_negation"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response='utter_negation')
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]

class ActionTime(Action):
    def name(self) -> Text:
        return "action_time"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dispatcher.utter_message(text='The current time is ' + current_time)
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]


class ActionAnswerBot(Action):
    def name(self) -> Text:
        return "action_answer_bot"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response='utter_answer_bot')
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]


class ActionChitChat(Action):
    def name(self) -> Text:
        return "action_chitchat"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        lastintent = tracker.latest_message['intent'].get('name')
        #if(lastintent == '')
        dispatcher.utter_message(response='utter_' + lastintent)
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]


class ActionRepeatLastQuest(Action):
    def name(self) -> Text:
        return "action_repeat_last_quest"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        getSlotValue = ""
        utter_action = ""
        last_question = ""
        for event in tracker.events:
            if event['event'] == 'slot':
                if event['name'] == 'requested_slot':
                    getSlotValue = event['value']
            if event['event'] == 'bot':
                utter_action = event['metadata'].get('utter_action')
                if utter_action == 'utter_greet/N':
                    last_question = 'utter_greet/N'
                elif utter_action == 'utter_greet/NN':
                    last_question = 'utter_greet/NN'
                elif utter_action == 'utter_how_you_are_doing/g':
                    last_question = 'utter_how_you_are_doing/request'
                elif utter_action == 'utter_how_you_are_doing/b':
                    last_question = 'utter_how_you_are_doing/request'
                elif utter_action == 'utter_how_you_are_doing/n':
                    last_question = 'utter_how_you_are_doing/request'
                if utter_action == 'utter_activity':
                    last_question = 'utter_activity'
                elif utter_action == 'utter_learning_style_recommendation_talk':
                    last_question = 'utter_learning_style_recommendation_talk'
                elif utter_action == 'utter_confirm_start_game':
                    last_question = 'utter_confirm_start_game'
                elif utter_action == 'utter_learning_style_recommendation_game':
                    last_question = 'utter_learning_style_recommendation_game'
                else:
                    last_question == 'utter_no_repeat'
        if getSlotValue is not None:
            if getSlotValue[0] == '2':
                dispatcher.utter_message(response='utter_ask_' + getSlotValue)
            else:
                dispatcher.utter_message(
                    response='utter_ask_' + getSlotValue + '/request')
        else:
            dispatcher.utter_message(response=last_question)
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]

class ActionRephraseLearningStyle(Action):
    def name(self) -> Text:
        return "action_rephrase_learningstyle"

    def run(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        utter_action = ""
        rephrase = ""
        for event in tracker.events:
            if event['event'] == 'bot':
                utter_action = event['metadata'].get('utter_action')
                if utter_action == 'utter_learningstyle':
                    rephrase= "You take in and process information in different ways. A learning style is a method you use to learn. You can use recognition of their individual learning styles to find what study methods, environment, and activities help you to learn best."
                else:
                    rephase = "I'm sorry! That´s not possible at the moment. Therefore I need more trainingsdata."

        dispatcher.utter_message(text=rephrase)
        return [UserUtteranceReverted(), FollowupAction(tracker.active_form.get('latest_action_name'))]