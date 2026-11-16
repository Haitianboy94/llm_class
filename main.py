from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from product import products
from tool import tools


load_dotenv()
api_key = os.getenv("OLLAMA_API")
base_url = os.getenv("OLLAMA_END_POINT")
model_name = os.getenv("MODEL_NAME")

if not all([api_key, base_url, model_name]):
    raise ValueError("Missing one of your keys")
print("ready to go")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)


def get_product_info(name: str) -> dict:
    for product in products:
        if product["name"].lower() == name.lower():
            return product
    return {"error": f"Product '{name}' not found"}


def get_products_by_category(category: str) -> list[dict]:
    results = []

    for product in products:
        if product["category"].lower() == category.lower():
            results.append(product)
    return results


user_input = input("Ask your question: ")
message = [{
        "role": "system",
        "content": "You're a product assistant working in a phoneshop"
        "always use the available tool to look up current product"
        "information, if the user just say hello, answer with a nice message"
        "and ask how can you help"
        },
    {
        "role": "user",
        "content": user_input
    }
]

response = client.chat.completions.create(
    model=model_name,
    messages=message,
    tools=tools,
    tool_choice="auto",
    temperature=0.2
)

response_message = response.choices[0].message

if response_message.tool_calls:
    message.append(response_message)

    tool_call = response_message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    if function_name == "get_product_info":
        result = get_product_info(**arguments)

    elif function_name == "get_products_by_category":
        result = get_products_by_category(**arguments)

    else:
        result = {"error": f"Unknown function: {function_name}"}

    message.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result)
    })

    final_message = client.chat.completions.create(
        model=model_name,
        messages=message,
        tools=tools,
        temperature=0.2
    )
    print(final_message.choices[0].message.content)
else:
    raise ValueError("Nothing found")