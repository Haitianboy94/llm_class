tools = [
    {
        "type": "function",
        "function": {
            "name": "get_product_info",
            "description": "Get information about a specific product by its name, including price, category, stock, and description.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the product, for example 'iPhone 15'."
                    }
                },
                "required": ["name"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_products_by_category",
            "description": "Get all products belonging to a specific category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Product category, such as Electronics, Computers, Audio, Gaming, or Accessories."
                    }
                },
                "required": ["category"],
                "additionalProperties": False
            }
        }
    },
    # {
    #     "type": "function",
    #     "function": {
    #         "name": "get_products_by_budget",
    #         "description": "Find products that cost less than or equal to the user's maximum budget.",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "max_price": {
    #                     "type": "number",
    #                     "description": "Maximum amount the user wants to spend in euros."
    #                 }
    #             },
    #             "required": ["max_price"],
    #             "additionalProperties": False
    #         }
    #     }
    # },
    # {
    #     "type": "function",
    #     "function": {
    #         "name": "check_stock",
    #         "description": "Check whether a specific product is available and return its stock quantity.",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "product_name": {
    #                     "type": "string",
    #                     "description": "Name of the product to check."
    #                 }
    #             },
    #             "required": ["product_name"],
    #             "additionalProperties": False
    #         }
    #     }
    # },
    # {
    #     "type": "function",
    #     "function": {
    #         "name": "calculate_total",
    #         "description": "Calculate the total price of multiple products using their IDs.",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "product_ids": {
    #                     "type": "array",
    #                     "items": {
    #                         "type": "integer"
    #                     },
    #                     "description": "List of product IDs to include in the total."
    #                 }
    #             },
    #             "required": ["product_ids"],
    #             "additionalProperties": False
    #         }
    #     }
    # }
]