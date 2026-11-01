from fastapi import FastAPI
from herb_data import herb_spice_details
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Aaron - your FastAPI is running!"}

    #

herb_spice_synonyms = {
    "Kaffir Lime": "Makrut Lime",
    "Black Seed": "Black Cumin",
    "Pimenta Dioica": "Allspice",
    "Ramp": "Wild Onion",
    "Mentha Spicata": "Spearmint",
    "Mentha Arvensis": "Wild Mint",
    "Mentha Canadensis": "Horsemint",
    "California Laurel": "California Bay",
    "Sweet Flag": "Loveroot",
    "Curcuma Zedoaria": "Zedoary",
    "Curcuma Longa": "Turmeric",
    "Wasabia Japonica": "Wasabi"
},

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
        canonical_name = herb_spice_synonyms[normalized]
        return {
            "item": canonical_name,
            "details": herb_spice_details[canonical_name]
        }
        # find the herb/spice
    for key in herb_spice_details:
        if key.lower() == normalized:
            return {
                "item": key,
                "details": herb_spice_details[key]
            }
        # if not found
    return {
        "error": f"'{name}' not found in the herbs and spices list."
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
