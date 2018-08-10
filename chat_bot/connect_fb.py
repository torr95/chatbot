access_token="EAAgcdB0uer0BAGtvYoJCytIwOP7ecohZCvfoP0rXSWQHCvtRFGQktnLJkQYwD1ImMgcvwBCgBvVeVgqdPRLVTHeTmZBpxyV4hFn1GY1kkwSLcSDqOUAMSgpyX41VQ9jZBYYztTZAEjI1tQeZCSq22rBDi8PcgX22MfKdYsSqNAAZDZD"
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter

# load your trained agent
agent = Agent.load("dialogue", interpreter=RegexInterpreter())

input_channel = FacebookInput(
   fb_verify="YOUR_FB_VERIFY",  # you need tell facebook this token, to confirm your URL
   fb_secret="YOUR_FB_SECRET",  # your app secret
   fb_access_token=access_token   # token for the page you subscribed to
)

agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))
