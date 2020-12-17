Found intents: 'contact_sales', 'ask_which_events', 'ask_question_in_forum', 'why_rasa', 'how_to_get_started', 'ask_how_contribute'
Found entity types: 'product', 'current_api'


venv/lib/python3.8/site-packages/rasa/shared/utils/io.py:93: UserWarning: Intent 'ask_question_in_forum' has only 1 training examples! Minimum is 2, training may fail.

venv/lib/python3.8/site-packages/rasa/shared/utils/io.py:93: UserWarning: Entity entity 'current_api' has only 1 training examples! The minimum is 2, because of this the training may fail.

venv/lib/python3.8/site-packages/rasa/shared/utils/io.py:93: UserWarning: Entity entity 'product' has only 1 training examples! The minimum is 2, because of this the training may fail.


ActionNotFoundException: Cannot access action 'utter_why_rasa', as that name is not a registered action for this domain. Available actions are:
	 - action_listen
	 - action_restart
	 - action_session_start
	 - action_default_fallback
	 - action_deactivate_loop
	 - action_revert_fallback_events
	 - action_default_ask_affirmation
	 - action_default_ask_rephrase
	 - action_two_stage_fallback
	 - action_back
     
export RASA_VERSION=2.1.3	 
Rasa Interactive Shell using docker
docker run -v $(pwd):/app rasa/rasa:${RASA_VERSION} run actions --actions actions.actions
docker-compose up app -d
docker run -it -v $(pwd):/app rasa/rasa:${RASA_VERSION} shell --debug



Run rasa server with action server in docker