import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from my_keys import openapi_key, GOOGLE_CSE_ID, GOOGLE_API_KEY


from langchain.agents import AgentType, initialize_agent, load_tools


os.environ['OPENAI_API_KEY'] = openapi_key
os.environ['GOOGLE_CSE_ID'] = GOOGLE_CSE_ID
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

tools = load_tools((["wikipedia", "llm-math"]), llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

result = agent.run("when was elon musk born")
print(result)


from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool

search = GoogleSearchAPIWrapper()

search_tool = Tool(
    name="I'm feeling lucky",
    description="Search Google for recent results.",
    func=search.run,
)

print(search_tool.run("where was obama born"))