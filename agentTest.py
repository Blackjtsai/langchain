from langchain.tools import BaseTool
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
import os
os.environ["OPENAI_API_KEY"] = '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'

# 搜索工具
class SearchTool(BaseTool):
    name = "Search"
    description = "如果我想知道天气，'鸡你太美'这两个问题时，请使用它"
    return_direct = True  # 直接返回结果

    def _run(self, query: str) -> str:
        print("\nSearchTool query: " + query)
        return "这个是一个通用的返回"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("暂时不支持异步")

# 计算工具
class CalculatorTool(BaseTool):
    name = "Calculator"
    description = "如果是关于数学计算的问题，请使用它"

    def _run(self, query: str) -> str:
        print("\nCalculatorTool query: " + query)
        return "3"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("暂时不支持异步")

llm = OpenAI(temperature=0)
tools = [SearchTool(), CalculatorTool()]
agent = initialize_agent(
    tools, llm, agent="zero-shot-react-description", verbose=True)

question = "2*8是多少?"
print("问题："+ question)
print("答案：" + agent.run('"'+question+'"'))

question = "查询这周天气?"
print("问题："+ question)
print("答案：" + agent.run('"'+question+'"'))

question = "告诉我'鸡你太美'是什么意思?"
print("问题："+ question)
print("答案：" + agent.run('"'+question+'"'))

question = "告诉我'hello world'是什么意思"
print("问题："+ question)
print("答案：" + agent.run('"'+question+'"'))
