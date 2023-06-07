import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my  boss for resignation",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nSubject Line: Resignation from position of [Position]\n\nDear [Boss Name],\n\nThis letter is to inform you of my intention to resign from my position as [Position] with [Company], effective [date].\n\nI have appreciated my time here and the support I have received during my tenure. It has been a great experience working for [Company], and I am thankful for the opportunity to contribute to the company\u2019s success.\n\nI am available to assist with any training needs or transition of tasks during this period if needed.\n\nI wish you all the best in the future.\n\nSincerely,\nName"
    }
  ],
  "created": 1686093730,
  "id": "cmpl-7OaI61VejiDLJCwSi15aru4HHBmCz",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 135,
    "prompt_tokens": 9,
    "total_tokens": 144
  }
}
'''