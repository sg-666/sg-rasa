class ChatForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "chat_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name", "conversation", "insurancetype", "healthvisatype",
                "age", "yorn", "preference", "result"]
'''
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        name = tracker.get_slot('name')
        conversation = tracker.get_slot('conversation')
        insurancetype = tracker.get_slot('insurancetype')
        healthvisatype = tracker.get_slot('healthvisatype')
        age = tracker.get_slot('age')
        yorn = tracker.get_slot('yorn')
        preference = tracker.get_slot('preference')
        result = tracker.get_slot('result')

        return []
'''
'''
slots:
   name:

     type: text
     influence_conversation: true
   conversation:
     type: categorical
     values:
       - looking_for_insurance
       - arrange_call_back
     influence_conversation: true
   insurancetype:
     type: categorical
     values:
         - senior_health_insurance
         - senior_life_insurance
     influence_conversation: true
   healthvisatype:
     type: categorical
     values:
         - 600
         - 601
         - aus_pr
         - other
     influence_conversation: true
   lifevisatype:
     type: categorical
     values:
         - accidential only
         - natural only
         - full cover
     influence_conversation: true
   age:
     type: float
     min_value: 0.0
     max_value: 130.0
   yorn:
     type: categorical
     values:
         - yes
         - no
     influence_conversation: true
   description:
     type: text
     influence_conversation: true
   preference:
     type: text
     values:
         - not_sure_yet
         - hospital_cover
         - dental
         - best_price
     # influence_conversation: true (demo will not change the result according to choice)
   result:
     type: text
     influence_conversation: true
'''