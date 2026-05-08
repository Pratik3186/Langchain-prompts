from langchain_core.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatOpenAI()

template2 = PromptTemplate(
    template = 'Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

prompt = template2.invoke({'name':'nitish'})

result = model.invoke(prompt)

print(result.invoke)


