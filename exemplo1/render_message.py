from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))


def addheart(text):
    return f"😁 {text} 😁"


env.filters["addheart"] = addheart

template = env.get_template("email.template.txt")

data = { 
    "name": "Vinicius",
    "products": [
        {"name": "plastation 5", "price": "3440.90"},
        {"name": "range rover", "price": "344000.99"},
        {"name": "macbook", "price": "10000.00"},
    ],
    "special_customer": True
    }
print(template.render(**data))
