from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Aaron - your FastAPI is running!"}

    # details dictionary for herbs and spices
herb_spice_details = {
    "Allspice": {
        "flavor-profile": "combination of sweet, warm, woody, mild pepper, mildly sweet, notes of cinnamon",
        "cuisine": ["Jamaican", "Middle Eastern / Arab", "North American",
                     "Mexican", "Polish", "Portuguese", "Swedish",
                     "British"],
        "pairings": ["mace", "cardamom", "ginger", "bay leaves", "black pepper",
                     "cumin", "coriander", "garlic", "thyme", "rosemary",
                     "star anise"]
    },
    "Angelica": {
        "flavor-profile": "herbal, notes of carrot, notes of celery, moderately bitter, warm, subtle spice",
        "cuisine": ["Scandinavian", "Sámi", "French", "European"],
        "pairings": ["fish", "soups", "poultry", "stew", "rhubarb tarts", "apple",
                     "orange", "citrus", "mint", "dill", "tarragon",
                     "gin", "vermouth", "absinthe", "Chartreuse Liqueur",
                     "Bénédictine Liqueur"]
    },
    "Anise": {
        "flavor-profile": "sweet, aromatic, strong notes of black licorice",
        "cuisine": ["Italian", "French", "German", "Austrian", "Greek",
                     "Chinese", "Vietnamese", "Indonesian", "Malaysian",
                     "Indian", "Pakistani","Middle Eastern", "North African",
                     "Mexican"],
        "pairings": ["citrus", "tree fruits", "berries", "honey", "vanilla",
                     "goat cheese", "caramel", "cinnamon", "nutmeg", "cardamom",
                     "cloves", "black pepper", "garlic", "ginger", "cumin", "mint",
                     "basil", "bay leaves", "fennel", "tarragon"]
    },
    "Annatto": {
        "flavor-profile": "a softer version of paprika, earthy, mildly sweet, floral undertones",
        "cuisine": ["Mexican", "Mayan", "Venezuelan", "Central American",
                     "South American", "Jamaican", "Puerto Rican", "Cuban",
                     "Chamorro", "Filipino", "Vietnamese", "World Cheeses"],
        "pairings": ["Cumin", "Coriander", "Black Peppercorn", "Chili Peppers", "Cloves", "Allspice",
                     "Turmeric", "Paprika", "Ceylon Cinnamon", "Oregano", "Garlic", "Onion",
                     "Thyme", "Sage", "Bay Leaves", "Lemongrass", "Epazote", "Star Anise"]
    },
    "Black Cumin": {
        "flavor-profile": "peppery, slight bitter taste, undertones of onion, oregano, toasted nutty flavor",
        "cuisine": ["Indian", "Pakistani", "Bangladeshi", "Turkish", "Palestinian",
                     "Iranian", "North African", "Syrian", "Ethiopian",
                     "Mediterranean"],
        "pairings": ["ginger", "garlic", "shallots", "mustard seeds", "coriander",
                     "sesame seeds", "cardamom", "cinnamon", "black pepper",
                     "fenugreek", "Panch Phoron", "berbere", "adobo", "dukkah",
                     "masala"]
    },
    "Black Pepper": {
        "flavor-profile": "sharp initial bite with a mild finish, sweet, grassy, pine, citrus notes",
        "cuisine": ["Indian", "Western and American", "Italian", "Chinese",
                    "French", "Middle Eastern", "African"],
        "pairings": ["rosemary", "thyme", "basil", "oregano", "sage", "bay leaf",
                     "garlic", "onion", "cumin", "coriander", "nutmeg",
                     "mustard seed", "turmeric", "cinnamon", "cloves",
                     "star anise", "vanilla"]
    },
    "Brown Mustard": {
        "flavor-profile": "hotter than yellow mustard, tangy, acidic, bold, complex, assertive heat",
        "cuisine": ["Indian", "South Asian", "American", "French",
                    "Chinese", "European", "Eastern European", "German",
                    "Dutch"],
        "pairings": ["cinnamon", "nutmeg", "allspice", "garlic", "caraway seeds",
                     "turmeric", "cumin", "coriander"]
    },
    "Caraway": {
        "flavor-profile": "earthy, bittersweet, pungent, hints of licorice, anise, pepper, and bright citrus",
        "cuisine": ["German", "Austrian", "Hungarian", "Czech",
                    "Slovak", "Swedish", "Norwegian", "Danish",
                    "Russian", "Polish", "Baltic", "British", "Irish",
                    "Middle Eastern", "North African", "Indian"],
        "pairings": ["coriander", "fennel", "dill", "garlic", "cumin",
                     "black pepper", "paprika", "juniper berries", "parsley",
                     "thyme", "oregano", "marjoram", "chives"]
    },
    "Cardamom": {
        "flavor-profile": "floral, citrus, mint, eucalyptus, faint peppery sweetness",
        "cuisine": ["Indian", "Middle Eastern", "Scandinavian",
                    "Korean", "Swedish", "African", "Finnish",
                    "Persian"],
        "pairings": ["cinnamon", "nutmeg", "coriander", "cumin", "ginger",
                     "cloves", "vanilla", "allspice", "turmeric", "star anise",
                     "black pepper", "fennel", "caraway", "coriander", "mint",
                     "basil", "rosemary", "oregano", "thyme", "rose petal",
                     "orange blossom"]
    },
    "Cayenne Pepper": {
        "flavor-profile": "strong heat from capsaicin, very little distinct flavor",
        "cuisine": ["American", "Cajun", "Creole", "Mexican", "Tex-Mex",
                    "Indian", "South Asian", "West African", "Middle Eastern",
                    "Asian", "Caribbean"],
        "pairings": ["paprika", "cumin", "coriander", "garlic powder", "onion powder",
                     "cinnamon", "nutmeg", "oregano", "thyme", "cilantro", "parsley",
                     "bay leaf", "rosemary", "marjoram"]
    },
    "Celery Seed":{
        "flavor-profile": "a concentrated, bold version of celery stalks. Savory, earthy, slightly bitter",
        "cuisine": ["American", "Cajun", "Creole", "Indian", "Middle Eastern",
                    "Persian", "Russian", "Scandinavian"],
        "pairings": ["Mustard Seed", "Black Pepper", "Garlic Powder", "Onion Powder",
                     "Paprika", "Cumin", "Coriander", "Bay Leaves",
                     "Dill", "Parsley", "Basil", "Thyme", "Rosemary",
                     "Oregano", "Marjory"]
    },
    "Coriander": {
        "flavor-profile": "warm, nutty, notes of citrus, ginger, earthy, notes of black pepper",
        "cuisine": ["Indian", "South Asian", "Middle Eastern", "Mexican", "Latin American",
                    "Southeast Asian", "Chinese", "Thai", "Vietnamese",
                    "Mediterranean", "North African", "European"],
        "pairings": ["Cumin", "Black Pepper", "Cinnamon", "Cardamom", "Allspice",
                     "Fennel Seeds", "Caraway Seeds", "Turmeric", "Ginger", "Garlic",
                     "Fresh Cilantro", "Parsley", "Thyme", "Mint", "Basil", "Dill",
                     "Lemongrass"]
    },
    "Cumin": {
        "flavor-profile": "warm, earthy, nutty flavor, slightly smoky, faint citrus",
        "cuisine": ["Indian", "Middle Eastern", "Mediterranean", "North African",
                    "Mexican", "Tex-Mex", "Chinese", "Central Asian", "Ethiopian",
                    "Eritrean", "Latin American", "Cuban"],
        "pairings": ["Coriander", "Turmeric", "Paprika", "Allspice", "Cinnamon",
                     "Cardamom", "Cloves", "Fennel Seeds", "Mustard Seeds", "Garlic",
                     "Ginger", "Cilantro", "Coriander Leaf", "Oregano", "Thyme",
                     "Rosemary", "Mint", "Parsley", "Dill"]
    },
    "Dill": {
        "flavor-profile": "fresh, grassy, slight citrus, hint of anise, hint of licorice, herbaceous",
        "cuisine": ["Seafood", "Dips", "Soups", "Vegetables", "Gravlax", "Salmon",
                    "Grilled Fish", "Baked Fish", "Greek", "Aioli", "Salad Dressing",
                    "Eastern Europe", "Borsch", "Chicken Soup", "Persian", "Bread"],
        "pairings": ["Parsley", "Chives", "Mint", "Basil", "Tarragon",
                     "Cilantro", "Garlic", "Horseradish", "Mustard", "Mustard Seed",
                     "Caraway", "Cumin", "Paprika", "Black Pepper", "Red Pepper", "Lemon Zest"]
    },
    "Fennel": {
        "flavor_profile": "sweet, warm, and mildly licorice-like with herbal and citrus undertones",
        "cuisine": ["Italian", "Mediterranean", "Indian", "Middle Eastern"],
        "pairings": ["anise", "coriander", "cumin", "black pepper", "thyme"]
    },
    "Fenugreek": {
        "flavor_profile": "earthy, nutty, and slightly bitter with maple-like sweetness when cooked",
                  "cuisine": ["Indian", "Middle Eastern", "North African"],
                  "pairings": ["cumin", "turmeric", "coriander", "mustard seed", "cardamom"]
    },

    "Juniper Berries": {
        "flavor_profile": "piney, resinous, sharp, and slightly citrusy with peppery notes",
        "cuisine": ["Scandinavian", "German", "Central European"],
        "pairings": ["bay leaf", "rosemary", "thyme", "black pepper", "garlic"]
    },

    "Lovage": {
        "flavor_profile": "bold, celery-like, herbaceous, and slightly peppery with hints of anise",
        "cuisine": ["European", "Mediterranean"],
        "pairings": ["parsley", "celery seed", "chives", "dill", "bay leaf"]
    },

    "Mace": {
        "flavor_profile": "warm, sweet, and aromatic with a lighter, more floral version of nutmeg’s flavor",
        "cuisine": ["Indian", "Middle Eastern", "European", "Caribbean"],
        "pairings": ["nutmeg", "cinnamon", "clove", "allspice", "ginger"]
    },
    "Mustard": {
        "flavor_profile": "sharp, pungent, and slightly bitter with warm, earthy heat when ground or cooked",
        "cuisine": ["Indian", "Chinese", "French", "German", "American"],
        "pairings": ["turmeric", "coriander", "cumin", "fenugreek", "black pepper"]
    },

    "Myrtle": {
        "flavor_profile": "aromatic, resinous, and slightly sweet with hints of eucalyptus and pine",
        "cuisine": ["Mediterranean", "Middle Eastern"],
        "pairings": ["bay leaf", "rosemary", "thyme", "sage", "juniper berries"]
    },

    "Nutmeg": {
        "flavor_profile": "warm, sweet, nutty, and aromatic with subtle clove-like spice",
        "cuisine": ["Indian", "Middle Eastern", "European", "Caribbean"],
        "pairings": ["mace", "cinnamon", "clove", "allspice", "ginger"]
    },

    "Paprika": {
        "flavor_profile": "sweet, mild, or smoky depending on variety, with warm pepper notes",
        "cuisine": ["Hungarian", "Spanish", "Central European"],
        "pairings": ["garlic", "cumin", "oregano", "black pepper", "cayenne pepper"]
    },

    "Pepper": {
        "flavor_profile": "pungent, sharp, and woody with citrusy and floral undertones depending on variety",
        "cuisine": ["Global", "Indian", "Chinese", "European"],
        "pairings": ["garlic", "thyme", "rosemary", "coriander", "bay leaf"]
    },
    "Pimento": {
        "flavor_profile": "warm, sweet, and mildly peppery with hints of clove, cinnamon, and nutmeg",
        "cuisine": ["Caribbean", "Jamaican", "Latin American"],
        "pairings": ["cinnamon", "clove", "nutmeg", "ginger", "allspice"]
    },

    "Sichuan Pepper": {
        "flavor_profile": "citrusy, floral, and slightly woody with a distinctive numbing, tingling sensation",
        "cuisine": ["Chinese", "Sichuan", "Tibetan", "Nepalese"],
        "pairings": ["ginger", "garlic", "star anise", "chili pepper", "coriander"]
    },

    "Star Anise": {
        "flavor_profile": "sweet, warm, and strongly licorice-like with aromatic, spicy depth",
        "cuisine": ["Chinese", "Vietnamese", "Indian"],
        "pairings": ["cinnamon", "clove", "ginger", "Sichuan pepper", "fennel"]
    },

    "Tabasco Pepper": {
        "flavor_profile": "hot, sharp, and bright with a clean, vinegary heat when processed into sauce",
        "cuisine": ["American", "Mexican", "Cajun", "Creole"],
        "pairings": ["garlic", "cumin", "paprika", "black pepper", "oregano"]
    },

    "Tamarind": {
        "flavor_profile": "tangy, sour, fruity, and slightly sweet with citrus-like brightness",
        "cuisine": ["Indian", "Thai", "Mexican", "Caribbean", "Middle Eastern"],
        "pairings": ["cumin", "coriander", "ginger", "chili pepper", "turmeric"]
    },
    "Vanilla": {
        "flavor_profile": "sweet, creamy, floral, and warm with rich aromatic depth",
        "cuisine": ["Global", "French", "American", "Mexican"],
        "pairings": ["cinnamon", "nutmeg", "clove", "cardamom", "cocoa"]
    },

    "White Mustard": {
        "flavor_profile": "mild, slightly tangy, and earthy with gentle heat when crushed",
        "cuisine": ["Indian", "Mediterranean", "European"],
        "pairings": ["turmeric", "coriander", "cumin", "fenugreek", "black pepper"]
    },

    "White Pepper": {
        "flavor_profile": "sharp, earthy, and slightly fermented with a cleaner heat than black pepper",
        "cuisine": ["Chinese", "Thai", "French", "European"],
        "pairings": ["garlic", "ginger", "coriander", "bay leaf", "lemongrass"]
    },

    "Absinthe": {
        "flavor_profile": "strongly herbal, bitter, and anise-like with minty and floral undertones",
        "cuisine": ["French", "European"],
        "pairings": ["anise", "fennel", "mint", "wormwood", "angelica"]
    },

    "Balm": {
        "flavor_profile": "lemony, bright, and mildly minty with soft herbal sweetness",
        "cuisine": ["European", "Mediterranean"],
        "pairings": ["mint", "lemon zest", "thyme", "parsley", "chamomile"]
    },

    "Basil": {
        "flavor_profile": "sweet, aromatic, and slightly peppery with hints of clove and anise",
        "cuisine": ["Italian", "Mediterranean", "Thai", "Vietnamese"],
        "pairings": ["tomato", "garlic", "oregano", "olive oil", "parsley"]
    },

    "Bay Leaf": {
        "flavor_profile": "herbaceous, woody, and slightly floral with subtle eucalyptus notes",
        "cuisine": ["Mediterranean", "French", "Indian", "American"],
        "pairings": ["thyme", "rosemary", "black pepper", "parsley", "juniper berries"]
    },

    "Buchu": {
        "flavor_profile": "minty, herbal, and slightly fruity with blackcurrant-like notes",
        "cuisine": ["South African"],
        "pairings": ["mint", "rosemary", "sage", "lemongrass", "coriander"]
    },

    "Capers": {
        "flavor_profile": "briny, tangy, and floral with sharp, salty acidity",
        "cuisine": ["Mediterranean", "Italian", "Middle Eastern"],
        "pairings": ["lemon", "garlic", "parsley", "thyme", "olive oil"]
    },

    "Celery": {
        "flavor_profile": "fresh, crisp, and mildly peppery with herbal, green notes",
        "cuisine": ["American", "European", "Mediterranean"],
        "pairings": ["parsley", "caraway", "dill", "bay leaf", "thyme"]
    },
    "Cinnamon": {
        "flavor_profile": "warm, sweet, woody, and aromatic with subtle spicy heat",
        "cuisine": ["Indian", "Middle Eastern", "European", "American"],
        "pairings": ["clove", "nutmeg", "ginger", "cardamom", "allspice"]
    },

    "Chamomile": {
        "flavor_profile": "floral, apple-like, mildly sweet, and gently herbaceous",
        "cuisine": ["European", "Mediterranean"],
        "pairings": ["mint", "lemon balm", "lavender", "honey", "cinnamon"]
    },

    "Chinese Keys": {
        "flavor_profile": "pungent, spicy, and aromatic with ginger-like heat and citrusy undertones",
        "cuisine": ["Chinese", "Southeast Asian"],
        "pairings": ["ginger", "garlic", "star anise", "Sichuan pepper", "coriander"]
    },

    "Cloves": {
        "flavor_profile": "intensely warm, sweet, and spicy with strong aromatic depth",
        "cuisine": ["Indian", "Middle Eastern", "Caribbean", "European"],
        "pairings": ["cinnamon", "nutmeg", "allspice", "ginger", "cardamom"]
    },

    "Curry Leaf": {
        "flavor_profile": "fragrant, citrusy, and herbal with warm, nutty undertones",
        "cuisine": ["Indian", "Sri Lankan", "South Asian"],
        "pairings": ["cumin", "mustard seed", "turmeric", "ginger", "coriander"]
    },

    "Field Mint": {
        "flavor_profile": "cool, bright, and sharply minty with herbal freshness",
        "cuisine": ["European", "Asian", "Middle Eastern"],
        "pairings": ["parsley", "lemon balm", "coriander", "ginger", "chamomile"]
    },

    "French Tarragon": {
        "flavor_profile": "sweet, anise-like, herbal, and slightly peppery with warm aromatic notes",
        "cuisine": ["French", "European"],
        "pairings": ["parsley", "chives", "thyme", "lemon zest", "black pepper"]
    },

    "Garden Nasturtium": {
        "flavor_profile": "peppery, bright, and slightly floral with mustard-like heat",
        "cuisine": ["European", "American"],
        "pairings": ["parsley", "chives", "mustard", "black pepper", "lemon"]
    },

    "Ginger": {
        "flavor_profile": "spicy, warm, citrusy, and pungent with sweet aromatic heat",
        "cuisine": ["Indian", "Chinese", "Thai", "Caribbean"],
        "pairings": ["garlic", "turmeric", "coriander", "cinnamon", "Sichuan pepper"]
    },
    "Hops": {
        "flavor_profile": "bitter, floral, citrusy, and resinous with herbal and pine-like notes",
        "cuisine": ["European", "American"],
        "pairings": ["coriander", "juniper berries", "lemongrass", "ginger", "sage"]
    },

    "Horseradish": {
        "flavor_profile": "hot, pungent, sharp, and sinus-clearing with mustard-like heat",
        "cuisine": ["European", "American", "Russian"],
        "pairings": ["mustard", "black pepper", "garlic", "dill", "parsley"]
    },

    "Hyssop": {
        "flavor_profile": "minty, slightly bitter, and herbal with floral and camphor-like undertones",
        "cuisine": ["Middle Eastern", "Mediterranean"],
        "pairings": ["mint", "sage", "thyme", "oregano", "lavender"]
    },

    "Lemon Verbena": {
        "flavor_profile": "bright, lemony, floral, and citrus-forward with sweet herbal notes",
        "cuisine": ["European", "Latin American"],
        "pairings": ["mint", "lemongrass", "ginger", "chamomile", "basil"]
    },

    "Lemongrass": {
        "flavor_profile": "citrusy, lemony, and herbal with mild ginger-like warmth",
        "cuisine": ["Thai", "Vietnamese", "Indonesian"],
        "pairings": ["ginger", "garlic", "mint", "Sichuan pepper", "coriander"]
    },

    "Licorice": {
        "flavor_profile": "sweet, earthy, and strongly anise-like with warm herbal depth",
        "cuisine": ["Chinese", "Middle Eastern", "European"],
        "pairings": ["anise", "fennel", "star anise", "cinnamon", "clove"]
    },

    "Makrut Lime": {
        "flavor_profile": "intensely citrusy, floral, and aromatic with bright lime and herbal notes",
        "cuisine": ["Thai", "Indonesian", "Cambodian"],
        "pairings": ["lemongrass", "ginger", "garlic", "mint", "coriander"]
    },

    "Mint": {
        "flavor_profile": "cool, bright, sweet, and herbal with refreshing menthol notes",
        "cuisine": ["Middle Eastern", "Mediterranean", "Indian"],
        "pairings": ["parsley", "lemon", "coriander", "ginger", "basil"]
    },

    "Oregano": {
        "flavor_profile": "earthy, robust, and slightly peppery with warm herbal bitterness",
        "cuisine": ["Italian", "Greek", "Mexican"],
        "pairings": ["basil", "thyme", "garlic", "black pepper", "marjoram"]
    },

    "Peppermint": {
        "flavor_profile": "cool, sharp, and sweet with strong menthol intensity",
        "cuisine": ["European", "American", "Middle Eastern"],
        "pairings": ["chocolate", "cinnamon", "ginger", "lemon balm", "chamomile"]
    },
    "Rue": {
        "flavor_profile": "bitter, pungent, and strongly herbal with citrus-like sharpness",
        "cuisine": ["Mediterranean", "Ethiopian"],
        "pairings": ["garlic", "oregano", "sage", "thyme", "black pepper"]
    },

    "Saffron": {
        "flavor_profile": "floral, honey-like, earthy, and slightly bitter with warm aromatic depth",
        "cuisine": ["Middle Eastern", "Indian", "Spanish", "Mediterranean"],
        "pairings": ["cardamom", "cinnamon", "turmeric", "rose water", "bay leaf"]
    },

    "Spearmint": {
        "flavor_profile": "sweet, mild, and cool with gentle menthol and herbal freshness",
        "cuisine": ["Middle Eastern", "Mediterranean", "American"],
        "pairings": ["parsley", "lemon", "coriander", "basil", "oregano"]
    },

    "Turmeric": {
        "flavor_profile": "earthy, warm, slightly bitter, and peppery with mild ginger-like notes",
        "cuisine": ["Indian", "Thai", "Middle Eastern"],
        "pairings": ["cumin", "coriander", "ginger", "mustard seed", "black pepper"]
    },

    "Wasabi": {
        "flavor_profile": "hot, sharp, and sinus-clearing with clean, green vegetal heat",
        "cuisine": ["Japanese"],
        "pairings": ["ginger", "soy sauce", "mustard", "horseradish", "seaweed"]
    },

    "Wormwood": {
        "flavor_profile": "intensely bitter, herbal, and aromatic with minty and anise-like undertones",
        "cuisine": ["European", "Mediterranean"],
        "pairings": ["anise", "fennel", "sage", "hyssop", "angelica"]
    },

    "Zedoary": {
        "flavor_profile": "earthy, woody, and slightly bitter with ginger-like heat and camphor notes",
        "cuisine": ["Indian", "Indonesian"],
        "pairings": ["ginger", "turmeric", "coriander", "garlic", "lemongrass"]
    },

    "Wild Mint": {
        "flavor_profile": "sharp, cool, and strongly herbal with bright menthol intensity",
        "cuisine": ["Native American", "European", "Middle Eastern"],
        "pairings": ["parsley", "lemon balm", "ginger", "oregano", "sage"]
    },

    "Horsemint": {
        "flavor_profile": "minty, spicy, and slightly citrusy with warm herbal depth",
        "cuisine": ["Native American", "Mexican"],
        "pairings": ["oregano", "sage", "thyme", "lemongrass", "ginger"]
    },

    "Loveroot": {
        "flavor_profile": "sweet, earthy, and slightly bitter with warm herbal notes",
        "cuisine": ["Native American"],
        "pairings": ["sage", "mint", "juniper", "wild onion", "oregano"]
    },

    "California Bay": {
        "flavor_profile": "strongly herbal, resinous, and pungent with eucalyptus-like sharpness",
        "cuisine": ["American", "Native Californian"],
        "pairings": ["sagebrush", "juniper", "thyme", "black pepper", "garlic"]
    },

    "Sagebrush": {
        "flavor_profile": "bitter, resinous, and strongly herbal with camphor-like intensity",
        "cuisine": ["Native American"],
        "pairings": ["juniper", "sage", "garlic", "oregano", "thyme"]
    },

    "Juniper": {
        "flavor_profile": "piney, resinous, sharp, and slightly citrusy with peppery notes",
        "cuisine": ["Scandinavian", "German", "Central European"],
        "pairings": ["bay leaf", "rosemary", "thyme", "black pepper", "garlic"]
    },

    "Wild Onion": {
        "flavor_profile": "sharp, savory, and mildly sweet with bright onion-like pungency",
        "cuisine": ["Native American", "American"],
        "pairings": ["sage", "mint", "garlic", "parsley", "black pepper"]
    },
}

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
