from slackclient import SlackClient

import os

def lambda_handler(event, context):

  print(event)
  print(context)

  slack_token = os.environ['SLACKTOKEN']

  sc = SlackClient(slack_token)

  sc.api_call(
  "chat.postMessage",
  channel="general",
  text="New EC2 is running! :rocket:"
  )

  return 'Post to Slack complete';