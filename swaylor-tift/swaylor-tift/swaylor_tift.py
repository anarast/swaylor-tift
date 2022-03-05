import math
import logging

from client import create_client
from generate_unconditional_samples import sample_model

logger = logging.getLogger()

def main():
  client = create_client()
  raw_lyrics = generate_lyrics()
  parsed_lyrics = parse_lyrics(raw_lyrics)
  send_tweet(parsed_lyrics, client)
  
def generate_lyrics():
  return sample_model(model_name='lyric', nsamples=1, length=100)

def parse_lyrics(raw_lyrics: str):
  lyric_array = raw_lyrics.split("\n")
  start_index = math.floor(len(lyric_array) / 2)
  end_index = start_index + 6
  
  parsed_array = []
  
  for x in range(0, len(lyric_array) - 2):
    if lyric_array[x] != '':
      parsed_array.append(lyric_array[x])
  
  return '\n'.join(parsed_array)

def send_tweet(tweet_body: str, client):
  print(f"Creating tweet: {tweet_body}")
  try:
    client.create_tweet(text=tweet_body)
  except Exception as e:
    logger.error(f"Error sending tweet: {e}")

if __name__ == '__main__':
  main()