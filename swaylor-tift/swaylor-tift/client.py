import os
import logging
import tweepy

from dotenv import load_dotenv

logger = logging.getLogger()

def create_client():
  load_dotenv()

  try:
    client = tweepy.Client(
      consumer_key=os.getenv("CONSUMER_KEY"),
      consumer_secret=os.getenv("CONSUMER_SECRET"),
      access_token=os.getenv("ACCESS_TOKEN"),
      access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )
  except Exception as e:
    logger.error("Error creating client", exc_info=True)
    raise e
    
  logger.info("client created")
  
  return client