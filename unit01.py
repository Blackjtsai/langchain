from langchain.llms import OpenAI

import os
os.environ["OPENAI_API_KEY"] = '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'

llm = OpenAI(model_name="text-davinci-003", max_tokens=100)
# llm = OpenAI(model_name="ada", max_tokens=100)
print(llm("怎么评价人工智能"))
