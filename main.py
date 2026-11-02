from sqlmodel import Session, select
from database import engine, HerbSpice

from fastapi import FastAPI
from herb_data import herb_spice_details
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Aaron - your FastAPI is running!"}


herb_spice_synonyms = {
    "kaffir lime": "Makrut Lime",
    "black seed": "Black Cumin",
    "pimenta dioica": "Allspice",
    "ramp": "Wild Onion",
    "mentha spicata": "Spearmint",
    "mentha arvensis": "Wild Mint",
    "mentha canadensis": "Horsemint",
    "california laurel": "California Bay",
    "sweet flag": "Loveroot",
    "curcuma zedoaria": "Zedoary",
    "curcuma longa": "Turmeric",
    "wasabia japonica": "Wasabi"
}


    #define list once outside the function
herbs_and_spices = list(herb_spice_details.keys())
@app.get("/herbs-and-spices")
def get_herbs_and_spices():
    herbs_and_spices = [
        "Allspice",
        "Angelica",
        "Anise",
        "Annatto",
        "Black Cumin",
        "Black Pepper",
        "Brown Mustard",
        "Caraway",
        "Cardamom",
        "Cayenne Pepper",
        "Celery Seed",
        "Coriander",
        "Cumin",
        "Dill",
        "Fennel",
        "Fenugreek",
        "Juniper Berries",
        "Lovage",
        "Mace",
        "Mustard",
        "Myrtle",
        "Nutmeg",
        "Paprika",
        "Pepper",
        "Pimento",
        "Sichuan Pepper",
        "Star Anise",
        "Tabasco Pepper",
        "Tamarind",
        "Vanilla",
        "White Mustard",
        "White Pepper",
        "Absinthe",
        "Balm",
        "Basil",
        "Bay Leaf",
        "Buchu",
        "Capers",
        "Celery",
        "Cinnamon",
        "Chamomile",
        "Chinese Keys",
        "Cloves",
        "Curry Leaf",
        "Field Mint",
        "French Tarragon",
        "Garden Nasturtium",
        "Ginger",
        "Hops",
        "Horseradish",
        "Hyssop",
        "Lemon Verbena",
        "Lemongrass",
        "Licorice",
        "Makrut Lime",
        "Mint",
        "Oregano",
        "Peppermint",
        "Rue",
        "Saffron",
        "Spearmint",
        "Turmeric",
        "Wasabi",
        "Wormwood",
        "Zedoary",
        "Wild Mint",
        "Horsemint",
        "Loveroot",
        "California Bay",
        "Sagebrush",
        "Juniper",
        "Wild Onion"
    ]
    return {"items": herbs_and_spices}
@app.get("/herbs-and-spices/{name}")
def get_herbs_and_spices(name: str):
        # normalize input for matching

    normalized = name.lower()

    if normalized in herb_spice_synonyms:
        name = herb_spice_synonyms[normalized]
    with Session(engine) as session:
       statement = select(HerbSpice)
       herbs = session.exec(statement).all()

       for herb in herbs:
           if herb.name.lower() == name.lower():
               return {
                   "item": herb.name,
                   "flavor_profile": herb.flavor_profile,
                   "cuisine": herb.cuisine,
                   "pairings": herb.pairings
               }
    return {
        "error": f"'{name}' not found in the herbs and spices database."
    }

@app.get("/cuisines/{cuisine}")
def get_cuisine_items(cuisine: str):
    normalized = cuisine.lower()
    results = []

    for herb, details in herb_spice_details.items():
        # each herb has a list of cuisines
        for c in details["cuisine"]:
            if c.lower() == normalized:
                results.append(herb)

    if results:
        return {"cuisine": cuisine, "herbs_and_spices": results}
    return {"cuisine": cuisine, "herbs_and_spices": [],
            "message": f"No Herbs or spices found for cuisine '{cuisine}'."}
