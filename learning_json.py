import json

simple_dict= {
    "Amount": 3000,
    "Category": "Food",
    "Description" : "Dinner"
}
with open("expenses.json","w") as file:
    json.dump(simple_dict,file)
with open("expenses.json","r") as output:
    print(json.load(output))