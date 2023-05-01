from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import load_tools

import os
os.environ["OPENAI_API_KEY"] = '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'
os.environ["SERPAPI_API_KEY"] = 'fd5b9cb6c89dcb45cc70ac8ff60ed759af5db8d8eedde7219bf8ba7ccb55f494'


# 加载 OpenAI 模型
llm = OpenAI(temperature=0, max_tokens=2048)

# 加载 serpapi 工具
tools = load_tools(["serpapi"])

# 如果搜索完想在计算一下可以这么写
# tools = load_tools(['serpapi', 'llm-math'])

# 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
# tools=load_tools(["serpapi","python_repl"])

# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
agent.run(
    "今天日期？當天歷史上有什麼重要的事情？ ")
