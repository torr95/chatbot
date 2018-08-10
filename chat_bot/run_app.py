from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-415320575926-413762546340-413291736448-c3edaad28324b25242195ea870f9b2c2', #app verification token
							'xoxb-415320575926-413291741184-WNyHI4jWwRBNga3Xk05kr9RB', # bot verification token
							'gy24kM5GAxnJJcTHJUwnE0IX', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
