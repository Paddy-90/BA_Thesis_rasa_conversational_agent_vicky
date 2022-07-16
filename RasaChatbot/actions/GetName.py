##########################################################################################
        # Namehandling
##########################################################################################
from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import UserUtteranceReverted, FollowupAction, AllSlotsReset, Restarted
from fuzzywuzzy import process
from datetime import datetime

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_1_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""
        #print("begin",caughtLearningStyles, caughtLearningStyles_talk, dialogLearningStyles, game_learningstyle_list)

        name = slot_value
        if name is not None and len(name) > 0:
            dispatcher.utter_message(response='utter_greet/N')
            return {"1_first_name": slot_value}
        else:
            dispatcher.utter_message(response='utter_greet/N')
            return {"1_first_name": "name"}
