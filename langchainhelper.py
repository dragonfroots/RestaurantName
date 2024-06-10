import os
from my_keys import openapi_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

def generate_restaurant_name_and_items(cuisine):

    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="i want to open a restaurant for {cuisine} food.  suggest a restaurant name."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="suggest menu items for {restaurant_name}. return it as a comma separated list"
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response

if __name__ == '__main__':
    print(generate_restaurant_name_and_items('Italian'))
