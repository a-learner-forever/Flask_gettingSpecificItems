from flask import Flask, request

app = Flask(__name__)
stores=[{"name":"MyStore","items":[
    {
        "name":"chair7",
        "price":1205
    },
    {
        "name":"table",
        "price":400
    }
]
}
]

@app.get("/store")
def get_stores():
    return{"stores":stores}

@app.post("/store")
def create_store():
    request_data=request.get_json()
    new_store={"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201


@app.post("/store/<string:name>/items")
def create_item(name):
    request_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item={"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item,201
    return{"message":"store not found"}, 404


@app.get("/store/<string:name>/items")
def get_item_in_store(name):
    for store in stores:
        if store["name"]==name:
            return{"items":store["items"]}
    return{"message":"Store not found"},404
