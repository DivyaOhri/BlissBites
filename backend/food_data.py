# Food data (used as fallback)
FOOD_DATA = [
    # ─── 1. Desi Urban Cafe (DUC) ─────────────────────────────────────────────
 
    # Mocktails
    {"name": "Fresh Lime Soda (DUC)", "tags": ["cold", "refreshing", "tangy", "light"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Lemon Ice Tea (DUC)", "tags": ["cold", "tangy", "refreshing", "light"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Virgin Mojito (DUC)", "tags": ["cold", "refreshing", "minty", "light"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Peach Mojito (DUC)", "tags": ["cold", "fruity", "refreshing", "sweet"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Strawberry Mojito (DUC)", "tags": ["cold", "fruity", "refreshing", "sweet"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Blueberry Mojito (DUC)", "tags": ["cold", "fruity", "refreshing", "sweet"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Green Apple Mojito (DUC)", "tags": ["cold", "fruity", "refreshing", "tangy"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Watermelon Mojito (DUC)", "tags": ["cold", "fruity", "refreshing", "light"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chilli Guava (DUC)", "tags": ["cold", "spicy", "tangy", "unique"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Burgers
    {"name": "Aloo Tikki Burger (DUC)", "tags": ["quick", "budget", "vegetarian", "comfort food"], "price": 40, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Burger (DUC)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Burger (DUC)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Burger (DUC)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Maharaja Burger (DUC)", "tags": ["filling", "loaded", "vegetarian", "indulgent"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chicken Burger (DUC)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Shakes
    {"name": "Mango Shake (DUC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Vanilla Shake (DUC)", "tags": ["cold", "sweet", "classic", "light"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cold Coffee Shake (DUC)", "tags": ["cold", "energizing", "refreshing", "classic"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chocolate Shake (DUC)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Black Current Shake (DUC)", "tags": ["cold", "fruity", "unique", "sweet"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Strawberry Shake (DUC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Oreo Shake (DUC)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 100, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Kitkat Shake (DUC)", "tags": ["cold", "sweet", "indulgent", "fun"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Sandwiches
    {"name": "Butter Bread Toast (DUC)", "tags": ["simple", "light", "quick", "budget"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Sandwich (DUC)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Corn Sandwich (DUC)", "tags": ["cheesy", "sweet", "filling", "quick"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Paneer Sandwich (DUC)", "tags": ["cheesy", "high protein", "filling", "vegetarian"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Pizza Sandwich (DUC)", "tags": ["cheesy", "filling", "indulgent", "unique"], "price": 130, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chicken Sandwich (DUC)", "tags": ["non-veg", "filling", "high protein", "quick"], "price": 190, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Pizza (Small)
    {"name": "Cheese Onion Pizza Small (DUC)", "tags": ["cheesy", "vegetarian", "classic", "comfort food"], "price": 100, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Corn Pizza Small (DUC)", "tags": ["cheesy", "sweet", "vegetarian", "light"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Paneer Pizza Small (DUC)", "tags": ["cheesy", "high protein", "vegetarian", "filling"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Tomato Pizza Small (DUC)", "tags": ["cheesy", "tangy", "vegetarian", "light"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Mushroom Pizza Small (DUC)", "tags": ["cheesy", "earthy", "vegetarian", "filling"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Margherita Pizza Small (DUC)", "tags": ["classic", "cheesy", "vegetarian", "light"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Pizza (Medium)
    {"name": "Cheese Onion Pizza Medium (DUC)", "tags": ["cheesy", "vegetarian", "classic", "sharing"], "price": 210, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Corn Pizza Medium (DUC)", "tags": ["cheesy", "sweet", "vegetarian", "sharing"], "price": 210, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Paneer Pizza Medium (DUC)", "tags": ["cheesy", "high protein", "vegetarian", "sharing"], "price": 210, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Tomato Pizza Medium (DUC)", "tags": ["cheesy", "tangy", "vegetarian", "sharing"], "price": 210, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Mushroom Pizza Medium (DUC)", "tags": ["cheesy", "earthy", "vegetarian", "sharing"], "price": 210, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Margherita Pizza Medium (DUC)", "tags": ["classic", "cheesy", "vegetarian", "sharing"], "price": 210, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Pizza (Large)
    {"name": "Cheese Onion Pizza Large (DUC)", "tags": ["cheesy", "vegetarian", "classic", "sharing"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Corn Pizza Large (DUC)", "tags": ["cheesy", "sweet", "vegetarian", "sharing"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Paneer Pizza Large (DUC)", "tags": ["cheesy", "high protein", "vegetarian", "sharing"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Tomato Pizza Large (DUC)", "tags": ["cheesy", "tangy", "vegetarian", "sharing"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cheese Mushroom Pizza Large (DUC)", "tags": ["cheesy", "earthy", "vegetarian", "sharing"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Margherita Pizza Large (DUC)", "tags": ["classic", "cheesy", "vegetarian", "sharing"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Pasta
    {"name": "Red Sauce Pasta (DUC)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "White Sauce Pasta (DUC)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Mix Sauce Pasta (DUC)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 130, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Tandoori Pasta (DUC)", "tags": ["spicy", "smoky", "vegetarian", "unique"], "price": 130, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Makhani Pasta (DUC)", "tags": ["rich", "creamy", "vegetarian", "indulgent"], "price": 150, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chicken Pasta (DUC)", "tags": ["non-veg", "filling", "high protein", "comfort food"], "price": 190, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Chinese
    {"name": "Veg Noodle (DUC)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Hakka Noodle (DUC)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Noodle (DUC)", "tags": ["filling", "high protein", "vegetarian", "comfort food"], "price": 130, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Spring Roll (DUC)", "tags": ["crispy", "light", "vegetarian", "snack"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Spring Roll (DUC)", "tags": ["crispy", "high protein", "vegetarian", "snack"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Momos (DUC)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Momos (DUC)", "tags": ["filling", "high protein", "vegetarian", "snack"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Kurkure Momos (DUC)", "tags": ["crispy", "crunchy", "vegetarian", "snack"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Kurkure Momos (DUC)", "tags": ["crispy", "high protein", "vegetarian", "snack"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chilli Potato (DUC)", "tags": ["spicy", "crispy", "snack", "bold"], "price": 100, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Honey Chilli Potato (DUC)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 130, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Honey Chilli Cauliflower (DUC)", "tags": ["sweet", "spicy", "vegetarian", "snack"], "price": 150, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Manchurian (DUC)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chilli Paneer (DUC)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 170, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Crispy Corn (DUC)", "tags": ["crispy", "light", "snack", "vegetarian"], "price": 180, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Special Pizza (Small)
    {"name": "Farm Fresh Pizza Small (DUC)", "tags": ["loaded", "vegetarian", "fresh", "filling"], "price": 190, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Tandoori Paneer Pizza Small (DUC)", "tags": ["spicy", "high protein", "vegetarian", "smoky"], "price": 190, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Makhani Pizza Small (DUC)", "tags": ["rich", "high protein", "creamy", "vegetarian"], "price": 190, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veggie Deluxe Pizza Small (DUC)", "tags": ["loaded", "vegetarian", "indulgent", "filling"], "price": 220, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Tandoori Chicken Pizza Small (DUC)", "tags": ["spicy", "non-veg", "smoky", "filling"], "price": 250, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Special Pizza (Medium)
    {"name": "Farm Fresh Pizza Medium (DUC)", "tags": ["loaded", "vegetarian", "fresh", "sharing"], "price": 290, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Tandoori Paneer Pizza Medium (DUC)", "tags": ["spicy", "high protein", "vegetarian", "sharing"], "price": 290, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Makhani Pizza Medium (DUC)", "tags": ["rich", "high protein", "creamy", "sharing"], "price": 290, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veggie Deluxe Pizza Medium (DUC)", "tags": ["loaded", "vegetarian", "indulgent", "sharing"], "price": 330, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Tandoori Chicken Pizza Medium (DUC)", "tags": ["spicy", "non-veg", "smoky", "sharing"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Special Pizza (Large)
    {"name": "Farm Fresh Pizza Large (DUC)", "tags": ["loaded", "vegetarian", "fresh", "sharing"], "price": 450, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Tandoori Paneer Pizza Large (DUC)", "tags": ["spicy", "high protein", "vegetarian", "sharing"], "price": 450, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Makhani Pizza Large (DUC)", "tags": ["rich", "high protein", "creamy", "sharing"], "price": 450, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veggie Deluxe Pizza Large (DUC)", "tags": ["loaded", "vegetarian", "indulgent", "sharing"], "price": 510, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Tandoori Chicken Pizza Large (DUC)", "tags": ["spicy", "non-veg", "smoky", "sharing"], "price": 590, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Stuffed Items
    {"name": "Zingy Parcel (DUC)", "tags": ["spicy", "quick", "snack", "vegetarian"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Parcel (DUC)", "tags": ["filling", "high protein", "vegetarian", "snack"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Plain Garlic Bread (DUC)", "tags": ["savory", "warm", "light", "quick"], "price": 100, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Stuff Garlic Bread (DUC)", "tags": ["savory", "cheesy", "warm", "filling"], "price": 140, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Calzone Pocket (DUC)", "tags": ["cheesy", "filling", "indulgent", "unique"], "price": 140, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Lassi
    {"name": "Sweet Lassi (DUC)", "tags": ["cold", "sweet", "refreshing", "comforting"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Namkeen Lassi (DUC)", "tags": ["cold", "salty", "refreshing", "light"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Mango Lassi (DUC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Kesar Lassi (DUC)", "tags": ["cold", "aromatic", "premium", "sweet"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Strawberry Lassi (DUC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Tandoori Snacks (Half)
    {"name": "Masala Chaap Half (DUC)", "tags": ["spicy", "smoky", "vegetarian", "snack"], "price": 150, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Malai Chaap Half (DUC)", "tags": ["creamy", "smoky", "vegetarian", "snack"], "price": 150, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Afghani Chaap Half (DUC)", "tags": ["aromatic", "creamy", "vegetarian", "snack"], "price": 180, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Masala Paneer Tikka Half (DUC)", "tags": ["spicy", "high protein", "grilled", "snack"], "price": 150, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Malai Paneer Tikka Half (DUC)", "tags": ["creamy", "high protein", "grilled", "snack"], "price": 180, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Tandoori Snacks (Full)
    {"name": "Masala Chaap Full (DUC)", "tags": ["spicy", "smoky", "vegetarian", "filling"], "price": 300, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Malai Chaap Full (DUC)", "tags": ["creamy", "smoky", "vegetarian", "filling"], "price": 300, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Afghani Chaap Full (DUC)", "tags": ["aromatic", "creamy", "vegetarian", "filling"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Masala Paneer Tikka Full (DUC)", "tags": ["spicy", "high protein", "grilled", "filling"], "price": 300, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Malai Paneer Tikka Full (DUC)", "tags": ["creamy", "high protein", "grilled", "filling"], "price": 350, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Chaat
    {"name": "Chana Tikki (DUC)", "tags": ["tangy", "spicy", "street food", "snack"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Crispy Aloo Tikki (DUC)", "tags": ["crispy", "spicy", "street food", "snack"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Dahi Bhalla (DUC)", "tags": ["tangy", "cooling", "street food", "snack"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Bhalla Papdi (DUC)", "tags": ["tangy", "crunchy", "street food", "snack"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Pav Bhaji (DUC)", "tags": ["spicy", "filling", "street food", "comfort food"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Thali
    {"name": "Veg Thali (DUC)", "tags": ["balanced", "vegetarian", "filling", "variety"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Supreme Thali (DUC)", "tags": ["balanced", "vegetarian", "premium", "variety"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Veg Deluxe Thali (DUC)", "tags": ["balanced", "vegetarian", "indulgent", "variety"], "price": 150, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Kathi Roll
    {"name": "Veg Kathi Roll (DUC)", "tags": ["quick", "light", "vegetarian", "snack"], "price": 100, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Kathi Roll (DUC)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Malai Kathi Roll (DUC)", "tags": ["creamy", "high protein", "vegetarian", "filling"], "price": 140, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "1 Egg Kathi Roll (DUC)", "tags": ["non-veg", "quick", "light", "snack"], "price": 100, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "2 Egg Kathi Roll (DUC)", "tags": ["non-veg", "filling", "high protein", "quick"], "price": 140, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chicken Kathi Roll (DUC)", "tags": ["non-veg", "filling", "spicy", "quick"], "price": 160, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Kulhad Chai & Beverages
    {"name": "Green Tea (DUC)", "tags": ["warm", "healthy", "light", "refreshing"], "price": 20, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Normal Chai (DUC)", "tags": ["warm", "simple", "comforting", "budget"], "price": 20, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Adrak Chai (DUC)", "tags": ["warm", "comforting", "spicy", "simple"], "price": 30, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Rose Chai (DUC)", "tags": ["warm", "aromatic", "light", "refreshing"], "price": 30, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chocolate Chai (DUC)", "tags": ["warm", "sweet", "indulgent", "unique"], "price": 30, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Kesar Chai (DUC)", "tags": ["warm", "aromatic", "premium", "comforting"], "price": 30, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Masala Chai (DUC)", "tags": ["warm", "spicy", "comforting", "energizing"], "price": 30, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Hot Coffee (DUC)", "tags": ["warm", "energizing", "simple", "comforting"], "price": 30, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Hot Choco Coffee (DUC)", "tags": ["warm", "sweet", "indulgent", "comforting"], "price": 40, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Cappuccino (DUC)", "tags": ["warm", "frothy", "comforting", "classic"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # South Indian
    {"name": "Plain Dosa (DUC)", "tags": ["South Indian", "light", "crispy", "simple"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Masala Dosa (DUC)", "tags": ["South Indian", "filling", "crispy", "classic"], "price": 90, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Dosa (DUC)", "tags": ["South Indian", "high protein", "filling", "crispy"], "price": 120, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Paratha
    {"name": "Aloo Paratha (DUC)", "tags": ["comforting", "filling", "home-style", "budget"], "price": 40, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Onion Paratha (DUC)", "tags": ["simple", "comforting", "home-style", "budget"], "price": 40, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Aloo Pyaz Paratha (DUC)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 40, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Mix Paratha (DUC)", "tags": ["filling", "variety", "comforting", "home-style"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Paratha (DUC)", "tags": ["filling", "high protein", "comforting", "home-style"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Omelette
    {"name": "Egg Bhurji (DUC)", "tags": ["high protein", "spicy", "quick", "simple"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Egg Omelet (DUC)", "tags": ["high protein", "simple", "quick", "light"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Bread Omelet (DUC)", "tags": ["high protein", "filling", "quick", "budget"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Dessert
    {"name": "Choco Lava Cake (DUC)", "tags": ["sweet", "warm", "indulgent", "dessert"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Donut Ice Cream (DUC)", "tags": ["sweet", "cold", "indulgent", "dessert"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Walnut Brownie (DUC)", "tags": ["sweet", "rich", "indulgent", "dessert"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Confetti Brownie (DUC)", "tags": ["sweet", "fun", "indulgent", "dessert"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Choco Star (DUC)", "tags": ["sweet", "warm", "chocolatey", "dessert"], "price": 60, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Waffle with Ice Cream (DUC)", "tags": ["sweet", "warm", "indulgent", "dessert"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Rice Combo (Small)
    {"name": "Rajma Chawal Small (DUC)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Curry Chawal Small (DUC)", "tags": ["warm", "comforting", "simple", "home-style"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chole Chawal Small (DUC)", "tags": ["spicy", "filling", "comforting", "home-style"], "price": 50, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Chawal Small (DUC)", "tags": ["high protein", "comforting", "filling", "home-style"], "price": 70, "restaurant": "Desi Urban Cafe (DUC)"},
 
    # Rice Combo (Large)
    {"name": "Rajma Chawal Large (DUC)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Curry Chawal Large (DUC)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Chole Chawal Large (DUC)", "tags": ["spicy", "filling", "comforting", "home-style"], "price": 80, "restaurant": "Desi Urban Cafe (DUC)"},
    {"name": "Paneer Chawal Large (DUC)", "tags": ["high protein", "comforting", "filling", "home-style"], "price": 110, "restaurant": "Desi Urban Cafe (DUC)"},
 
 
    # ─── 2. Wok 'n' Roll (WNR) Café ──────────────────────────────────────────
 
    # Pasta & Macaroni
    {"name": "White Sauce Pasta (WNR)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 130, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Red Sauce Pasta (WNR)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Masala Pasta (WNR)", "tags": ["spicy", "comfort food", "vegetarian", "filling"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Veg Macaroni (WNR)", "tags": ["light", "vegetarian", "quick", "comfort food"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cheese Macaroni (WNR)", "tags": ["cheesy", "indulgent", "comfort food", "quick"], "price": 110, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Beverages
    {"name": "Hot Coffee (WNR)", "tags": ["warm", "energizing", "simple", "comforting"], "price": 30, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cold Coffee (WNR)", "tags": ["cold", "energizing", "refreshing", "classic"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Green Coffee (WNR)", "tags": ["warm", "healthy", "light", "unique"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Hot Chocolate (WNR)", "tags": ["warm", "sweet", "comforting", "indulgent"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Veg Soup (WNR)", "tags": ["warm", "light", "healthy", "soup"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Sweet Corn Soup (WNR)", "tags": ["warm", "sweet", "light", "soup"], "price": 50, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Masala Tea (WNR)", "tags": ["warm", "spicy", "comforting", "budget"], "price": 20, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Green Tea (WNR)", "tags": ["warm", "healthy", "light", "refreshing"], "price": 26, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Honey Lemon Tea (WNR)", "tags": ["warm", "tangy", "soothing", "light"], "price": 28, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Ice Tea (WNR)", "tags": ["cold", "refreshing", "light", "sweet"], "price": 50, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Kulcha, Bread & Patty
    {"name": "Cheese Paneer Kulcha (WNR)", "tags": ["cheesy", "high protein", "filling", "warm"], "price": 95, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cheese Onion Kulcha (WNR)", "tags": ["cheesy", "savory", "filling", "warm"], "price": 85, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Veg Cheese Kulcha (WNR)", "tags": ["cheesy", "vegetarian", "filling", "warm"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Kulcha with Chana (WNR)", "tags": ["filling", "spicy", "comforting", "classic"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Aloo Patty (WNR)", "tags": ["crispy", "budget", "snack", "vegetarian"], "price": 30, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Paneer Patty (WNR)", "tags": ["crispy", "high protein", "snack", "vegetarian"], "price": 40, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cheese Corn Patty (WNR)", "tags": ["cheesy", "sweet", "snack", "crispy"], "price": 75, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Pizza Patty (WNR)", "tags": ["cheesy", "savory", "snack", "unique"], "price": 86, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cassata Patty (WNR)", "tags": ["sweet", "unique", "snack", "dessert-like"], "price": 96, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Veg Cold Sandwich (WNR)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Butter Grilled Sandwich (WNR)", "tags": ["warm", "buttery", "quick", "vegetarian"], "price": 96, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cheese Grilled Sandwich (WNR)", "tags": ["cheesy", "grilled", "filling", "quick"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Burgers
    {"name": "Veg Burger (WNR)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 85, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cheese Burger (WNR)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Snacks
    {"name": "Butter Corns (WNR)", "tags": ["warm", "buttery", "light", "snack"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Fried Corns (WNR)", "tags": ["crispy", "light", "snack", "vegetarian"], "price": 76, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Spring Rolls (WNR)", "tags": ["crispy", "light", "vegetarian", "snack"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Spring Rolls with Gravy (WNR)", "tags": ["crispy", "saucy", "vegetarian", "snack"], "price": 125, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "French Fries (WNR)", "tags": ["crispy", "snack", "quick", "comfort food"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Veg Noodles (WNR)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 90, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Hakka Noodles (WNR)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 110, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cheese Noodles (WNR)", "tags": ["cheesy", "indulgent", "comfort food", "filling"], "price": 140, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Gravy Noodles (WNR)", "tags": ["saucy", "comforting", "vegetarian", "filling"], "price": 120, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Honey Chilli Potato (WNR)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 110, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Honey Chilli Mushroom (WNR)", "tags": ["sweet", "spicy", "earthy", "snack"], "price": 140, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Honey Chilli Cauliflower (WNR)", "tags": ["sweet", "spicy", "vegetarian", "snack"], "price": 160, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Pav Bhaji (WNR)", "tags": ["spicy", "filling", "street food", "comfort food"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Vada Pav (WNR)", "tags": ["spicy", "budget", "street food", "snack"], "price": 40, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Bar-B-Q
    {"name": "Mutton Seekh Kebab (WNR)", "tags": ["non-veg", "grilled", "spicy", "filling"], "price": 175, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Chicken Seekh (WNR)", "tags": ["non-veg", "grilled", "spicy", "filling"], "price": 165, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Fish Tikka (WNR)", "tags": ["non-veg", "seafood", "grilled", "spicy"], "price": 190, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Chicken Leg Piece (WNR)", "tags": ["non-veg", "grilled", "filling", "bold"], "price": 180, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Paneer Tikka (WNR)", "tags": ["high protein", "grilled", "vegetarian", "smoky"], "price": 160, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Mushroom Tikka (WNR)", "tags": ["earthy", "grilled", "vegetarian", "smoky"], "price": 150, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Pineapple Chorasko (WNR)", "tags": ["sweet", "tangy", "vegetarian", "grilled"], "price": 130, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Cold Beverages
    {"name": "Cold Coffee with Ice Cream (WNR)", "tags": ["cold", "sweet", "indulgent", "energizing"], "price": 110, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Chocolate Shake (WNR)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 76, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Strawberry Crush (WNR)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 75, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Mango Shake (WNR)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 90, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Banana Shake (WNR)", "tags": ["cold", "filling", "energizing", "high protein"], "price": 65, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Ice Cream Shake (WNR)", "tags": ["cold", "sweet", "indulgent", "creamy"], "price": 85, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Watermelon Shake (WNR)", "tags": ["cold", "fruity", "refreshing", "light"], "price": 76, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Sweet Lassi (WNR)", "tags": ["cold", "sweet", "refreshing", "comforting"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Salted Lassi (WNR)", "tags": ["cold", "salty", "refreshing", "light"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Fresh Lime Water (WNR)", "tags": ["cold", "refreshing", "tangy", "light"], "price": 50, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Fresh Lime Soda (WNR)", "tags": ["cold", "fizzy", "refreshing", "tangy"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "FL Soda Blueberry (WNR)", "tags": ["cold", "fizzy", "fruity", "refreshing"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "FL Soda Kalakhatta (WNR)", "tags": ["cold", "fizzy", "tangy", "refreshing"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "FL Soda BlueMoon (WNR)", "tags": ["cold", "fizzy", "unique", "refreshing"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Eggs
    {"name": "Egg Paratha (WNR)", "tags": ["high protein", "filling", "comforting", "non-veg"], "price": 65, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Egg Bhurji (WNR)", "tags": ["high protein", "spicy", "quick", "simple"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Bread Omelet (WNR)", "tags": ["high protein", "filling", "quick", "budget"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Egg Roll (WNR)", "tags": ["non-veg", "quick", "light", "snack"], "price": 80, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Breakfast
    {"name": "Lacha Paratha (WNR)", "tags": ["flaky", "comforting", "layered", "classic"], "price": 30, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Aloo Pyaj Paratha (WNR)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 40, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Pyaj Paratha (WNR)", "tags": ["simple", "comforting", "home-style", "budget"], "price": 40, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Gobhi Paratha (WNR)", "tags": ["filling", "comforting", "home-style", "vegetarian"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Paneer Pyaj Paratha (WNR)", "tags": ["filling", "high protein", "comforting", "home-style"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Mix Paratha (WNR)", "tags": ["filling", "variety", "comforting", "home-style"], "price": 90, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Sugar Paratha (WNR)", "tags": ["sweet", "simple", "light", "comfort food"], "price": 40, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Poha (WNR)", "tags": ["light", "simple", "quick", "home-style"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Maggi
    {"name": "Plain Maggi (WNR)", "tags": ["quick", "simple", "comfort food", "budget"], "price": 40, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Tadka Maggi (WNR)", "tags": ["spicy", "quick", "comfort food", "bold"], "price": 65, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Vegetable Maggi (WNR)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 66, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Corn Maggi (WNR)", "tags": ["sweet", "quick", "comfort food", "light"], "price": 65, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Cheese Maggi (WNR)", "tags": ["cheesy", "indulgent", "comfort food", "quick"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Double Masala Maggi (WNR)", "tags": ["spicy", "bold", "quick", "comfort food"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Chaap
    {"name": "Butter Masala Chaap (WNR)", "tags": ["rich", "creamy", "vegetarian", "filling"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Veg Chilli Chaap (WNR)", "tags": ["spicy", "vegetarian", "bold", "snack"], "price": 100, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Tadka Chaap (WNR)", "tags": ["spicy", "vegetarian", "bold", "filling"], "price": 110, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Malai Chaap (WNR)", "tags": ["creamy", "smoky", "vegetarian", "snack"], "price": 110, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Momos
    {"name": "Veg Momos (WNR)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 90, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Veg Fried Momos (WNR)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 108, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Chicken Momos (WNR)", "tags": ["non-veg", "light", "steamed", "snack"], "price": 145, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Spl Honey Chilli Momos (WNR)", "tags": ["sweet", "spicy", "crispy", "snack"], "price": 150, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
    # Sweets
    {"name": "Hot Gulab Jamun (WNR)", "tags": ["sweet", "warm", "dessert", "classic"], "price": 40, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Butterscotch Kheer (WNR)", "tags": ["sweet", "creamy", "dessert", "comforting"], "price": 60, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
    {"name": "Gajar Ka Halwa (WNR)", "tags": ["sweet", "warm", "dessert", "traditional"], "price": 70, "restaurant": "Wok 'n' Roll (WNR) Cafe"},
 
 
    # ─── 3. Food Point ────────────────────────────────────────────────────────
 
    # Main Course Non-Veg (Half)
    {"name": "Kadai Chicken Half (Food Point)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 250, "restaurant": "Food Point"},
    {"name": "Chicken Butter Masala Half (Food Point)", "tags": ["creamy", "non-veg", "rich", "comforting"], "price": 250, "restaurant": "Food Point"},
    {"name": "Rara Chicken Half (Food Point)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 250, "restaurant": "Food Point"},
    {"name": "Egg Curry Half (Food Point)", "tags": ["comforting", "high protein", "home-style", "simple"], "price": 120, "restaurant": "Food Point"},
    {"name": "Butter Chicken Half (Food Point)", "tags": ["creamy", "non-veg", "rich", "comforting"], "price": 270, "restaurant": "Food Point"},
    {"name": "Mutton Curry Half (Food Point)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 300, "restaurant": "Food Point"},
    {"name": "Mutton Korma Half (Food Point)", "tags": ["rich", "creamy", "non-veg", "indulgent"], "price": 320, "restaurant": "Food Point"},
    {"name": "Rara Mutton Half (Food Point)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 350, "restaurant": "Food Point"},
 
    # Main Course Non-Veg (Full)
    {"name": "Kadai Chicken Full (Food Point)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 450, "restaurant": "Food Point"},
    {"name": "Chicken Butter Masala Full (Food Point)", "tags": ["creamy", "non-veg", "rich", "sharing"], "price": 480, "restaurant": "Food Point"},
    {"name": "Rara Chicken Full (Food Point)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 520, "restaurant": "Food Point"},
    {"name": "Egg Curry Full (Food Point)", "tags": ["comforting", "high protein", "home-style", "filling"], "price": 170, "restaurant": "Food Point"},
    {"name": "Butter Chicken Full (Food Point)", "tags": ["creamy", "non-veg", "rich", "sharing"], "price": 499, "restaurant": "Food Point"},
    {"name": "Mutton Curry Full (Food Point)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 550, "restaurant": "Food Point"},
    {"name": "Mutton Korma Full (Food Point)", "tags": ["rich", "creamy", "non-veg", "sharing"], "price": 600, "restaurant": "Food Point"},
    {"name": "Rara Mutton Full (Food Point)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 600, "restaurant": "Food Point"},
 
    # Main Course Veg
    {"name": "Dal Tadka (Food Point)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 140, "restaurant": "Food Point"},
    {"name": "Dal Makhani (Food Point)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 160, "restaurant": "Food Point"},
    {"name": "Rajma Masala (Food Point)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 130, "restaurant": "Food Point"},
    {"name": "Chana Masala (Food Point)", "tags": ["spicy", "filling", "vegetarian", "bold"], "price": 150, "restaurant": "Food Point"},
    {"name": "Mix Veg (Food Point)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 170, "restaurant": "Food Point"},
    {"name": "Aloo Jeera (Food Point)", "tags": ["simple", "comforting", "home-style", "light"], "price": 100, "restaurant": "Food Point"},
    {"name": "Mushroom Masala (Food Point)", "tags": ["earthy", "spicy", "vegetarian", "filling"], "price": 180, "restaurant": "Food Point"},
    {"name": "Mushroom Do Pyaza (Food Point)", "tags": ["earthy", "spicy", "onion-rich", "vegetarian"], "price": 190, "restaurant": "Food Point"},
    {"name": "Malai Mushroom (Food Point)", "tags": ["creamy", "earthy", "vegetarian", "rich"], "price": 200, "restaurant": "Food Point"},
    {"name": "Kadai Mushroom (Food Point)", "tags": ["spicy", "earthy", "vegetarian", "bold"], "price": 190, "restaurant": "Food Point"},
    {"name": "Mutter Mushroom (Food Point)", "tags": ["earthy", "vegetarian", "balanced", "filling"], "price": 170, "restaurant": "Food Point"},
    {"name": "Paneer Butter Masala (Food Point)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 190, "restaurant": "Food Point"},
    {"name": "Paneer Do Pyaza (Food Point)", "tags": ["spicy", "high protein", "onion-rich", "bold"], "price": 190, "restaurant": "Food Point"},
    {"name": "Kadai Paneer (Food Point)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 200, "restaurant": "Food Point"},
    {"name": "Shahi Paneer (Food Point)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 200, "restaurant": "Food Point"},
    {"name": "Mutter Paneer (Food Point)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 170, "restaurant": "Food Point"},
    {"name": "Paneer Bhurji (Food Point)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 170, "restaurant": "Food Point"},
    {"name": "Palak Paneer (Food Point)", "tags": ["healthy", "high protein", "vegetarian", "comforting"], "price": 190, "restaurant": "Food Point"},
 
    # Biryani & Rice
    {"name": "Veg Biryani (Food Point)", "tags": ["aromatic", "vegetarian", "filling", "comfort food"], "price": 170, "restaurant": "Food Point"},
    {"name": "Egg Biryani (Food Point)", "tags": ["aromatic", "non-veg", "filling", "comfort food"], "price": 180, "restaurant": "Food Point"},
    {"name": "Chicken Biryani (Food Point)", "tags": ["aromatic", "non-veg", "filling", "comfort food"], "price": 220, "restaurant": "Food Point"},
    {"name": "Plain Rice (Food Point)", "tags": ["simple", "light", "budget", "home-style"], "price": 50, "restaurant": "Food Point"},
    {"name": "Veg Pulao (Food Point)", "tags": ["light", "aromatic", "vegetarian", "balanced"], "price": 100, "restaurant": "Food Point"},
    {"name": "Rajma Rice Small (Food Point)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 50, "restaurant": "Food Point"},
    {"name": "Rajma Rice Large (Food Point)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 90, "restaurant": "Food Point"},
 
    # Breads
    {"name": "Plain Roti (Food Point)", "tags": ["simple", "light", "budget", "home-style"], "price": 10, "restaurant": "Food Point"},
    {"name": "Butter Roti (Food Point)", "tags": ["simple", "comforting", "budget", "home-style"], "price": 15, "restaurant": "Food Point"},
    {"name": "Garlic Naan (Food Point)", "tags": ["aromatic", "soft", "savory", "classic"], "price": 40, "restaurant": "Food Point"},
    {"name": "Laccha Prantha (Food Point)", "tags": ["flaky", "comforting", "layered", "classic"], "price": 30, "restaurant": "Food Point"},
    {"name": "Butter Naan (Food Point)", "tags": ["soft", "comforting", "buttery", "classic"], "price": 35, "restaurant": "Food Point"},
    {"name": "Plain Naan (Food Point)", "tags": ["soft", "simple", "light", "classic"], "price": 25, "restaurant": "Food Point"},
    {"name": "Missi Roti (Food Point)", "tags": ["earthy", "rustic", "home-style", "simple"], "price": 20, "restaurant": "Food Point"},
    {"name": "Paneer Naan with Gravy (Food Point)", "tags": ["filling", "high protein", "comforting", "complete meal"], "price": 130, "restaurant": "Food Point"},
 
    # Thali
    {"name": "Special Thali (Food Point)", "tags": ["balanced", "vegetarian", "filling", "variety"], "price": 180, "restaurant": "Food Point"},
    {"name": "Special Non Veg Thali (Food Point)", "tags": ["balanced", "non-veg", "filling", "variety"], "price": 220, "restaurant": "Food Point"},
 
    # Indian Snacks
    {"name": "Veg Pakora (Food Point)", "tags": ["crispy", "warm", "vegetarian", "snack"], "price": 90, "restaurant": "Food Point"},
    {"name": "Onion Pakora (Food Point)", "tags": ["crispy", "warm", "vegetarian", "snack"], "price": 90, "restaurant": "Food Point"},
    {"name": "Paneer Pakora (Food Point)", "tags": ["crispy", "high protein", "warm", "snack"], "price": 170, "restaurant": "Food Point"},
    {"name": "Mushroom Pakora (Food Point)", "tags": ["crispy", "earthy", "warm", "snack"], "price": 150, "restaurant": "Food Point"},
    {"name": "Bread Pakora (Food Point)", "tags": ["crispy", "budget", "snack", "comfort food"], "price": 70, "restaurant": "Food Point"},
    {"name": "Veg Cutlet (Food Point)", "tags": ["crispy", "vegetarian", "snack", "light"], "price": 90, "restaurant": "Food Point"},
    {"name": "French Fries Small (Food Point)", "tags": ["crispy", "snack", "quick", "budget"], "price": 60, "restaurant": "Food Point"},
    {"name": "French Fries Large (Food Point)", "tags": ["crispy", "snack", "sharing", "comfort food"], "price": 110, "restaurant": "Food Point"},
 
    # Wrap & Roll
    {"name": "Veg Wrap Roll (Food Point)", "tags": ["quick", "light", "vegetarian", "snack"], "price": 70, "restaurant": "Food Point"},
    {"name": "Paneer Roll (Food Point)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 120, "restaurant": "Food Point"},
    {"name": "Afghani Chaap Roll (Food Point)", "tags": ["aromatic", "creamy", "vegetarian", "filling"], "price": 120, "restaurant": "Food Point"},
    {"name": "Malai Chaap Roll (Food Point)", "tags": ["creamy", "vegetarian", "filling", "rich"], "price": 120, "restaurant": "Food Point"},
    {"name": "Masala Chaap Roll (Food Point)", "tags": ["spicy", "vegetarian", "filling", "bold"], "price": 110, "restaurant": "Food Point"},
    {"name": "Egg Roll (Food Point)", "tags": ["non-veg", "quick", "light", "snack"], "price": 70, "restaurant": "Food Point"},
    {"name": "Chicken Roll (Food Point)", "tags": ["non-veg", "filling", "spicy", "quick"], "price": 130, "restaurant": "Food Point"},
 
    # Non-Veg Snacks
    {"name": "Chicken Momos (Food Point)", "tags": ["non-veg", "light", "steamed", "snack"], "price": 150, "restaurant": "Food Point"},
    {"name": "Chicken Manchurian (Food Point)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 250, "restaurant": "Food Point"},
    {"name": "Fried Chicken (Food Point)", "tags": ["crispy", "non-veg", "filling", "bold"], "price": 250, "restaurant": "Food Point"},
    {"name": "Fried Fish (Food Point)", "tags": ["crispy", "non-veg", "seafood", "bold"], "price": 300, "restaurant": "Food Point"},
    {"name": "Chilly Chicken Half (Food Point)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 250, "restaurant": "Food Point"},
    {"name": "Chilly Chicken Full (Food Point)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 460, "restaurant": "Food Point"},
    {"name": "Chicken Malai Tikka (Food Point)", "tags": ["creamy", "non-veg", "grilled", "rich"], "price": 250, "restaurant": "Food Point"},
    {"name": "Tandoori Chicken Half (Food Point)", "tags": ["spicy", "non-veg", "grilled", "smoky"], "price": 250, "restaurant": "Food Point"},
    {"name": "Tandoori Chicken Full (Food Point)", "tags": ["spicy", "non-veg", "grilled", "sharing"], "price": 450, "restaurant": "Food Point"},
    {"name": "Chicken Seekh Kebab (Food Point)", "tags": ["non-veg", "grilled", "spicy", "filling"], "price": 250, "restaurant": "Food Point"},
    {"name": "Mutton Seekh Kebab (Food Point)", "tags": ["non-veg", "grilled", "spicy", "filling"], "price": 350, "restaurant": "Food Point"},
 
    # Soya Chaap (Half)
    {"name": "Malai Chaap Half (Food Point)", "tags": ["creamy", "smoky", "vegetarian", "snack"], "price": 170, "restaurant": "Food Point"},
    {"name": "Afghani Chaap Half (Food Point)", "tags": ["aromatic", "creamy", "vegetarian", "snack"], "price": 170, "restaurant": "Food Point"},
    {"name": "Achari Chaap Half (Food Point)", "tags": ["tangy", "spicy", "vegetarian", "snack"], "price": 170, "restaurant": "Food Point"},
    {"name": "Garlic Chaap Half (Food Point)", "tags": ["aromatic", "savory", "vegetarian", "snack"], "price": 170, "restaurant": "Food Point"},
    {"name": "Masala Chaap Half (Food Point)", "tags": ["spicy", "smoky", "vegetarian", "snack"], "price": 170, "restaurant": "Food Point"},
 
    # Soya Chaap (Full)
    {"name": "Malai Chaap Full (Food Point)", "tags": ["creamy", "smoky", "vegetarian", "filling"], "price": 260, "restaurant": "Food Point"},
    {"name": "Afghani Chaap Full (Food Point)", "tags": ["aromatic", "creamy", "vegetarian", "filling"], "price": 260, "restaurant": "Food Point"},
    {"name": "Achari Chaap Full (Food Point)", "tags": ["tangy", "spicy", "vegetarian", "filling"], "price": 260, "restaurant": "Food Point"},
    {"name": "Garlic Chaap Full (Food Point)", "tags": ["aromatic", "savory", "vegetarian", "filling"], "price": 260, "restaurant": "Food Point"},
    {"name": "Masala Chaap Full (Food Point)", "tags": ["spicy", "smoky", "vegetarian", "filling"], "price": 260, "restaurant": "Food Point"},
 
    # Chinese Snacks
    {"name": "Veg Momos (Food Point)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 80, "restaurant": "Food Point"},
    {"name": "Fried Momos (Food Point)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 100, "restaurant": "Food Point"},
    {"name": "Paneer Momos (Food Point)", "tags": ["filling", "high protein", "vegetarian", "snack"], "price": 120, "restaurant": "Food Point"},
    {"name": "Tandoori Momos (Food Point)", "tags": ["spicy", "smoky", "vegetarian", "snack"], "price": 150, "restaurant": "Food Point"},
    {"name": "Veg Manchurian (Food Point)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 120, "restaurant": "Food Point"},
    {"name": "Pav Bhaji (Food Point)", "tags": ["spicy", "filling", "street food", "comfort food"], "price": 80, "restaurant": "Food Point"},
    {"name": "Honey Chilli Potato (Food Point)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 140, "restaurant": "Food Point"},
    {"name": "Honey Chilli Cauliflower (Food Point)", "tags": ["sweet", "spicy", "vegetarian", "snack"], "price": 160, "restaurant": "Food Point"},
    {"name": "Corn Salt & Pepper (Food Point)", "tags": ["crispy", "savory", "snack", "light"], "price": 140, "restaurant": "Food Point"},
    {"name": "Vada Pav (Food Point)", "tags": ["spicy", "budget", "street food", "snack"], "price": 90, "restaurant": "Food Point"},
    {"name": "Chilli Paneer (Food Point)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 200, "restaurant": "Food Point"},
    {"name": "Mushroom Chilli (Food Point)", "tags": ["spicy", "earthy", "vegetarian", "bold"], "price": 170, "restaurant": "Food Point"},
    {"name": "Veg Fried Rice (Food Point)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 90, "restaurant": "Food Point"},
    {"name": "Egg Fried Rice (Food Point)", "tags": ["filling", "non-veg", "quick", "comfort food"], "price": 110, "restaurant": "Food Point"},
    {"name": "Chicken Fried Rice (Food Point)", "tags": ["filling", "non-veg", "quick", "comfort food"], "price": 140, "restaurant": "Food Point"},
    {"name": "Paneer Fried Rice (Food Point)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 130, "restaurant": "Food Point"},
    {"name": "Veg Chowmein Small (Food Point)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 50, "restaurant": "Food Point"},
    {"name": "Veg Chowmein Large (Food Point)", "tags": ["quick", "vegetarian", "filling", "comfort food"], "price": 90, "restaurant": "Food Point"},
    {"name": "Paneer Chowmein Small (Food Point)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 70, "restaurant": "Food Point"},
    {"name": "Paneer Chowmein Large (Food Point)", "tags": ["filling", "high protein", "vegetarian", "comfort food"], "price": 120, "restaurant": "Food Point"},
    {"name": "Chicken Chowmein Small (Food Point)", "tags": ["quick", "non-veg", "filling", "comfort food"], "price": 70, "restaurant": "Food Point"},
    {"name": "Chicken Chowmein Large (Food Point)", "tags": ["non-veg", "filling", "comfort food", "bold"], "price": 140, "restaurant": "Food Point"},
    {"name": "Egg Chowmein Small (Food Point)", "tags": ["quick", "non-veg", "light", "comfort food"], "price": 70, "restaurant": "Food Point"},
    {"name": "Egg Chowmein Large (Food Point)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 110, "restaurant": "Food Point"},
    {"name": "Spring Roll (Food Point)", "tags": ["crispy", "light", "vegetarian", "snack"], "price": 100, "restaurant": "Food Point"},
 
    # Burgers
    {"name": "Veg Burger (Food Point)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 50, "restaurant": "Food Point"},
    {"name": "Veg Burger with Cheese (Food Point)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 70, "restaurant": "Food Point"},
    {"name": "Chicken Burger (Food Point)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 90, "restaurant": "Food Point"},
    {"name": "Chicken Burger with Cheese (Food Point)", "tags": ["cheesy", "non-veg", "filling", "indulgent"], "price": 110, "restaurant": "Food Point"},
    {"name": "Paneer Burger (Food Point)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 80, "restaurant": "Food Point"},
    {"name": "Aloo Tikki Burger (Food Point)", "tags": ["quick", "budget", "vegetarian", "comfort food"], "price": 45, "restaurant": "Food Point"},
 
    # Sandwiches
    {"name": "Veg Sandwich (Food Point)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 90, "restaurant": "Food Point"},
    {"name": "Veg Club Sandwich (Food Point)", "tags": ["loaded", "vegetarian", "filling", "premium"], "price": 100, "restaurant": "Food Point"},
    {"name": "Egg Sandwich (Food Point)", "tags": ["non-veg", "quick", "light", "budget"], "price": 70, "restaurant": "Food Point"},
    {"name": "Cheese Corn Sandwich (Food Point)", "tags": ["cheesy", "sweet", "filling", "quick"], "price": 120, "restaurant": "Food Point"},
    {"name": "Mushroom Sandwich (Food Point)", "tags": ["earthy", "vegetarian", "filling", "quick"], "price": 100, "restaurant": "Food Point"},
    {"name": "Paneer Corn Sandwich (Food Point)", "tags": ["high protein", "sweet", "filling", "vegetarian"], "price": 100, "restaurant": "Food Point"},
 
    # Eggs
    {"name": "Plain Omelette (Food Point)", "tags": ["high protein", "simple", "quick", "light"], "price": 40, "restaurant": "Food Point"},
    {"name": "Bread Omelette (Food Point)", "tags": ["high protein", "filling", "quick", "budget"], "price": 50, "restaurant": "Food Point"},
    {"name": "Mushroom Omelette (Food Point)", "tags": ["high protein", "earthy", "filling", "quick"], "price": 50, "restaurant": "Food Point"},
    {"name": "Masala Omelette (Food Point)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 50, "restaurant": "Food Point"},
    {"name": "Boiled Egg (Food Point)", "tags": ["high protein", "simple", "light", "budget"], "price": 30, "restaurant": "Food Point"},
    {"name": "French Toast (Food Point)", "tags": ["sweet", "light", "quick", "breakfast"], "price": 70, "restaurant": "Food Point"},
    {"name": "Egg Bhurji (Food Point)", "tags": ["high protein", "spicy", "quick", "simple"], "price": 50, "restaurant": "Food Point"},
 
    # Breakfast
    {"name": "Plain Prantha (Food Point)", "tags": ["simple", "light", "budget", "home-style"], "price": 25, "restaurant": "Food Point"},
    {"name": "Aloo Prantha (Food Point)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 30, "restaurant": "Food Point"},
    {"name": "Paneer Prantha (Food Point)", "tags": ["filling", "high protein", "comforting", "home-style"], "price": 50, "restaurant": "Food Point"},
    {"name": "Onion Prantha (Food Point)", "tags": ["simple", "comforting", "home-style", "budget"], "price": 35, "restaurant": "Food Point"},
    {"name": "Aloo Pyaz Prantha (Food Point)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 35, "restaurant": "Food Point"},
    {"name": "Egg Prantha (Food Point)", "tags": ["high protein", "filling", "comforting", "non-veg"], "price": 50, "restaurant": "Food Point"},
    {"name": "Gobhi Prantha (Food Point)", "tags": ["filling", "comforting", "home-style", "vegetarian"], "price": 35, "restaurant": "Food Point"},
    {"name": "Butter Toast (Food Point)", "tags": ["simple", "light", "quick", "budget"], "price": 30, "restaurant": "Food Point"},
    {"name": "Poori Bhaji (Food Point)", "tags": ["filling", "spicy", "comfort food", "classic"], "price": 90, "restaurant": "Food Point"},
    {"name": "Channa Bhatura (Food Point)", "tags": ["filling", "energizing", "spicy", "classic"], "price": 100, "restaurant": "Food Point"},
 
    # Pizza & Pasta
    {"name": "Veg Pizza (Food Point)", "tags": ["vegetarian", "cheesy", "filling", "comfort food"], "price": 160, "restaurant": "Food Point"},
    {"name": "Onion Capsicum Pizza (Food Point)", "tags": ["vegetarian", "tangy", "cheesy", "light"], "price": 140, "restaurant": "Food Point"},
    {"name": "Plain Cheese Pizza (Food Point)", "tags": ["classic", "cheesy", "vegetarian", "simple"], "price": 130, "restaurant": "Food Point"},
    {"name": "Cheese & Corn Pizza (Food Point)", "tags": ["cheesy", "sweet", "vegetarian", "light"], "price": 150, "restaurant": "Food Point"},
    {"name": "Paneer Pizza (Food Point)", "tags": ["high protein", "cheesy", "vegetarian", "filling"], "price": 170, "restaurant": "Food Point"},
    {"name": "Chicken Pizza (Food Point)", "tags": ["non-veg", "cheesy", "filling", "bold"], "price": 200, "restaurant": "Food Point"},
    {"name": "Peri-Peri Pizza (Food Point)", "tags": ["spicy", "bold", "cheesy", "filling"], "price": 220, "restaurant": "Food Point"},
    {"name": "White Sauce Pasta Small (Food Point)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 160, "restaurant": "Food Point"},
    {"name": "White Sauce Pasta Large (Food Point)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 200, "restaurant": "Food Point"},
    {"name": "Red Sauce Pasta Small (Food Point)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 150, "restaurant": "Food Point"},
    {"name": "Red Sauce Pasta Large (Food Point)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 200, "restaurant": "Food Point"},
    {"name": "Mixed Sauce Pasta Small (Food Point)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 170, "restaurant": "Food Point"},
    {"name": "Mixed Sauce Pasta Large (Food Point)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 210, "restaurant": "Food Point"},
 
    # Soup
    {"name": "Veg Soup (Food Point)", "tags": ["warm", "light", "healthy", "soup"], "price": 50, "restaurant": "Food Point"},
    {"name": "Hot & Sour Soup (Food Point)", "tags": ["warm", "tangy", "spicy", "soup"], "price": 45, "restaurant": "Food Point"},
    {"name": "Sweet Corn Soup (Food Point)", "tags": ["warm", "sweet", "light", "soup"], "price": 50, "restaurant": "Food Point"},
    {"name": "Veg Manchow Soup (Food Point)", "tags": ["warm", "spicy", "light", "soup"], "price": 50, "restaurant": "Food Point"},
    {"name": "Chicken Soup (Food Point)", "tags": ["warm", "non-veg", "light", "comforting"], "price": 70, "restaurant": "Food Point"},
    {"name": "Egg Soup (Food Point)", "tags": ["warm", "non-veg", "light", "simple"], "price": 50, "restaurant": "Food Point"},
 
 
    # ─── 4. Chaudhary Juice Corner ────────────────────────────────────────────
 
    # Shakes (Small / Medium / Large)
    {"name": "Banana Shake Small (CJC)", "tags": ["cold", "filling", "energizing", "high protein"], "price": 50, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Banana Shake Medium (CJC)", "tags": ["cold", "filling", "energizing", "high protein"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Banana Shake Large (CJC)", "tags": ["cold", "filling", "energizing", "high protein"], "price": 80, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mango Shake Small (CJC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 50, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mango Shake Medium (CJC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mango Shake Large (CJC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 80, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Butterscotch Shake Small (CJC)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Butterscotch Shake Medium (CJC)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Butterscotch Shake Large (CJC)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Strawberry Shake Small (CJC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Strawberry Shake Medium (CJC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Strawberry Shake Large (CJC)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Chocolate Shake Small (CJC)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Chocolate Shake Medium (CJC)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Chocolate Shake Large (CJC)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Kiwi Shake Small (CJC)", "tags": ["cold", "fruity", "tangy", "refreshing"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Kiwi Shake Medium (CJC)", "tags": ["cold", "fruity", "tangy", "refreshing"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Kiwi Shake Large (CJC)", "tags": ["cold", "fruity", "tangy", "refreshing"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Guava Shake Small (CJC)", "tags": ["cold", "fruity", "tangy", "refreshing"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Guava Shake Medium (CJC)", "tags": ["cold", "fruity", "tangy", "refreshing"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Guava Shake Large (CJC)", "tags": ["cold", "fruity", "tangy", "refreshing"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Black Currant Shake Small (CJC)", "tags": ["cold", "fruity", "unique", "sweet"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Black Currant Shake Medium (CJC)", "tags": ["cold", "fruity", "unique", "sweet"], "price": 80, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Black Currant Shake Large (CJC)", "tags": ["cold", "fruity", "unique", "sweet"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Blueberry Shake Small (CJC)", "tags": ["cold", "fruity", "antioxidant", "sweet"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Blueberry Shake Medium (CJC)", "tags": ["cold", "fruity", "antioxidant", "sweet"], "price": 80, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Blueberry Shake Large (CJC)", "tags": ["cold", "fruity", "antioxidant", "sweet"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Chiku Shake Small (CJC)", "tags": ["cold", "fruity", "sweet", "unique"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Chiku Shake Medium (CJC)", "tags": ["cold", "fruity", "sweet", "unique"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Chiku Shake Large (CJC)", "tags": ["cold", "fruity", "sweet", "unique"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Papaya Shake Small (CJC)", "tags": ["cold", "fruity", "healthy", "light"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Papaya Shake Medium (CJC)", "tags": ["cold", "fruity", "healthy", "light"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Papaya Shake Large (CJC)", "tags": ["cold", "fruity", "healthy", "light"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Oreo Shake Small (CJC)", "tags": ["cold", "sweet", "indulgent", "fun"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Oreo Shake Medium (CJC)", "tags": ["cold", "sweet", "indulgent", "fun"], "price": 70, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Oreo Shake Large (CJC)", "tags": ["cold", "sweet", "indulgent", "fun"], "price": 90, "restaurant": "Chaudhary Juice Corner"},
 
    # Juice (Small / Medium / Large)
    {"name": "Mosambi Juice Small (CJC)", "tags": ["cold", "citrus", "refreshing", "healthy"], "price": 50, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mosambi Juice Medium (CJC)", "tags": ["cold", "citrus", "refreshing", "healthy"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mosambi Juice Large (CJC)", "tags": ["cold", "citrus", "refreshing", "healthy"], "price": 80, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mix Fruit Juice Small (CJC)", "tags": ["cold", "fruity", "refreshing", "healthy"], "price": 50, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mix Fruit Juice Medium (CJC)", "tags": ["cold", "fruity", "refreshing", "healthy"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mix Fruit Juice Large (CJC)", "tags": ["cold", "fruity", "refreshing", "healthy"], "price": 80, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mix Vegetable Juice Small (CJC)", "tags": ["cold", "healthy", "light", "vegetarian"], "price": 50, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mix Vegetable Juice Medium (CJC)", "tags": ["cold", "healthy", "light", "vegetarian"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Mix Vegetable Juice Large (CJC)", "tags": ["cold", "healthy", "light", "vegetarian"], "price": 20, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Pomegranate Juice Small (CJC)", "tags": ["cold", "antioxidant", "healthy", "refreshing"], "price": 80, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Pomegranate Juice Medium (CJC)", "tags": ["cold", "antioxidant", "healthy", "refreshing"], "price": 100, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Pomegranate Juice Large (CJC)", "tags": ["cold", "antioxidant", "healthy", "premium"], "price": 120, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Orange Juice Small (CJC)", "tags": ["cold", "citrus", "refreshing", "healthy"], "price": 50, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Orange Juice Medium (CJC)", "tags": ["cold", "citrus", "refreshing", "healthy"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Orange Juice Large (CJC)", "tags": ["cold", "citrus", "refreshing", "healthy"], "price": 20, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Carrot Juice Small (CJC)", "tags": ["cold", "healthy", "light", "vegetarian"], "price": 40, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Carrot Juice Medium (CJC)", "tags": ["cold", "healthy", "light", "vegetarian"], "price": 50, "restaurant": "Chaudhary Juice Corner"},
    {"name": "Carrot Juice Large (CJC)", "tags": ["cold", "healthy", "light", "vegetarian"], "price": 60, "restaurant": "Chaudhary Juice Corner"},
 
 
    # ─── 5. Mishti ────────────────────────────────────────────────────────────
 
    # Thali
    {"name": "Normal Thali (Mishti)", "tags": ["balanced", "simple", "filling", "budget"], "price": 90, "restaurant": "Mishti"},
    {"name": "Special Veg Thali (Mishti)", "tags": ["balanced", "vegetarian", "premium", "variety"], "price": 170, "restaurant": "Mishti"},
    {"name": "Special Non Veg Thali (Mishti)", "tags": ["balanced", "non-veg", "premium", "variety"], "price": 200, "restaurant": "Mishti"},
 
    # Main Course Non-Veg (Half)
    {"name": "Chicken Curry Half (Mishti)", "tags": ["spicy", "non-veg", "comforting", "filling"], "price": 250, "restaurant": "Mishti"},
    {"name": "Kadai Chicken Half (Mishti)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 250, "restaurant": "Mishti"},
    {"name": "Chicken Masala Half (Mishti)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 250, "restaurant": "Mishti"},
    {"name": "Chicken Handi Half (Mishti)", "tags": ["rich", "non-veg", "comforting", "filling"], "price": 260, "restaurant": "Mishti"},
    {"name": "Butter Chicken Half (Mishti)", "tags": ["creamy", "non-veg", "rich", "comforting"], "price": 270, "restaurant": "Mishti"},
    {"name": "Lemon Chicken Half (Mishti)", "tags": ["tangy", "non-veg", "refreshing", "light"], "price": 220, "restaurant": "Mishti"},
    {"name": "Chicken do Pyaza Half (Mishti)", "tags": ["spicy", "non-veg", "onion-rich", "filling"], "price": 260, "restaurant": "Mishti"},
    {"name": "Rahra Chicken Half (Mishti)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 260, "restaurant": "Mishti"},
 
    # Main Course Non-Veg (Full)
    {"name": "Chicken Curry Full (Mishti)", "tags": ["spicy", "non-veg", "comforting", "sharing"], "price": 470, "restaurant": "Mishti"},
    {"name": "Kadai Chicken Full (Mishti)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 480, "restaurant": "Mishti"},
    {"name": "Chicken Masala Full (Mishti)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 480, "restaurant": "Mishti"},
    {"name": "Chicken Handi Full (Mishti)", "tags": ["rich", "non-veg", "comforting", "sharing"], "price": 490, "restaurant": "Mishti"},
    {"name": "Butter Chicken Full (Mishti)", "tags": ["creamy", "non-veg", "rich", "sharing"], "price": 490, "restaurant": "Mishti"},
    {"name": "Lemon Chicken Full (Mishti)", "tags": ["tangy", "non-veg", "refreshing", "sharing"], "price": 400, "restaurant": "Mishti"},
    {"name": "Chicken do Pyaza Full (Mishti)", "tags": ["spicy", "non-veg", "onion-rich", "sharing"], "price": 490, "restaurant": "Mishti"},
    {"name": "Rahra Chicken Full (Mishti)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 490, "restaurant": "Mishti"},
 
    # Main Course Veg
    {"name": "Matter Paneer (Mishti)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 180, "restaurant": "Mishti"},
    {"name": "Kadai Paneer (Mishti)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 180, "restaurant": "Mishti"},
    {"name": "Shahi Paneer Small (Mishti)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 190, "restaurant": "Mishti"},
    {"name": "Shahi Paneer Large (Mishti)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 200, "restaurant": "Mishti"},
    {"name": "Paneer Butter Masala (Mishti)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 200, "restaurant": "Mishti"},
    {"name": "Paneer Masala (Mishti)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 180, "restaurant": "Mishti"},
    {"name": "Paneer do Pyaza (Mishti)", "tags": ["spicy", "high protein", "onion-rich", "bold"], "price": 190, "restaurant": "Mishti"},
    {"name": "Rahra Paneer (Mishti)", "tags": ["spicy", "high protein", "bold", "filling"], "price": 180, "restaurant": "Mishti"},
    {"name": "Paneer Tomato (Mishti)", "tags": ["tangy", "high protein", "vegetarian", "light"], "price": 170, "restaurant": "Mishti"},
    {"name": "Paneer Bhurji Small (Mishti)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 120, "restaurant": "Mishti"},
    {"name": "Paneer Bhurji Large (Mishti)", "tags": ["high protein", "spicy", "filling", "bold"], "price": 220, "restaurant": "Mishti"},
    {"name": "Palak Paneer (Mishti)", "tags": ["healthy", "high protein", "vegetarian", "comforting"], "price": 190, "restaurant": "Mishti"},
    {"name": "Veg Kofta (Mishti)", "tags": ["rich", "vegetarian", "indulgent", "filling"], "price": 160, "restaurant": "Mishti"},
    {"name": "Malai Kofta (Mishti)", "tags": ["rich", "creamy", "vegetarian", "indulgent"], "price": 200, "restaurant": "Mishti"},
    {"name": "Paneer Makki Masala (Mishti)", "tags": ["spicy", "high protein", "unique", "filling"], "price": 180, "restaurant": "Mishti"},
    {"name": "Dal Yellow (Mishti)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 120, "restaurant": "Mishti"},
    {"name": "Dal Mix (Mishti)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 100, "restaurant": "Mishti"},
    {"name": "Rajmah Masala (Mishti)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 130, "restaurant": "Mishti"},
    {"name": "Chana Masala (Mishti)", "tags": ["spicy", "filling", "vegetarian", "bold"], "price": 130, "restaurant": "Mishti"},
    {"name": "Dal Makhani (Mishti)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 140, "restaurant": "Mishti"},
    {"name": "Mix Veg (Mishti)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 130, "restaurant": "Mishti"},
    {"name": "Jeera Aaloo (Mishti)", "tags": ["simple", "comforting", "home-style", "light"], "price": 90, "restaurant": "Mishti"},
    {"name": "Masala Chaap (Mishti)", "tags": ["spicy", "smoky", "vegetarian", "filling"], "price": 180, "restaurant": "Mishti"},
    {"name": "Malai Chaap (Mishti)", "tags": ["creamy", "smoky", "vegetarian", "filling"], "price": 200, "restaurant": "Mishti"},
 
    # Continental Snacks
    {"name": "Red Sauce Pasta (Mishti)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 130, "restaurant": "Mishti"},
    {"name": "White Sauce Pasta (Mishti)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 140, "restaurant": "Mishti"},
    {"name": "Mix Sauce Pasta (Mishti)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 150, "restaurant": "Mishti"},
    {"name": "Veg Macaroni (Mishti)", "tags": ["light", "vegetarian", "quick", "comfort food"], "price": 90, "restaurant": "Mishti"},
    {"name": "Paneer Macaroni (Mishti)", "tags": ["high protein", "filling", "vegetarian", "comfort food"], "price": 120, "restaurant": "Mishti"},
    {"name": "Cheese Macaroni (Mishti)", "tags": ["cheesy", "indulgent", "comfort food", "quick"], "price": 120, "restaurant": "Mishti"},
    {"name": "Egg Macaroni (Mishti)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 120, "restaurant": "Mishti"},
    {"name": "Veg Chowmein (Mishti)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 90, "restaurant": "Mishti"},
    {"name": "Hakka Chowmein (Mishti)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 100, "restaurant": "Mishti"},
    {"name": "Non-Veg Hakka Chowmein (Mishti)", "tags": ["quick", "non-veg", "filling", "comfort food"], "price": 130, "restaurant": "Mishti"},
    {"name": "Veg Singapuri (Mishti)", "tags": ["spicy", "unique", "vegetarian", "filling"], "price": 100, "restaurant": "Mishti"},
    {"name": "Non-Veg Singapuri (Mishti)", "tags": ["spicy", "unique", "non-veg", "filling"], "price": 130, "restaurant": "Mishti"},
    {"name": "Garlic Chowmein (Mishti)", "tags": ["savory", "bold", "vegetarian", "quick"], "price": 100, "restaurant": "Mishti"},
 
    # Burgers
    {"name": "Veg Burger (Mishti)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 50, "restaurant": "Mishti"},
    {"name": "Double Tikki Burger (Mishti)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 65, "restaurant": "Mishti"},
    {"name": "Aaloo Tikki Burger (Mishti)", "tags": ["quick", "budget", "vegetarian", "comfort food"], "price": 40, "restaurant": "Mishti"},
    {"name": "Cheese Burger (Mishti)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 70, "restaurant": "Mishti"},
    {"name": "Paneer Burger (Mishti)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 70, "restaurant": "Mishti"},
    {"name": "Chicken Burger (Mishti)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 90, "restaurant": "Mishti"},
 
    # Snacks
    {"name": "Fried Chicken Half (Mishti)", "tags": ["crispy", "non-veg", "filling", "bold"], "price": 250, "restaurant": "Mishti"},
    {"name": "Fried Chicken Full (Mishti)", "tags": ["crispy", "non-veg", "filling", "sharing"], "price": 480, "restaurant": "Mishti"},
    {"name": "Chilly Paneer (Mishti)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 190, "restaurant": "Mishti"},
    {"name": "Veg Manchurian (Mishti)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 130, "restaurant": "Mishti"},
    {"name": "Chilly Chicken Half (Mishti)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 250, "restaurant": "Mishti"},
    {"name": "Chilly Chicken Full (Mishti)", "tags": ["spicy", "non-veg", "bold", "sharing"], "price": 480, "restaurant": "Mishti"},
    {"name": "Honey Chilly Potato (Mishti)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 140, "restaurant": "Mishti"},
    {"name": "Crispy Corn (Mishti)", "tags": ["crispy", "light", "snack", "vegetarian"], "price": 120, "restaurant": "Mishti"},
    {"name": "Veg Momos (Mishti)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 90, "restaurant": "Mishti"},
    {"name": "Veg Fried Momos (Mishti)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 100, "restaurant": "Mishti"},
    {"name": "Chicken Momos (Mishti)", "tags": ["non-veg", "light", "steamed", "snack"], "price": 130, "restaurant": "Mishti"},
    {"name": "Chana Chat (Mishti)", "tags": ["tangy", "spicy", "street food", "snack"], "price": 100, "restaurant": "Mishti"},
    {"name": "Plain Maggi (Mishti)", "tags": ["quick", "simple", "comfort food", "budget"], "price": 30, "restaurant": "Mishti"},
    {"name": "Masala Maggi (Mishti)", "tags": ["spicy", "quick", "comfort food", "bold"], "price": 50, "restaurant": "Mishti"},
    {"name": "Veg Pakora (Mishti)", "tags": ["crispy", "warm", "vegetarian", "snack"], "price": 120, "restaurant": "Mishti"},
    {"name": "Paneer Pakora (Mishti)", "tags": ["crispy", "high protein", "warm", "snack"], "price": 150, "restaurant": "Mishti"},
    {"name": "Egg Maggi (Mishti)", "tags": ["non-veg", "quick", "comfort food", "simple"], "price": 60, "restaurant": "Mishti"},
    {"name": "Chicken Maggi (Mishti)", "tags": ["non-veg", "quick", "comfort food", "filling"], "price": 80, "restaurant": "Mishti"},
    {"name": "Veg Maggi (Mishti)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 50, "restaurant": "Mishti"},
    {"name": "Paneer Maggi (Mishti)", "tags": ["high protein", "quick", "vegetarian", "comfort food"], "price": 60, "restaurant": "Mishti"},
    {"name": "Veg Roll (Mishti)", "tags": ["quick", "light", "vegetarian", "snack"], "price": 50, "restaurant": "Mishti"},
    {"name": "Egg Roll (Mishti)", "tags": ["non-veg", "quick", "light", "snack"], "price": 70, "restaurant": "Mishti"},
    {"name": "Chicken Roll (Mishti)", "tags": ["non-veg", "filling", "spicy", "quick"], "price": 100, "restaurant": "Mishti"},
    {"name": "Paneer Roll (Mishti)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 70, "restaurant": "Mishti"},
    {"name": "French Fries (Mishti)", "tags": ["crispy", "snack", "quick", "comfort food"], "price": 100, "restaurant": "Mishti"},
    {"name": "Chicken Tikka Half (Mishti)", "tags": ["non-veg", "grilled", "spicy", "filling"], "price": 250, "restaurant": "Mishti"},
    {"name": "Chicken Tikka Full (Mishti)", "tags": ["non-veg", "grilled", "spicy", "sharing"], "price": 500, "restaurant": "Mishti"},
    {"name": "Paneer Tikka Half (Mishti)", "tags": ["high protein", "grilled", "vegetarian", "smoky"], "price": 200, "restaurant": "Mishti"},
    {"name": "Paneer Tikka Full (Mishti)", "tags": ["high protein", "grilled", "vegetarian", "smoky"], "price": 400, "restaurant": "Mishti"},
    {"name": "Chicken Nuggets (Mishti)", "tags": ["crispy", "non-veg", "snack", "quick"], "price": 120, "restaurant": "Mishti"},
 
    # Breakfast
    {"name": "Normal Tea (Mishti)", "tags": ["warm", "simple", "comforting", "budget"], "price": 20, "restaurant": "Mishti"},
    {"name": "Special Tea (Mishti)", "tags": ["warm", "aromatic", "comforting", "premium"], "price": 30, "restaurant": "Mishti"},
    {"name": "Coffee (Mishti)", "tags": ["warm", "energizing", "simple", "comforting"], "price": 35, "restaurant": "Mishti"},
    {"name": "Cold Coffee (Mishti)", "tags": ["cold", "energizing", "refreshing", "classic"], "price": 60, "restaurant": "Mishti"},
    {"name": "Butter Toast (Mishti)", "tags": ["simple", "light", "quick", "budget"], "price": 40, "restaurant": "Mishti"},
    {"name": "Jam Toast (Mishti)", "tags": ["sweet", "light", "quick", "simple"], "price": 50, "restaurant": "Mishti"},
    {"name": "Veg Sandwich (Mishti)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 50, "restaurant": "Mishti"},
    {"name": "Egg Toast (Mishti)", "tags": ["high protein", "light", "quick", "simple"], "price": 50, "restaurant": "Mishti"},
    {"name": "Chicken Sandwich (Mishti)", "tags": ["non-veg", "filling", "high protein", "quick"], "price": 60, "restaurant": "Mishti"},
    {"name": "Masala Omelette (Mishti)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 40, "restaurant": "Mishti"},
    {"name": "Tomato Omelette (Mishti)", "tags": ["high protein", "tangy", "quick", "light"], "price": 40, "restaurant": "Mishti"},
    {"name": "Plain Omelette (Mishti)", "tags": ["high protein", "simple", "quick", "light"], "price": 30, "restaurant": "Mishti"},
    {"name": "Bread Omelet (Mishti)", "tags": ["high protein", "filling", "quick", "budget"], "price": 50, "restaurant": "Mishti"},
    {"name": "Chana Bhatura (Mishti)", "tags": ["filling", "energizing", "spicy", "classic"], "price": 100, "restaurant": "Mishti"},
    {"name": "Aaloo Puri (Mishti)", "tags": ["filling", "spicy", "comfort food", "classic"], "price": 90, "restaurant": "Mishti"},
    {"name": "Aaloo Parantha (Mishti)", "tags": ["comforting", "filling", "home-style", "budget"], "price": 30, "restaurant": "Mishti"},
    {"name": "Pyaz Parantha (Mishti)", "tags": ["simple", "comforting", "home-style", "budget"], "price": 40, "restaurant": "Mishti"},
    {"name": "Mix Parantha (Mishti)", "tags": ["filling", "variety", "comforting", "home-style"], "price": 45, "restaurant": "Mishti"},
    {"name": "Paneer Parantha (Mishti)", "tags": ["filling", "high protein", "comforting", "home-style"], "price": 50, "restaurant": "Mishti"},
    {"name": "Egg Parantha (Mishti)", "tags": ["high protein", "filling", "comforting", "non-veg"], "price": 60, "restaurant": "Mishti"},
 
 
    # ─── 6. Wonder Hills Cafe ─────────────────────────────────────────────────
 
    # Breakfast
    {"name": "Stuffed Paratha Small (Wonder Hills)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 35, "restaurant": "Wonder Hills Cafe"},
    {"name": "Stuffed Paratha Large (Wonder Hills)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 60, "restaurant": "Wonder Hills Cafe"},
    {"name": "Mix Paratha (Wonder Hills)", "tags": ["filling", "variety", "comforting", "home-style"], "price": 40, "restaurant": "Wonder Hills Cafe"},
    {"name": "Pahadi Paneer Paratha Small (Wonder Hills)", "tags": ["local", "high protein", "filling", "unique"], "price": 70, "restaurant": "Wonder Hills Cafe"},
    {"name": "Pahadi Paneer Paratha Large (Wonder Hills)", "tags": ["local", "high protein", "filling", "premium"], "price": 90, "restaurant": "Wonder Hills Cafe"},
    {"name": "Morning Masti Poha (Wonder Hills)", "tags": ["light", "simple", "quick", "home-style"], "price": 60, "restaurant": "Wonder Hills Cafe"},
    {"name": "Chana Bhatura (Wonder Hills)", "tags": ["filling", "energizing", "spicy", "classic"], "price": 80, "restaurant": "Wonder Hills Cafe"},
    {"name": "Puri Bhaji (Wonder Hills)", "tags": ["filling", "spicy", "comfort food", "classic"], "price": 80, "restaurant": "Wonder Hills Cafe"},
    {"name": "Gobhi Naan (Wonder Hills)", "tags": ["filling", "comforting", "warm", "vegetarian"], "price": 130, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Naan (Wonder Hills)", "tags": ["filling", "high protein", "warm", "soft"], "price": 130, "restaurant": "Wonder Hills Cafe"},
    {"name": "Aloo Naan (Wonder Hills)", "tags": ["filling", "comforting", "warm", "soft"], "price": 100, "restaurant": "Wonder Hills Cafe"},
 
    # Beverages
    {"name": "Tea (Wonder Hills)", "tags": ["warm", "simple", "light", "budget"], "price": 15, "restaurant": "Wonder Hills Cafe"},
    {"name": "Masala Tea (Wonder Hills)", "tags": ["warm", "spicy", "comforting", "budget"], "price": 20, "restaurant": "Wonder Hills Cafe"},
    {"name": "Green Tea (Wonder Hills)", "tags": ["warm", "healthy", "light", "refreshing"], "price": 20, "restaurant": "Wonder Hills Cafe"},
    {"name": "Lemon Tea (Wonder Hills)", "tags": ["warm", "tangy", "refreshing", "light"], "price": 20, "restaurant": "Wonder Hills Cafe"},
    {"name": "Cappuccino (Wonder Hills)", "tags": ["warm", "frothy", "comforting", "classic"], "price": 50, "restaurant": "Wonder Hills Cafe"},
    {"name": "Cold Coffee Breeze (Wonder Hills)", "tags": ["cold", "energizing", "refreshing", "classic"], "price": 80, "restaurant": "Wonder Hills Cafe"},
    {"name": "Virgin Mojito Zest (Wonder Hills)", "tags": ["cold", "refreshing", "minty", "light"], "price": 70, "restaurant": "Wonder Hills Cafe"},
 
    # Fried Treats
    {"name": "French Fries (Wonder Hills)", "tags": ["crispy", "snack", "quick", "comfort food"], "price": 90, "restaurant": "Wonder Hills Cafe"},
    {"name": "Cheesy Fingers (Wonder Hills)", "tags": ["cheesy", "crispy", "snack", "indulgent"], "price": 100, "restaurant": "Wonder Hills Cafe"},
    {"name": "Spring Roll Crisp (Wonder Hills)", "tags": ["crispy", "light", "vegetarian", "snack"], "price": 80, "restaurant": "Wonder Hills Cafe"},
    {"name": "Cheese Corn Roll (Wonder Hills)", "tags": ["cheesy", "sweet", "crispy", "snack"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Cheese Garlic Toast (Wonder Hills)", "tags": ["cheesy", "savory", "warm", "quick"], "price": 100, "restaurant": "Wonder Hills Cafe"},
    {"name": "Veg Fried Momos (Wonder Hills)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Fried Momos (Wonder Hills)", "tags": ["crispy", "high protein", "vegetarian", "snack"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Crispy Corn Pop (Wonder Hills)", "tags": ["crispy", "light", "snack", "vegetarian"], "price": 140, "restaurant": "Wonder Hills Cafe"},
 
    # Indian Main Course
    {"name": "Dal Makhani (Wonder Hills)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 180, "restaurant": "Wonder Hills Cafe"},
    {"name": "Yellow Dal Tadka (Wonder Hills)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 160, "restaurant": "Wonder Hills Cafe"},
    {"name": "Kadhai Paneer Special (Wonder Hills)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 200, "restaurant": "Wonder Hills Cafe"},
    {"name": "Royal Shahi Paneer (Wonder Hills)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 220, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Lababdar (Wonder Hills)", "tags": ["rich", "high protein", "indulgent", "creamy"], "price": 210, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Butter Masala (Wonder Hills)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 200, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Bhurji (Wonder Hills)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 230, "restaurant": "Wonder Hills Cafe"},
    {"name": "Matar Paneer Homestyle (Wonder Hills)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 200, "restaurant": "Wonder Hills Cafe"},
    {"name": "Jeera Aloo (Wonder Hills)", "tags": ["simple", "comforting", "home-style", "light"], "price": 110, "restaurant": "Wonder Hills Cafe"},
    {"name": "Mix Veg (Wonder Hills)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 170, "restaurant": "Wonder Hills Cafe"},
    {"name": "Aloo Matar (Wonder Hills)", "tags": ["comforting", "simple", "vegetarian", "home-style"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Punjabi Chana Masala (Wonder Hills)", "tags": ["spicy", "filling", "vegetarian", "bold"], "price": 150, "restaurant": "Wonder Hills Cafe"},
    {"name": "Rajma Homestyle (Wonder Hills)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 150, "restaurant": "Wonder Hills Cafe"},
    {"name": "Amritsari Chhole (Wonder Hills)", "tags": ["spicy", "bold", "filling", "classic"], "price": 150, "restaurant": "Wonder Hills Cafe"},
    {"name": "Cheese Tomato (Wonder Hills)", "tags": ["cheesy", "tangy", "vegetarian", "comfort food"], "price": 200, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Makhni (Wonder Hills)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 220, "restaurant": "Wonder Hills Cafe"},
 
    # Pizzas
    {"name": "Margherita Magic Pizza (Wonder Hills)", "tags": ["classic", "cheesy", "vegetarian", "light"], "price": 119, "restaurant": "Wonder Hills Cafe"},
    {"name": "Corn Crunch Pizza (Wonder Hills)", "tags": ["cheesy", "sweet", "vegetarian", "light"], "price": 149, "restaurant": "Wonder Hills Cafe"},
    {"name": "Classic Veg Delight Pizza (Wonder Hills)", "tags": ["vegetarian", "cheesy", "filling", "comfort food"], "price": 179, "restaurant": "Wonder Hills Cafe"},
    {"name": "Farmhouse Feast Pizza (Wonder Hills)", "tags": ["loaded", "vegetarian", "filling", "indulgent"], "price": 199, "restaurant": "Wonder Hills Cafe"},
    {"name": "Mushroom Medley Pizza (Wonder Hills)", "tags": ["earthy", "vegetarian", "cheesy", "filling"], "price": 199, "restaurant": "Wonder Hills Cafe"},
    {"name": "Himalayan Paneer Delight Pizza (Wonder Hills)", "tags": ["local", "high protein", "cheesy", "premium"], "price": 249, "restaurant": "Wonder Hills Cafe"},
 
    # Chinese
    {"name": "Veg Hakka Noodles Small (Wonder Hills)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 60, "restaurant": "Wonder Hills Cafe"},
    {"name": "Veg Hakka Noodles Large (Wonder Hills)", "tags": ["quick", "vegetarian", "filling", "comfort food"], "price": 90, "restaurant": "Wonder Hills Cafe"},
    {"name": "Chilli Garlic Noodles Small (Wonder Hills)", "tags": ["spicy", "bold", "vegetarian", "quick"], "price": 70, "restaurant": "Wonder Hills Cafe"},
    {"name": "Chilli Garlic Noodles Large (Wonder Hills)", "tags": ["spicy", "bold", "vegetarian", "filling"], "price": 100, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Hakka Noodles Small (Wonder Hills)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 80, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Hakka Noodles Large (Wonder Hills)", "tags": ["filling", "high protein", "vegetarian", "comfort food"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Veg Fried Rice Small (Wonder Hills)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 70, "restaurant": "Wonder Hills Cafe"},
    {"name": "Veg Fried Rice Large (Wonder Hills)", "tags": ["filling", "vegetarian", "comfort food", "sharing"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Chilli Garlic Fried Rice Small (Wonder Hills)", "tags": ["spicy", "savory", "vegetarian", "quick"], "price": 70, "restaurant": "Wonder Hills Cafe"},
    {"name": "Chilli Garlic Fried Rice Large (Wonder Hills)", "tags": ["spicy", "savory", "vegetarian", "filling"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Chilli Paneer (Wonder Hills)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 200, "restaurant": "Wonder Hills Cafe"},
    {"name": "Veg Manchurian (Wonder Hills)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 150, "restaurant": "Wonder Hills Cafe"},
    {"name": "Honey Chilli Cauliflower (Wonder Hills)", "tags": ["sweet", "spicy", "vegetarian", "snack"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Classic Chilli Potato (Wonder Hills)", "tags": ["spicy", "crispy", "snack", "bold"], "price": 100, "restaurant": "Wonder Hills Cafe"},
    {"name": "Honey Chilli Potato Bliss (Wonder Hills)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 110, "restaurant": "Wonder Hills Cafe"},
    {"name": "Chilli Mushroom (Wonder Hills)", "tags": ["spicy", "earthy", "vegetarian", "bold"], "price": 170, "restaurant": "Wonder Hills Cafe"},
    {"name": "Crispy Chaap (Wonder Hills)", "tags": ["crispy", "vegetarian", "snack", "bold"], "price": 150, "restaurant": "Wonder Hills Cafe"},
 
    # Momo Mania
    {"name": "Veg Steamed Momos (Wonder Hills)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 80, "restaurant": "Wonder Hills Cafe"},
    {"name": "Paneer Momos (Wonder Hills)", "tags": ["filling", "high protein", "vegetarian", "snack"], "price": 100, "restaurant": "Wonder Hills Cafe"},
    {"name": "Spicy Chilli Momos (Wonder Hills)", "tags": ["spicy", "vegetarian", "bold", "snack"], "price": 100, "restaurant": "Wonder Hills Cafe"},
    {"name": "Creamy Dream Momos (Wonder Hills)", "tags": ["creamy", "vegetarian", "unique", "snack"], "price": 110, "restaurant": "Wonder Hills Cafe"},
    {"name": "Saucy Momos (Wonder Hills)", "tags": ["saucy", "spicy", "vegetarian", "snack"], "price": 120, "restaurant": "Wonder Hills Cafe"},
    {"name": "Kurkure Momos (Wonder Hills)", "tags": ["crispy", "crunchy", "vegetarian", "snack"], "price": 150, "restaurant": "Wonder Hills Cafe"},
 
    # Thali
    {"name": "Regular Hill Thali (Wonder Hills)", "tags": ["balanced", "local", "filling", "variety"], "price": 199, "restaurant": "Wonder Hills Cafe"},
    {"name": "Special Wonder Thali (Wonder Hills)", "tags": ["balanced", "premium", "filling", "variety"], "price": 150, "restaurant": "Wonder Hills Cafe"},
 
 
    # ─── 7. Pizza Town ────────────────────────────────────────────────────────
 
    # Burgers
    {"name": "Aloo Tikki Burger (Pizza Town)", "tags": ["quick", "budget", "vegetarian", "comfort food"], "price": 39, "restaurant": "Pizza Town"},
    {"name": "Veggie Burger (Pizza Town)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 45, "restaurant": "Pizza Town"},
    {"name": "Pub Ji Burger (Pizza Town)", "tags": ["filling", "vegetarian", "unique", "quick"], "price": 55, "restaurant": "Pizza Town"},
    {"name": "Cheesy Burger (Pizza Town)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 60, "restaurant": "Pizza Town"},
    {"name": "Cheesy Spicy Burger (Pizza Town)", "tags": ["cheesy", "spicy", "vegetarian", "bold"], "price": 65, "restaurant": "Pizza Town"},
    {"name": "Paneer Burger (Pizza Town)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 70, "restaurant": "Pizza Town"},
    {"name": "Maharaja Burger (Pizza Town)", "tags": ["filling", "loaded", "vegetarian", "indulgent"], "price": 150, "restaurant": "Pizza Town"},
    {"name": "Chicken Burger (Pizza Town)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 90, "restaurant": "Pizza Town"},
    {"name": "Peri Peri Burger (Pizza Town)", "tags": ["spicy", "bold", "filling", "quick"], "price": 165, "restaurant": "Pizza Town"},
    {"name": "BBQ Burger (Pizza Town)", "tags": ["smoky", "bold", "filling", "savory"], "price": 115, "restaurant": "Pizza Town"},
 
    # Pasta
    {"name": "Red Sauce Pasta (Pizza Town)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 100, "restaurant": "Pizza Town"},
    {"name": "White Sauce Pasta (Pizza Town)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 100, "restaurant": "Pizza Town"},
    {"name": "Tandoori Pasta (Pizza Town)", "tags": ["spicy", "smoky", "vegetarian", "unique"], "price": 110, "restaurant": "Pizza Town"},
    {"name": "Jumbo Pasta (Pizza Town)", "tags": ["filling", "indulgent", "vegetarian", "comfort food"], "price": 120, "restaurant": "Pizza Town"},
    {"name": "Makhani Pasta (Pizza Town)", "tags": ["rich", "creamy", "vegetarian", "indulgent"], "price": 130, "restaurant": "Pizza Town"},
    {"name": "White Sauce Chicken Pasta (Pizza Town)", "tags": ["creamy", "non-veg", "filling", "comfort food"], "price": 139, "restaurant": "Pizza Town"},
    {"name": "Red Sauce Chicken Pasta (Pizza Town)", "tags": ["tangy", "non-veg", "filling", "comfort food"], "price": 139, "restaurant": "Pizza Town"},
    {"name": "Tandoori Chicken Pasta (Pizza Town)", "tags": ["spicy", "non-veg", "smoky", "filling"], "price": 149, "restaurant": "Pizza Town"},
 
    # Pizzas Veg
    {"name": "Margherita Pizza (Pizza Town)", "tags": ["classic", "cheesy", "vegetarian", "light"], "price": 79, "restaurant": "Pizza Town"},
    {"name": "Onion Pizza (Pizza Town)", "tags": ["vegetarian", "cheesy", "simple", "comfort food"], "price": 79, "restaurant": "Pizza Town"},
    {"name": "Capsicum Pizza (Pizza Town)", "tags": ["vegetarian", "cheesy", "light", "comfort food"], "price": 79, "restaurant": "Pizza Town"},
    {"name": "Tomato Pizza (Pizza Town)", "tags": ["vegetarian", "tangy", "light", "classic"], "price": 79, "restaurant": "Pizza Town"},
    {"name": "Corn Pizza (Pizza Town)", "tags": ["vegetarian", "sweet", "cheesy", "light"], "price": 89, "restaurant": "Pizza Town"},
    {"name": "Mushroom Pizza (Pizza Town)", "tags": ["earthy", "vegetarian", "cheesy", "filling"], "price": 90, "restaurant": "Pizza Town"},
    {"name": "Paneer Pizza (Pizza Town)", "tags": ["high protein", "vegetarian", "cheesy", "filling"], "price": 100, "restaurant": "Pizza Town"},
    {"name": "Double Toppings Pizza (Pizza Town)", "tags": ["loaded", "vegetarian", "cheesy", "filling"], "price": 109, "restaurant": "Pizza Town"},
    {"name": "Farm Fresh Pizza (Pizza Town)", "tags": ["loaded", "vegetarian", "fresh", "filling"], "price": 200, "restaurant": "Pizza Town"},
    {"name": "Achari Pizza (Pizza Town)", "tags": ["tangy", "spicy", "vegetarian", "unique"], "price": 119, "restaurant": "Pizza Town"},
    {"name": "Veg Deluxe Pizza (Pizza Town)", "tags": ["loaded", "vegetarian", "indulgent", "premium"], "price": 240, "restaurant": "Pizza Town"},
    {"name": "Mix Veg Pizza (Pizza Town)", "tags": ["loaded", "vegetarian", "filling", "comfort food"], "price": 260, "restaurant": "Pizza Town"},
    {"name": "Veg Supreme Pizza (Pizza Town)", "tags": ["loaded", "vegetarian", "premium", "indulgent"], "price": 300, "restaurant": "Pizza Town"},
 
    # Pizzas Non-Veg
    {"name": "Cheesy Spicy Chicken Pizza (Pizza Town)", "tags": ["cheesy", "spicy", "non-veg", "bold"], "price": 189, "restaurant": "Pizza Town"},
    {"name": "Barbecue Chicken Pizza (Pizza Town)", "tags": ["smoky", "non-veg", "bold", "filling"], "price": 259, "restaurant": "Pizza Town"},
    {"name": "Spicy Murgh Pizza (Pizza Town)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 329, "restaurant": "Pizza Town"},
    {"name": "Spicy Double Chicken Pizza (Pizza Town)", "tags": ["spicy", "non-veg", "loaded", "bold"], "price": 349, "restaurant": "Pizza Town"},
    {"name": "Chicken Paprika Pizza (Pizza Town)", "tags": ["spicy", "non-veg", "filling", "bold"], "price": 349, "restaurant": "Pizza Town"},
    {"name": "Chicken Fiesta Pizza (Pizza Town)", "tags": ["non-veg", "loaded", "filling", "premium"], "price": 369, "restaurant": "Pizza Town"},
    {"name": "Chicken Pepperoni Pizza (Pizza Town)", "tags": ["non-veg", "savory", "classic", "filling"], "price": 369, "restaurant": "Pizza Town"},
    {"name": "Non-Veg Supreme Pizza (Pizza Town)", "tags": ["non-veg", "loaded", "premium", "indulgent"], "price": 449, "restaurant": "Pizza Town"},
 
 
    # ─── 8. Laziz Pizza ───────────────────────────────────────────────────────
 
    # Main Course
    {"name": "Chana Masala (Laziz)", "tags": ["spicy", "filling", "vegetarian", "bold"], "price": 180, "restaurant": "Laziz Pizza"},
    {"name": "Yellow Dal Tadka (Laziz)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 170, "restaurant": "Laziz Pizza"},
    {"name": "Dal Makhani (Laziz)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 200, "restaurant": "Laziz Pizza"},
    {"name": "Paneer Bhurji (Laziz)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 220, "restaurant": "Laziz Pizza"},
    {"name": "Mater Paneer (Laziz)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 240, "restaurant": "Laziz Pizza"},
    {"name": "Kadai Paneer (Laziz)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 230, "restaurant": "Laziz Pizza"},
    {"name": "Shahi Paneer (Laziz)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 250, "restaurant": "Laziz Pizza"},
    {"name": "Paneer Butter Masala (Laziz)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 240, "restaurant": "Laziz Pizza"},
    {"name": "Rajma (Laziz)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 180, "restaurant": "Laziz Pizza"},
 
    # Chinese
    {"name": "Noodles Small (Laziz)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 60, "restaurant": "Laziz Pizza"},
    {"name": "Noodles Large (Laziz)", "tags": ["quick", "vegetarian", "filling", "comfort food"], "price": 110, "restaurant": "Laziz Pizza"},
    {"name": "Chilli Garlic Noodles (Laziz)", "tags": ["spicy", "bold", "vegetarian", "quick"], "price": 129, "restaurant": "Laziz Pizza"},
    {"name": "Cheese Noodles (Laziz)", "tags": ["cheesy", "indulgent", "comfort food", "filling"], "price": 139, "restaurant": "Laziz Pizza"},
    {"name": "Hakka Noodles (Laziz)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 139, "restaurant": "Laziz Pizza"},
    {"name": "Honey Chilli Potato (Laziz)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 160, "restaurant": "Laziz Pizza"},
    {"name": "Honey Chilli Cauliflower (Laziz)", "tags": ["sweet", "spicy", "vegetarian", "snack"], "price": 170, "restaurant": "Laziz Pizza"},
    {"name": "Manchurian Small (Laziz)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 140, "restaurant": "Laziz Pizza"},
    {"name": "Manchurian Large (Laziz)", "tags": ["spicy", "vegetarian", "comfort food", "sharing"], "price": 150, "restaurant": "Laziz Pizza"},
    {"name": "Chilli Paneer Small (Laziz)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 200, "restaurant": "Laziz Pizza"},
    {"name": "Chilli Paneer Large (Laziz)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 220, "restaurant": "Laziz Pizza"},
    {"name": "Chicken Noodles (Laziz)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 209, "restaurant": "Laziz Pizza"},
    {"name": "Egg Noodles (Laziz)", "tags": ["non-veg", "quick", "filling", "comfort food"], "price": 189, "restaurant": "Laziz Pizza"},
 
    # Burgers
    {"name": "Veg Fusion Burger Regular (Laziz)", "tags": ["quick", "vegetarian", "simple", "budget"], "price": 85, "restaurant": "Laziz Pizza"},
    {"name": "Veg Fusion Burger Large (Laziz)", "tags": ["filling", "vegetarian", "comfort food", "indulgent"], "price": 105, "restaurant": "Laziz Pizza"},
    {"name": "Peri Peri Paneer Burger Regular (Laziz)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 125, "restaurant": "Laziz Pizza"},
    {"name": "Peri Peri Paneer Burger Large (Laziz)", "tags": ["spicy", "high protein", "vegetarian", "filling"], "price": 145, "restaurant": "Laziz Pizza"},
    {"name": "Fiery Paneer Burger Regular (Laziz)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 145, "restaurant": "Laziz Pizza"},
    {"name": "Fiery Paneer Burger Large (Laziz)", "tags": ["spicy", "high protein", "vegetarian", "filling"], "price": 165, "restaurant": "Laziz Pizza"},
    {"name": "Chicken Burger Regular (Laziz)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 105, "restaurant": "Laziz Pizza"},
    {"name": "Chicken Burger Large (Laziz)", "tags": ["non-veg", "filling", "indulgent", "comfort food"], "price": 125, "restaurant": "Laziz Pizza"},
    {"name": "Peri Peri Chicken Burger Regular (Laziz)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 125, "restaurant": "Laziz Pizza"},
    {"name": "Peri Peri Chicken Burger Large (Laziz)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 145, "restaurant": "Laziz Pizza"},
    {"name": "Fiery Chicken Burger Regular (Laziz)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 145, "restaurant": "Laziz Pizza"},
    {"name": "Fiery Chicken Burger Large (Laziz)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 165, "restaurant": "Laziz Pizza"},
 
 
    # ─── 9. Domino's ──────────────────────────────────────────────────────────
 
    # Pizzas
    {"name": "Burger Pizza Classic Veg (Dominos)", "tags": ["vegetarian", "cheesy", "classic", "comfort food"], "price": 125, "restaurant": "Domino's"},
    {"name": "Burger Pizza Classic Non-Veg (Dominos)", "tags": ["non-veg", "cheesy", "classic", "filling"], "price": 170, "restaurant": "Domino's"},
    {"name": "Burger Pizza Premium Veg (Dominos)", "tags": ["vegetarian", "cheesy", "premium", "filling"], "price": 155, "restaurant": "Domino's"},
    {"name": "Spiced Double Chicken Pizza (Dominos)", "tags": ["spicy", "non-veg", "loaded", "bold"], "price": 330, "restaurant": "Domino's"},
    {"name": "Pepper Barbecue Chicken Pizza (Dominos)", "tags": ["smoky", "non-veg", "bold", "filling"], "price": 260, "restaurant": "Domino's"},
    {"name": "Peppy Paneer Pizza (Dominos)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 280, "restaurant": "Domino's"},
    {"name": "Fresh Veggie Pizza (Dominos)", "tags": ["fresh", "vegetarian", "light", "classic"], "price": 230, "restaurant": "Domino's"},
    {"name": "Indi Chicken Tikka Pizza (Dominos)", "tags": ["spicy", "non-veg", "bold", "premium"], "price": 400, "restaurant": "Domino's"},
    {"name": "Achari Do Pyaza Pizza (Dominos)", "tags": ["tangy", "spicy", "vegetarian", "unique"], "price": 210, "restaurant": "Domino's"},
    {"name": "Corn N Cheese Paratha Pizza (Dominos)", "tags": ["cheesy", "sweet", "vegetarian", "unique"], "price": 210, "restaurant": "Domino's"},
    {"name": "Indi Tandoori Paneer Pizza (Dominos)", "tags": ["spicy", "high protein", "vegetarian", "smoky"], "price": 340, "restaurant": "Domino's"},
 
    # Sides
    {"name": "Veg Parcel (Dominos)", "tags": ["vegetarian", "snack", "quick", "light"], "price": 50, "restaurant": "Domino's"},
    {"name": "Chicken Parcel (Dominos)", "tags": ["non-veg", "snack", "quick", "filling"], "price": 60, "restaurant": "Domino's"},
    {"name": "Garlic Breadsticks (Dominos)", "tags": ["savory", "warm", "light", "classic"], "price": 120, "restaurant": "Domino's"},
    {"name": "Stuffed Garlic Bread (Dominos)", "tags": ["cheesy", "savory", "filling", "indulgent"], "price": 190, "restaurant": "Domino's"},
 
    # Desserts
    {"name": "Choco Lava Cake (Dominos)", "tags": ["sweet", "warm", "indulgent", "dessert"], "price": 110, "restaurant": "Domino's"},
    {"name": "Red Velvet Lava Cake (Dominos)", "tags": ["sweet", "indulgent", "premium", "dessert"], "price": 150, "restaurant": "Domino's"},
    {"name": "Butterscotch Mousse Cake (Dominos)", "tags": ["sweet", "creamy", "indulgent", "dessert"], "price": 105, "restaurant": "Domino's"},
 
 
    # ─── 10. Laxmi Bakers ────────────────────────────────────────────────────
 
    # Cakes (Half kg)
    {"name": "Vanilla Cake Half kg (Laxmi)", "tags": ["sweet", "classic", "dessert", "light"], "price": 350, "restaurant": "Laxmi Bakers"},
    {"name": "Pineapple Cake Half kg (Laxmi)", "tags": ["sweet", "fruity", "dessert", "classic"], "price": 350, "restaurant": "Laxmi Bakers"},
    {"name": "White Forest Cake Half kg (Laxmi)", "tags": ["sweet", "creamy", "premium", "dessert"], "price": 400, "restaurant": "Laxmi Bakers"},
    {"name": "Chocolate Cake Half kg (Laxmi)", "tags": ["sweet", "rich", "indulgent", "dessert"], "price": 350, "restaurant": "Laxmi Bakers"},
    {"name": "Fresh Fruit Cake Half kg (Laxmi)", "tags": ["sweet", "fruity", "fresh", "dessert"], "price": 500, "restaurant": "Laxmi Bakers"},
    {"name": "Truffle Cake Half kg (Laxmi)", "tags": ["sweet", "rich", "premium", "dessert"], "price": 500, "restaurant": "Laxmi Bakers"},
    {"name": "Red Velvet Cake Half kg (Laxmi)", "tags": ["sweet", "indulgent", "premium", "dessert"], "price": 500, "restaurant": "Laxmi Bakers"},
 
    # Cakes (1 kg)
    {"name": "Vanilla Cake 1kg (Laxmi)", "tags": ["sweet", "classic", "dessert", "sharing"], "price": 650, "restaurant": "Laxmi Bakers"},
    {"name": "Pineapple Cake 1kg (Laxmi)", "tags": ["sweet", "fruity", "dessert", "sharing"], "price": 650, "restaurant": "Laxmi Bakers"},
    {"name": "White Forest Cake 1kg (Laxmi)", "tags": ["sweet", "creamy", "premium", "sharing"], "price": 750, "restaurant": "Laxmi Bakers"},
    {"name": "Chocolate Cake 1kg (Laxmi)", "tags": ["sweet", "rich", "indulgent", "sharing"], "price": 700, "restaurant": "Laxmi Bakers"},
    {"name": "Fresh Fruit Cake 1kg (Laxmi)", "tags": ["sweet", "fruity", "fresh", "sharing"], "price": 1000, "restaurant": "Laxmi Bakers"},
    {"name": "Truffle Cake 1kg (Laxmi)", "tags": ["sweet", "rich", "premium", "sharing"], "price": 1000, "restaurant": "Laxmi Bakers"},
    {"name": "Red Velvet Cake 1kg (Laxmi)", "tags": ["sweet", "indulgent", "premium", "sharing"], "price": 1000, "restaurant": "Laxmi Bakers"},
 
    # Patties
    {"name": "Aloo Patty (Laxmi)", "tags": ["crispy", "budget", "snack", "vegetarian"], "price": 20, "restaurant": "Laxmi Bakers"},
    {"name": "Paneer Patty (Laxmi)", "tags": ["crispy", "high protein", "snack", "vegetarian"], "price": 40, "restaurant": "Laxmi Bakers"},
    {"name": "Corn Patty (Laxmi)", "tags": ["crispy", "sweet", "snack", "vegetarian"], "price": 50, "restaurant": "Laxmi Bakers"},
 
    # Burgers
    {"name": "Veg Aloo Patty Burger (Laxmi)", "tags": ["quick", "budget", "vegetarian", "comfort food"], "price": 50, "restaurant": "Laxmi Bakers"},
    {"name": "Double Patty Burger (Laxmi)", "tags": ["filling", "vegetarian", "indulgent", "comfort food"], "price": 80, "restaurant": "Laxmi Bakers"},
    {"name": "Cheese Burger (Laxmi)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 70, "restaurant": "Laxmi Bakers"},
 
    # Momos
    {"name": "Steam Momos (Laxmi)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 80, "restaurant": "Laxmi Bakers"},
    {"name": "Fried Momos (Laxmi)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 100, "restaurant": "Laxmi Bakers"},
    {"name": "Kurkure Momos (Laxmi)", "tags": ["crispy", "crunchy", "vegetarian", "snack"], "price": 120, "restaurant": "Laxmi Bakers"},
    {"name": "Peri-Peri Momos (Laxmi)", "tags": ["spicy", "crispy", "bold", "snack"], "price": 120, "restaurant": "Laxmi Bakers"},
 
    # Pizzas
    {"name": "Kulhad Pizza (Laxmi)", "tags": ["unique", "cheesy", "vegetarian", "rustic"], "price": 100, "restaurant": "Laxmi Bakers"},
    {"name": "Margherita Pizza (Laxmi)", "tags": ["classic", "cheesy", "vegetarian", "light"], "price": 150, "restaurant": "Laxmi Bakers"},
    {"name": "Onion Capsicum Pizza (Laxmi)", "tags": ["vegetarian", "tangy", "cheesy", "light"], "price": 150, "restaurant": "Laxmi Bakers"},
    {"name": "Corn Pizza (Laxmi)", "tags": ["vegetarian", "sweet", "cheesy", "light"], "price": 180, "restaurant": "Laxmi Bakers"},
    
    # ─── 1. Cheers to Chai (C2C) ───────────────────────────────────────────────
 
    # Chai
    {"name": "Adrak Chai", "tags": ["warm", "comforting", "simple", "quick"], "price": 25, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chocolate Chai", "tags": ["warm", "sweet", "indulgent", "comforting"], "price": 25, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Rose Chai", "tags": ["warm", "aromatic", "light", "refreshing"], "price": 25, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Lemon Chai", "tags": ["warm", "tangy", "refreshing", "light"], "price": 25, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Elaichi Chai", "tags": ["warm", "aromatic", "comforting", "classic"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paan Chai", "tags": ["warm", "unique", "aromatic", "refreshing"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Kesar Chai", "tags": ["warm", "aromatic", "premium", "comforting"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Masala Chai", "tags": ["warm", "spicy", "comforting", "energizing"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Tulsi Chai", "tags": ["warm", "herbal", "soothing", "healthy"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
 
    # Coffee
    {"name": "Black Coffee", "tags": ["warm", "bold", "energizing", "simple"], "price": 25, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Coffee", "tags": ["warm", "comforting", "classic", "energizing"], "price": 35, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Strong Coffee", "tags": ["warm", "bold", "energizing", "intense"], "price": 35, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chocolate Coffee", "tags": ["warm", "sweet", "indulgent", "comforting"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Choco Coffee", "tags": ["warm", "sweet", "indulgent", "rich"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Hazelnut Coffee", "tags": ["warm", "aromatic", "premium", "sweet"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
 
    # Cold Drinks
    {"name": "Fresh Lime Water", "tags": ["cold", "refreshing", "light", "tangy"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Fresh Lime Soda", "tags": ["cold", "fizzy", "refreshing", "tangy"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Namkeen Lassi", "tags": ["cold", "salty", "refreshing", "light"], "price": 35, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Sweet Lassi", "tags": ["cold", "sweet", "refreshing", "comforting"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mint Mojito", "tags": ["cold", "refreshing", "minty", "energizing"], "price": 89, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Green Apple Mocktail", "tags": ["cold", "fruity", "refreshing", "sweet"], "price": 89, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Blue Curacao Mocktail", "tags": ["cold", "fruity", "refreshing", "vibrant"], "price": 89, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Pina Colada", "tags": ["cold", "tropical", "sweet", "indulgent"], "price": 149, "restaurant": "Cheers to Chai (C2C)"},
 
    # Cold Coffee
    {"name": "Cold Coffee (C2C)", "tags": ["cold", "energizing", "refreshing", "classic"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chocolate Cold Coffee", "tags": ["cold", "sweet", "indulgent", "energizing"], "price": 90, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Choco Cold Coffee", "tags": ["cold", "sweet", "rich", "indulgent"], "price": 100, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Hazelnut Cold Coffee", "tags": ["cold", "aromatic", "premium", "sweet"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
 
    # Shakes
    {"name": "Oreo Shake (C2C)", "tags": ["cold", "sweet", "indulgent", "filling"], "price": 99, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Banana Shake (C2C)", "tags": ["cold", "filling", "energizing", "high protein"], "price": 59, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chocolate Shake (C2C)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 89, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mango Shake (C2C)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 89, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Vanilla Shake (C2C)", "tags": ["cold", "sweet", "classic", "light"], "price": 89, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Kit Kat Shake", "tags": ["cold", "sweet", "indulgent", "fun"], "price": 89, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Choco Lava Shake", "tags": ["cold", "rich", "indulgent", "sweet"], "price": 99, "restaurant": "Cheers to Chai (C2C)"},
 
    # Sandwiches
    {"name": "Veggie Sandwich (C2C)", "tags": ["quick", "light", "simple", "vegetarian"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Cheese Corn Sandwich", "tags": ["filling", "cheesy", "comforting", "quick"], "price": 60, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Corn Masala Sandwich", "tags": ["spicy", "filling", "vegetarian", "quick"], "price": 60, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Tikka Sandwich", "tags": ["spicy", "filling", "high protein", "grilled"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Corn Mayo Sandwich", "tags": ["creamy", "quick", "light", "comforting"], "price": 60, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Tandoori Sandwich", "tags": ["spicy", "grilled", "filling", "smoky"], "price": 70, "restaurant": "Cheers to Chai (C2C)"},
 
    # Burgers
    {"name": "Aalu Tikki Burger", "tags": ["quick", "filling", "budget", "comforting"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Veg Burger (C2C)", "tags": ["quick", "simple", "filling", "budget"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Veg Paneer Burger", "tags": ["filling", "high protein", "comforting", "quick"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Veg Cheese Burger (C2C)", "tags": ["cheesy", "filling", "indulgent", "quick"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Veg Mexican Burger", "tags": ["spicy", "filling", "bold", "quick"], "price": 90, "restaurant": "Cheers to Chai (C2C)"},
 
    # Pizza
    {"name": "Margherita Pizza (C2C)", "tags": ["classic", "cheesy", "vegetarian", "comfort food"], "price": 119, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Onion Pizza (C2C)", "tags": ["vegetarian", "cheesy", "simple", "comfort food"], "price": 119, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Tomato Pizza", "tags": ["vegetarian", "tangy", "light", "classic"], "price": 119, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Sweet Corn Pizza (C2C)", "tags": ["vegetarian", "sweet", "cheesy", "light"], "price": 119, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Capsicum Pizza", "tags": ["vegetarian", "cheesy", "filling", "comfort food"], "price": 219, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mushroom Pizza (C2C)", "tags": ["vegetarian", "earthy", "cheesy", "filling"], "price": 219, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Farm House Pizza (C2C)", "tags": ["vegetarian", "loaded", "filling", "indulgent"], "price": 279, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Double Cheese Loaded Pizza", "tags": ["cheesy", "indulgent", "filling", "rich"], "price": 319, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Fully Loaded Pizza", "tags": ["loaded", "indulgent", "filling", "variety"], "price": 280, "restaurant": "Cheers to Chai (C2C)"},
 
    # Maggi
    {"name": "Plain Maggi (C2C)", "tags": ["quick", "comfort food", "simple", "budget"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Double Masala Maggi (C2C)", "tags": ["spicy", "quick", "comfort food", "bold"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Vegetable Maggi (C2C)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Cheese Corn Maggi", "tags": ["cheesy", "indulgent", "comfort food", "quick"], "price": 60, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Shezwan Maggi (C2C)", "tags": ["spicy", "bold", "quick", "comfort food"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
 
    # Pasta
    {"name": "Red Sauce Pasta (C2C)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 119, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "White Sauce Pasta (C2C)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 129, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mix Sauce Pasta (C2C)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 149, "restaurant": "Cheers to Chai (C2C)"},
 
    # Chinese
    {"name": "Veg Noodles (C2C)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Dry Manchurian (C2C)", "tags": ["spicy", "crispy", "vegetarian", "snack"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Gravy Manchurian (C2C)", "tags": ["spicy", "saucy", "vegetarian", "comfort food"], "price": 140, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Fried Momos (C2C)", "tags": ["crispy", "snack", "filling", "vegetarian"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Kurkure Momos", "tags": ["crispy", "crunchy", "snack", "indulgent"], "price": 150, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Spring Roll (C2C)", "tags": ["crispy", "snack", "light", "vegetarian"], "price": 100, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Veg Thupka (C2C)", "tags": ["warm", "soupy", "light", "comfort food"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mix Thupka (C2C)", "tags": ["warm", "soupy", "filling", "comfort food"], "price": 100, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Momos (C2C)", "tags": ["filling", "high protein", "snack", "steamed"], "price": 160, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Steamed Momos (C2C)", "tags": ["light", "healthy", "snack", "vegetarian"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Fried Rice (C2C)", "tags": ["filling", "quick", "vegetarian", "comfort food"], "price": 70, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Schezwan Fried Rice (C2C)", "tags": ["spicy", "bold", "filling", "quick"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Fried Rice (C2C)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 90, "restaurant": "Cheers to Chai (C2C)"},
 
    # Snacks
    {"name": "French Fries (C2C)", "tags": ["crispy", "snack", "quick", "comfort food"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Masala Fries (C2C)", "tags": ["spicy", "crispy", "snack", "quick"], "price": 100, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Peri Peri Fries (C2C)", "tags": ["spicy", "crispy", "bold", "snack"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Cheesy Fries (C2C)", "tags": ["cheesy", "indulgent", "snack", "comfort food"], "price": 149, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Fries", "tags": ["high protein", "crispy", "filling", "snack"], "price": 169, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chilli Potato (C2C)", "tags": ["spicy", "crispy", "snack", "bold"], "price": 99, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Honey Chilli Potato (C2C)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chilli Cauliflower (C2C)", "tags": ["spicy", "vegetarian", "crispy", "snack"], "price": 140, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Honey Chilli Cauliflower (C2C)", "tags": ["sweet", "spicy", "vegetarian", "snack"], "price": 160, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chilli Mushroom (C2C)", "tags": ["spicy", "earthy", "vegetarian", "snack"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Cheese Chilli (C2C)", "tags": ["cheesy", "spicy", "indulgent", "snack"], "price": 240, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Crispy Corn (C2C)", "tags": ["crispy", "light", "snack", "vegetarian"], "price": 149, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Cheese Corn Balls", "tags": ["cheesy", "crispy", "snack", "indulgent"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mac & Cheese Balls", "tags": ["cheesy", "indulgent", "snack", "comfort food"], "price": 180, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Roll (C2C)", "tags": ["filling", "high protein", "quick", "snack"], "price": 100, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Nuggets (C2C)", "tags": ["crispy", "high protein", "snack", "filling"], "price": 179, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Veg Roll (C2C)", "tags": ["quick", "light", "vegetarian", "snack"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mix Pakoda (C2C)", "tags": ["crispy", "warm", "comfort food", "snack"], "price": 150, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Pakoda (C2C)", "tags": ["crispy", "high protein", "warm", "snack"], "price": 180, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Bread Pakoda (C2C)", "tags": ["crispy", "budget", "snack", "comfort food"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
 
    # Indian Zaika
    {"name": "Shahi Paneer (C2C)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 280, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Kadhai Paneer (C2C)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 300, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mattar Paneer (C2C)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 240, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Bhurji (C2C)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 300, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mushroom Masala (C2C)", "tags": ["earthy", "spicy", "vegetarian", "filling"], "price": 180, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Dal Makhni (C2C)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 190, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Dal Tadka (C2C)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 190, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Rajmaah (C2C)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 160, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Kadi Pakoda (C2C)", "tags": ["tangy", "comforting", "home-style", "warm"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Chana Masala (C2C)", "tags": ["spicy", "filling", "vegetarian", "bold"], "price": 140, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mix Veg (C2C)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 180, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Jeera Aalu (C2C)", "tags": ["simple", "comforting", "home-style", "light"], "price": 100, "restaurant": "Cheers to Chai (C2C)"},
 
    # Breads & Raita
    {"name": "Aaloo Prantha (C2C)", "tags": ["comforting", "filling", "home-style", "simple"], "price": 30, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Onion Prantha", "tags": ["comforting", "home-style", "simple", "budget"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Aaloo Pyaaz Prantha", "tags": ["comforting", "filling", "home-style", "budget"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Gobhi Prantha (C2C)", "tags": ["comforting", "filling", "home-style", "vegetarian"], "price": 40, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Paneer Prantha (C2C)", "tags": ["filling", "high protein", "comforting", "rich"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mix Prantha (C2C)", "tags": ["filling", "variety", "comforting", "home-style"], "price": 60, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Tawa Roti (C2C)", "tags": ["simple", "light", "budget", "home-style"], "price": 12, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Butter Roti (C2C)", "tags": ["simple", "comforting", "budget", "home-style"], "price": 15, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Curd (C2C)", "tags": ["cooling", "light", "healthy", "simple"], "price": 25, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Boondi Raita (C2C)", "tags": ["cooling", "light", "comforting", "refreshing"], "price": 60, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mix Raita (C2C)", "tags": ["cooling", "light", "refreshing", "healthy"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
 
    # Brunch Specials
    {"name": "Cholle Bhature (C2C)", "tags": ["filling", "energizing", "spicy", "classic"], "price": 100, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Cholle Puri (C2C)", "tags": ["filling", "spicy", "comfort food", "classic"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Aalu Puri (C2C)", "tags": ["filling", "simple", "comfort food", "home-style"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Mix Veg Puri (C2C)", "tags": ["filling", "vegetarian", "comfort food", "home-style"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
 
    # Rice & Combos
    {"name": "Plain Rice (C2C)", "tags": ["simple", "light", "budget", "home-style"], "price": 70, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Jeera Rice (C2C)", "tags": ["light", "aromatic", "simple", "comforting"], "price": 80, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Peas Pulao (C2C)", "tags": ["light", "vegetarian", "aromatic", "balanced"], "price": 120, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Veg Pulao (C2C)", "tags": ["balanced", "vegetarian", "aromatic", "filling"], "price": 140, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Rajma Rice (C2C)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Kadi Chawal (C2C)", "tags": ["tangy", "comforting", "home-style", "filling"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Cholle Rice (C2C)", "tags": ["spicy", "filling", "comforting", "bold"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Dal Rice (C2C)", "tags": ["warm", "comforting", "simple", "home-style"], "price": 50, "restaurant": "Cheers to Chai (C2C)"},
 
    # Thali
    {"name": "Veg Thali (C2C)", "tags": ["balanced", "comforting", "filling", "variety"], "price": 90, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Special Thali (C2C)", "tags": ["balanced", "premium", "filling", "variety"], "price": 150, "restaurant": "Cheers to Chai (C2C)"},
 
    # Desserts
    {"name": "Chocolate Ice Cream (C2C)", "tags": ["sweet", "cold", "indulgent", "dessert"], "price": 79, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Butter Scotch Ice Cream (C2C)", "tags": ["sweet", "cold", "indulgent", "dessert"], "price": 79, "restaurant": "Cheers to Chai (C2C)"},
    {"name": "Vanilla Ice Cream (C2C)", "tags": ["sweet", "cold", "light", "dessert"], "price": 69, "restaurant": "Cheers to Chai (C2C)"},
 
    # ─── 2. Alpine Espresso ────────────────────────────────────────────────────
 
    # Hot Coffee
    {"name": "Espresso (Alpine)", "tags": ["warm", "bold", "energizing", "classic"], "price": 80, "restaurant": "Alpine Espresso"},
    {"name": "Americano (Alpine)", "tags": ["warm", "bold", "energizing", "simple"], "price": 90, "restaurant": "Alpine Espresso"},
    {"name": "Cappuccino (Alpine)", "tags": ["warm", "frothy", "comforting", "classic"], "price": 110, "restaurant": "Alpine Espresso"},
    {"name": "Cafe Latte (Alpine)", "tags": ["warm", "creamy", "comforting", "classic"], "price": 120, "restaurant": "Alpine Espresso"},
    {"name": "Mocha (Alpine)", "tags": ["warm", "sweet", "rich", "comforting"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Hot Chocolate (Alpine)", "tags": ["warm", "sweet", "comforting", "indulgent"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Irish Coffee (Alpine)", "tags": ["warm", "premium", "rich", "bold"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Tiramisu Coffee (Alpine)", "tags": ["warm", "premium", "indulgent", "sweet"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Affogato (Alpine)", "tags": ["warm", "premium", "indulgent", "dessert"], "price": 160, "restaurant": "Alpine Espresso"},
 
    # Cold Coffee
    {"name": "Iced Americano (Alpine)", "tags": ["cold", "bold", "energizing", "refreshing"], "price": 85, "restaurant": "Alpine Espresso"},
    {"name": "Iced Cappuccino (Alpine)", "tags": ["cold", "frothy", "refreshing", "classic"], "price": 100, "restaurant": "Alpine Espresso"},
    {"name": "Iced Latte (Alpine)", "tags": ["cold", "creamy", "refreshing", "classic"], "price": 110, "restaurant": "Alpine Espresso"},
    {"name": "Frappe (Alpine)", "tags": ["cold", "blended", "refreshing", "sweet"], "price": 120, "restaurant": "Alpine Espresso"},
    {"name": "Frappe Chocolate (Alpine)", "tags": ["cold", "sweet", "indulgent", "blended"], "price": 160, "restaurant": "Alpine Espresso"},
 
    # Other Beverages
    {"name": "Boba Tea Green Apple (Alpine)", "tags": ["cold", "fruity", "unique", "refreshing"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Boba Tea Raspberry (Alpine)", "tags": ["cold", "fruity", "unique", "sweet"], "price": 130, "restaurant": "Alpine Espresso"},
    {"name": "Redbull Energy Drink (Alpine)", "tags": ["cold", "energizing", "bold", "quick"], "price": 130, "restaurant": "Alpine Espresso"},
 
    # Breakfast
    {"name": "Cornflakes (Alpine)", "tags": ["light", "quick", "simple", "healthy"], "price": 80, "restaurant": "Alpine Espresso"},
    {"name": "Sunny Side Up (Alpine)", "tags": ["light", "high protein", "simple", "quick"], "price": 100, "restaurant": "Alpine Espresso"},
    {"name": "Cereal and Cornflakes (Alpine)", "tags": ["light", "healthy", "simple", "quick"], "price": 100, "restaurant": "Alpine Espresso"},
    {"name": "Scrambled Eggs (Alpine)", "tags": ["high protein", "light", "quick", "simple"], "price": 80, "restaurant": "Alpine Espresso"},
 
    # Salads
    {"name": "Veg Salad (Alpine)", "tags": ["fresh", "light", "healthy", "vegetarian"], "price": 120, "restaurant": "Alpine Espresso"},
    {"name": "Paneer Salad (Alpine)", "tags": ["fresh", "high protein", "healthy", "light"], "price": 120, "restaurant": "Alpine Espresso"},
    {"name": "Egg Salad (Alpine)", "tags": ["fresh", "high protein", "healthy", "light"], "price": 180, "restaurant": "Alpine Espresso"},
    {"name": "Salami and Chicken Salad (Alpine)", "tags": ["fresh", "high protein", "non-veg", "light"], "price": 230, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Salad (Alpine)", "tags": ["fresh", "high protein", "healthy", "non-veg"], "price": 160, "restaurant": "Alpine Espresso"},
 
    # Smoothies
    {"name": "Banana Smoothie (Alpine)", "tags": ["cold", "healthy", "filling", "energizing"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Strawberry Smoothie (Alpine)", "tags": ["cold", "fruity", "healthy", "refreshing"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Blueberry Smoothie (Alpine)", "tags": ["cold", "fruity", "healthy", "antioxidant"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Kiwi Smoothie (Alpine)", "tags": ["cold", "fruity", "refreshing", "healthy"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Alpine Surprise Smoothie", "tags": ["cold", "unique", "refreshing", "healthy"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Mango Smoothie (Alpine)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Protein Smoothie (Alpine)", "tags": ["cold", "high protein", "healthy", "energizing"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Mix Berry Smoothie (Alpine)", "tags": ["cold", "fruity", "healthy", "antioxidant"], "price": 200, "restaurant": "Alpine Espresso"},
 
    # Shakes
    {"name": "Protein Shake (Alpine)", "tags": ["cold", "high protein", "fitness", "filling"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Oreo Shake (Alpine)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 170, "restaurant": "Alpine Espresso"},
    {"name": "Blue Berry Shake (Alpine)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 170, "restaurant": "Alpine Espresso"},
    {"name": "Hazelnut Shake (Alpine)", "tags": ["cold", "aromatic", "sweet", "indulgent"], "price": 170, "restaurant": "Alpine Espresso"},
    {"name": "Strawberry Shake (Alpine)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 170, "restaurant": "Alpine Espresso"},
    {"name": "Chocolate Shake (Alpine)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 170, "restaurant": "Alpine Espresso"},
    {"name": "Brownie Hazelnut Shake (Alpine)", "tags": ["cold", "rich", "indulgent", "premium"], "price": 190, "restaurant": "Alpine Espresso"},
    {"name": "Scoff Shake (Alpine)", "tags": ["cold", "indulgent", "premium", "rich"], "price": 190, "restaurant": "Alpine Espresso"},
 
    # Desserts & Bakery
    {"name": "Chocolate Waffle (Alpine)", "tags": ["sweet", "warm", "indulgent", "dessert"], "price": 160, "restaurant": "Alpine Espresso"},
    {"name": "Vanilla Waffle (Alpine)", "tags": ["sweet", "warm", "classic", "dessert"], "price": 170, "restaurant": "Alpine Espresso"},
    {"name": "Red Velvet Waffle (Alpine)", "tags": ["sweet", "indulgent", "premium", "dessert"], "price": 180, "restaurant": "Alpine Espresso"},
    {"name": "Blueberry Pancake (Alpine)", "tags": ["sweet", "fruity", "warm", "dessert"], "price": 180, "restaurant": "Alpine Espresso"},
    {"name": "Strawberry Pancake (Alpine)", "tags": ["sweet", "fruity", "warm", "dessert"], "price": 180, "restaurant": "Alpine Espresso"},
    {"name": "Protein Pancake (Alpine)", "tags": ["sweet", "high protein", "healthy", "filling"], "price": 230, "restaurant": "Alpine Espresso"},
    {"name": "Brownie (Alpine)", "tags": ["sweet", "indulgent", "rich", "dessert"], "price": 110, "restaurant": "Alpine Espresso"},
    {"name": "Brownie with Ice Cream (Alpine)", "tags": ["sweet", "indulgent", "rich", "premium"], "price": 170, "restaurant": "Alpine Espresso"},
 
    # Garlic Loaf
    {"name": "Veg Garlic Loaf Small (Alpine)", "tags": ["savory", "warm", "light", "quick"], "price": 100, "restaurant": "Alpine Espresso"},
    {"name": "Veg Garlic Loaf Medium (Alpine)", "tags": ["savory", "warm", "filling", "comforting"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Veg Garlic Loaf Large (Alpine)", "tags": ["savory", "warm", "filling", "sharing"], "price": 300, "restaurant": "Alpine Espresso"},
    {"name": "Non-Veg Garlic Loaf Small (Alpine)", "tags": ["savory", "warm", "non-veg", "quick"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Non-Veg Garlic Loaf Medium (Alpine)", "tags": ["savory", "warm", "non-veg", "filling"], "price": 250, "restaurant": "Alpine Espresso"},
    {"name": "Non-Veg Garlic Loaf Large (Alpine)", "tags": ["savory", "warm", "non-veg", "sharing"], "price": 350, "restaurant": "Alpine Espresso"},
 
    # Thin Crust Pizza (Veg) - using 7" price
    {"name": "Margherita Thin Crust Pizza (Alpine)", "tags": ["classic", "cheesy", "vegetarian", "light"], "price": 120, "restaurant": "Alpine Espresso"},
    {"name": "Hawaiian Veg Thin Crust Pizza (Alpine)", "tags": ["sweet", "tangy", "vegetarian", "unique"], "price": 130, "restaurant": "Alpine Espresso"},
    {"name": "Farm House Thin Crust Pizza (Alpine)", "tags": ["loaded", "vegetarian", "filling", "classic"], "price": 140, "restaurant": "Alpine Espresso"},
    {"name": "Mushroom & Corn Thin Crust Pizza (Alpine)", "tags": ["earthy", "vegetarian", "light", "classic"], "price": 140, "restaurant": "Alpine Espresso"},
    {"name": "Paneer & Corn Thin Crust Pizza (Alpine)", "tags": ["high protein", "vegetarian", "filling", "cheesy"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Paneer Paprika Thin Crust Pizza (Alpine)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 140, "restaurant": "Alpine Espresso"},
 
    # Non-Veg Pizza (7" price)
    {"name": "Hawaiian Chicken Pizza (Alpine)", "tags": ["sweet", "non-veg", "unique", "filling"], "price": 140, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Sausage Pizza (Alpine)", "tags": ["savory", "non-veg", "filling", "bold"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Fiery Chicken Jalapeño Pizza (Alpine)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 160, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Harvest Pizza (Alpine)", "tags": ["savory", "non-veg", "loaded", "filling"], "price": 170, "restaurant": "Alpine Espresso"},
 
    # Pocket Pizza
    {"name": "Veg Pocket Pizza (Alpine)", "tags": ["vegetarian", "filling", "quick", "unique"], "price": 250, "restaurant": "Alpine Espresso"},
    {"name": "Non-Veg Pocket Pizza (Alpine)", "tags": ["non-veg", "filling", "quick", "unique"], "price": 280, "restaurant": "Alpine Espresso"},
 
    # Pasta (using Red Sauce Veg price)
    {"name": "Veg Red Sauce Pasta (Alpine)", "tags": ["tangy", "vegetarian", "filling", "comfort food"], "price": 160, "restaurant": "Alpine Espresso"},
    {"name": "Veg White Sauce Pasta (Alpine)", "tags": ["creamy", "vegetarian", "filling", "comfort food"], "price": 170, "restaurant": "Alpine Espresso"},
    {"name": "Veg Pink Sauce Pasta (Alpine)", "tags": ["creamy", "tangy", "vegetarian", "filling"], "price": 180, "restaurant": "Alpine Espresso"},
    {"name": "Non-Veg Red Sauce Pasta (Alpine)", "tags": ["tangy", "non-veg", "filling", "comfort food"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Non-Veg White Sauce Pasta (Alpine)", "tags": ["creamy", "non-veg", "filling", "comfort food"], "price": 230, "restaurant": "Alpine Espresso"},
    {"name": "Non-Veg Pink Sauce Pasta (Alpine)", "tags": ["creamy", "tangy", "non-veg", "filling"], "price": 250, "restaurant": "Alpine Espresso"},
 
    # Sandwiches
    {"name": "Veg Grilled Sandwich (Alpine)", "tags": ["quick", "light", "vegetarian", "grilled"], "price": 120, "restaurant": "Alpine Espresso"},
    {"name": "Veg Corn Sandwich (Alpine)", "tags": ["quick", "light", "vegetarian", "sweet"], "price": 130, "restaurant": "Alpine Espresso"},
    {"name": "Paneer Sandwich (Alpine)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Club Veg Sandwich (Alpine)", "tags": ["loaded", "vegetarian", "filling", "premium"], "price": 200, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Sandwich (Alpine)", "tags": ["non-veg", "filling", "high protein", "quick"], "price": 230, "restaurant": "Alpine Espresso"},
 
    # Burgers
    {"name": "Veg Burger (Alpine)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 80, "restaurant": "Alpine Espresso"},
    {"name": "Cheese Burger (Alpine)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 100, "restaurant": "Alpine Espresso"},
    {"name": "Super Veggie Burger (Alpine)", "tags": ["filling", "vegetarian", "loaded", "hearty"], "price": 130, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Burger (Alpine)", "tags": ["non-veg", "filling", "quick", "hearty"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Salami Burger (Alpine)", "tags": ["non-veg", "savory", "filling", "bold"], "price": 180, "restaurant": "Alpine Espresso"},
 
    # Wraps
    {"name": "Veg Wrap (Alpine)", "tags": ["quick", "light", "vegetarian", "balanced"], "price": 99, "restaurant": "Alpine Espresso"},
    {"name": "Paneer Wrap (Alpine)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 119, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Wrap (Alpine)", "tags": ["non-veg", "filling", "high protein", "quick"], "price": 140, "restaurant": "Alpine Espresso"},
 
    # Sides
    {"name": "Fries (Alpine)", "tags": ["crispy", "snack", "quick", "simple"], "price": 110, "restaurant": "Alpine Espresso"},
    {"name": "Peri Peri Fries (Alpine)", "tags": ["spicy", "crispy", "bold", "snack"], "price": 120, "restaurant": "Alpine Espresso"},
    {"name": "Cheese Fries (Alpine)", "tags": ["cheesy", "indulgent", "snack", "comfort food"], "price": 130, "restaurant": "Alpine Espresso"},
    {"name": "Veg Nugget (Alpine)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 130, "restaurant": "Alpine Espresso"},
    {"name": "Veggie Fingers (Alpine)", "tags": ["crispy", "vegetarian", "snack", "light"], "price": 140, "restaurant": "Alpine Espresso"},
    {"name": "Cheese Nugget (Alpine)", "tags": ["cheesy", "crispy", "indulgent", "snack"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Loaded Fries (Alpine)", "tags": ["cheesy", "indulgent", "filling", "snack"], "price": 150, "restaurant": "Alpine Espresso"},
    {"name": "Chicken Nugget (Alpine)", "tags": ["non-veg", "crispy", "snack", "filling"], "price": 190, "restaurant": "Alpine Espresso"},
 
    # ─── 3. Nescafe ───────────────────────────────────────────────────────────
 
    # Hot Favorites
    {"name": "Nescafé Regular", "tags": ["warm", "simple", "energizing", "budget"], "price": 25, "restaurant": "Nescafe"},
    {"name": "Cappuccino (Nescafe)", "tags": ["warm", "frothy", "comforting", "quick"], "price": 35, "restaurant": "Nescafe"},
    {"name": "Café Mocha (Nescafe)", "tags": ["warm", "sweet", "comforting", "quick"], "price": 30, "restaurant": "Nescafe"},
    {"name": "Café Latte (Nescafe)", "tags": ["warm", "creamy", "comforting", "quick"], "price": 30, "restaurant": "Nescafe"},
    {"name": "Hot Chocolate (Nescafe)", "tags": ["warm", "sweet", "comforting", "simple"], "price": 25, "restaurant": "Nescafe"},
    {"name": "Espresso (Nescafe)", "tags": ["warm", "bold", "energizing", "quick"], "price": 20, "restaurant": "Nescafe"},
    {"name": "Nestea Cardamom", "tags": ["warm", "aromatic", "soothing", "budget"], "price": 15, "restaurant": "Nescafe"},
    {"name": "Nestea Masala Tea", "tags": ["warm", "spicy", "comforting", "budget"], "price": 20, "restaurant": "Nescafe"},
    {"name": "Hot Lemon Tea (Nescafe)", "tags": ["warm", "tangy", "refreshing", "budget"], "price": 20, "restaurant": "Nescafe"},
    {"name": "Nestea Tea Bag", "tags": ["warm", "simple", "light", "budget"], "price": 10, "restaurant": "Nescafe"},
 
    # Cold Refreshers
    {"name": "Nescafé Ice (Nescafe)", "tags": ["cold", "energizing", "refreshing", "simple"], "price": 50, "restaurant": "Nescafe"},
    {"name": "Hazelnut Frappe (Nescafe)", "tags": ["cold", "aromatic", "sweet", "refreshing"], "price": 60, "restaurant": "Nescafe"},
    {"name": "Caramel Frappe (Nescafe)", "tags": ["cold", "sweet", "indulgent", "refreshing"], "price": 60, "restaurant": "Nescafe"},
    {"name": "Lemon Ice Tea (Nescafe)", "tags": ["cold", "tangy", "refreshing", "light"], "price": 70, "restaurant": "Nescafe"},
    {"name": "Masala Ice Tea (Nescafe)", "tags": ["cold", "spicy", "refreshing", "unique"], "price": 40, "restaurant": "Nescafe"},
    {"name": "Cold Chocolate (Nescafe)", "tags": ["cold", "sweet", "comforting", "simple"], "price": 45, "restaurant": "Nescafe"},
 
    # Sandwiches
    {"name": "Veg Grill Sandwich (Nescafe)", "tags": ["quick", "light", "vegetarian", "grilled"], "price": 45, "restaurant": "Nescafe"},
    {"name": "Veg Paneer Sandwich (Nescafe)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 45, "restaurant": "Nescafe"},
    {"name": "Grill Corn Sandwich (Nescafe)", "tags": ["quick", "sweet", "vegetarian", "grilled"], "price": 45, "restaurant": "Nescafe"},
    {"name": "Tandoori Paneer Sandwich (Nescafe)", "tags": ["spicy", "grilled", "high protein", "filling"], "price": 70, "restaurant": "Nescafe"},
    {"name": "Chilly Garlic Sandwich (Nescafe)", "tags": ["spicy", "quick", "bold", "light"], "price": 40, "restaurant": "Nescafe"},
 
    # Burgers
    {"name": "Veg Burger (Nescafe)", "tags": ["quick", "simple", "budget", "vegetarian"], "price": 50, "restaurant": "Nescafe"},
    {"name": "Cheese Burger (Nescafe)", "tags": ["cheesy", "quick", "comfort food", "budget"], "price": 60, "restaurant": "Nescafe"},
    {"name": "Paneer Burger (Nescafe)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 60, "restaurant": "Nescafe"},
 
    # Fries
    {"name": "Masala Fries (Nescafe)", "tags": ["spicy", "crispy", "snack", "quick"], "price": 70, "restaurant": "Nescafe"},
    {"name": "Chilly Fries (Nescafe)", "tags": ["spicy", "crispy", "snack", "bold"], "price": 50, "restaurant": "Nescafe"},
    {"name": "Cheese Fries (Nescafe)", "tags": ["cheesy", "crispy", "indulgent", "snack"], "price": 60, "restaurant": "Nescafe"},
 
    # Pasta
    {"name": "White Sauce Pasta (Nescafe)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 50, "restaurant": "Nescafe"},
    {"name": "Red Sauce Pasta (Nescafe)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 60, "restaurant": "Nescafe"},
    {"name": "Mix Sauce Pasta (Nescafe)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 60, "restaurant": "Nescafe"},
 
    # Other
    {"name": "Paneer Kulcha (Nescafe)", "tags": ["filling", "high protein", "warm", "comfort food"], "price": 60, "restaurant": "Nescafe"},
 
    # ─── 4. Kiyansh Cafe ──────────────────────────────────────────────────────
 
    # Non-Veg – Chicken Momos
    {"name": "Chicken Steam Momos (Kiyansh)", "tags": ["light", "non-veg", "steamed", "snack"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Fried Momos (Kiyansh)", "tags": ["crispy", "non-veg", "snack", "filling"], "price": 90, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Jhol Momos (Kiyansh)", "tags": ["spicy", "non-veg", "saucy", "unique"], "price": 100, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Chilly Momos (Kiyansh)", "tags": ["spicy", "non-veg", "bold", "snack"], "price": 100, "restaurant": "Kiyansh Cafe"},
 
    # Non-Veg – Noodles & Maggi
    {"name": "Egg Chowmein (Kiyansh)", "tags": ["quick", "non-veg", "filling", "comfort food"], "price": 70, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Chowmein (Kiyansh)", "tags": ["quick", "non-veg", "filling", "comfort food"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Egg Maggi (Kiyansh)", "tags": ["quick", "non-veg", "comfort food", "simple"], "price": 60, "restaurant": "Kiyansh Cafe"},
 
    # Non-Veg – Chinese
    {"name": "Egg Fried Rice (Kiyansh)", "tags": ["filling", "non-veg", "quick", "comfort food"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Fried Rice (Kiyansh)", "tags": ["filling", "non-veg", "quick", "comfort food"], "price": 90, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Garlic Fried Rice (Kiyansh)", "tags": ["bold", "non-veg", "filling", "savory"], "price": 100, "restaurant": "Kiyansh Cafe"},
    {"name": "Chilli Chicken (Kiyansh)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 200, "restaurant": "Kiyansh Cafe"},
 
    # Non-Veg – Burgers & Eggs
    {"name": "Chicken Burger (Kiyansh)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Cheese Burger (Kiyansh)", "tags": ["cheesy", "non-veg", "filling", "indulgent"], "price": 100, "restaurant": "Kiyansh Cafe"},
    {"name": "Boiled Egg (Kiyansh)", "tags": ["high protein", "simple", "light", "budget"], "price": 12, "restaurant": "Kiyansh Cafe"},
    {"name": "Plain Omelette (Kiyansh)", "tags": ["high protein", "simple", "quick", "light"], "price": 30, "restaurant": "Kiyansh Cafe"},
    {"name": "Masala Omelette (Kiyansh)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 40, "restaurant": "Kiyansh Cafe"},
    {"name": "Bread Omelette (Kiyansh)", "tags": ["high protein", "filling", "quick", "budget"], "price": 50, "restaurant": "Kiyansh Cafe"},
 
    # Non-Veg – Rice
    {"name": "Chicken Biryani (Kiyansh)", "tags": ["filling", "non-veg", "aromatic", "comfort food"], "price": 120, "restaurant": "Kiyansh Cafe"},
    {"name": "Chicken Chawal (Kiyansh)", "tags": ["filling", "non-veg", "simple", "comfort food"], "price": 150, "restaurant": "Kiyansh Cafe"},
 
    # Veg – Momos
    {"name": "Veg Steam Momos (Kiyansh)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 50, "restaurant": "Kiyansh Cafe"},
    {"name": "Veg Fried Momos (Kiyansh)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 60, "restaurant": "Kiyansh Cafe"},
    {"name": "Veg Jhol Momos (Kiyansh)", "tags": ["spicy", "vegetarian", "saucy", "unique"], "price": 90, "restaurant": "Kiyansh Cafe"},
    {"name": "Veg Chilly Momos (Kiyansh)", "tags": ["spicy", "vegetarian", "bold", "snack"], "price": 100, "restaurant": "Kiyansh Cafe"},
 
    # Veg – Noodles & Maggi
    {"name": "Veg Chowmein (Kiyansh)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 50, "restaurant": "Kiyansh Cafe"},
    {"name": "Paneer Chowmein (Kiyansh)", "tags": ["filling", "high protein", "vegetarian", "comfort food"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Plain Maggi (Kiyansh)", "tags": ["quick", "simple", "comfort food", "budget"], "price": 40, "restaurant": "Kiyansh Cafe"},
    {"name": "Veggie Maggi (Kiyansh)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 50, "restaurant": "Kiyansh Cafe"},
    {"name": "Cheese Maggi (Kiyansh)", "tags": ["cheesy", "indulgent", "comfort food", "quick"], "price": 60, "restaurant": "Kiyansh Cafe"},
    {"name": "Veggie Wai Wai (Kiyansh)", "tags": ["quick", "light", "vegetarian", "unique"], "price": 50, "restaurant": "Kiyansh Cafe"},
 
    # Veg – Chinese & Snacks
    {"name": "Veg Fried Rice (Kiyansh)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 70, "restaurant": "Kiyansh Cafe"},
    {"name": "Paneer Fried Rice (Kiyansh)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Veg Manchurian (Kiyansh)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Chilli Paneer (Kiyansh)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 150, "restaurant": "Kiyansh Cafe"},
    {"name": "Honey Chilli Potato (Kiyansh)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 120, "restaurant": "Kiyansh Cafe"},
    {"name": "Chilli Potato (Kiyansh)", "tags": ["spicy", "crispy", "snack", "bold"], "price": 100, "restaurant": "Kiyansh Cafe"},
    {"name": "French Fries (Kiyansh)", "tags": ["crispy", "snack", "quick", "budget"], "price": 70, "restaurant": "Kiyansh Cafe"},
    {"name": "Spring Roll (Kiyansh)", "tags": ["crispy", "vegetarian", "snack", "light"], "price": 80, "restaurant": "Kiyansh Cafe"},
 
    # Veg – Paratha
    {"name": "Plain Paratha (Kiyansh)", "tags": ["simple", "budget", "light", "home-style"], "price": 25, "restaurant": "Kiyansh Cafe"},
    {"name": "Aloo Paratha (Kiyansh)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 40, "restaurant": "Kiyansh Cafe"},
    {"name": "Aloo Pyaz Paratha (Kiyansh)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 45, "restaurant": "Kiyansh Cafe"},
    {"name": "Mix Veg Paratha (Kiyansh)", "tags": ["filling", "vegetarian", "home-style", "balanced"], "price": 50, "restaurant": "Kiyansh Cafe"},
    {"name": "Paneer Paratha (Kiyansh)", "tags": ["filling", "high protein", "comforting", "home-style"], "price": 60, "restaurant": "Kiyansh Cafe"},
 
    # Veg – Burger
    {"name": "Veg Burger (Kiyansh)", "tags": ["quick", "budget", "vegetarian", "simple"], "price": 40, "restaurant": "Kiyansh Cafe"},
    {"name": "Cheese Burger (Kiyansh)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 60, "restaurant": "Kiyansh Cafe"},
    {"name": "Double Cheese Burger (Kiyansh)", "tags": ["cheesy", "indulgent", "filling", "comfort food"], "price": 80, "restaurant": "Kiyansh Cafe"},
 
    # Combos
    {"name": "Chowmein + Manchurian Combo (Kiyansh)", "tags": ["filling", "vegetarian", "combo", "comfort food"], "price": 160, "restaurant": "Kiyansh Cafe"},
    {"name": "Fried Rice + Manchurian Combo (Kiyansh)", "tags": ["filling", "vegetarian", "combo", "comfort food"], "price": 160, "restaurant": "Kiyansh Cafe"},
 
    # Beverages
    {"name": "Black Tea (Kiyansh)", "tags": ["warm", "simple", "light", "budget"], "price": 10, "restaurant": "Kiyansh Cafe"},
    {"name": "Milk Tea (Kiyansh)", "tags": ["warm", "comforting", "simple", "budget"], "price": 15, "restaurant": "Kiyansh Cafe"},
    {"name": "Black Coffee (Kiyansh)", "tags": ["warm", "bold", "energizing", "budget"], "price": 20, "restaurant": "Kiyansh Cafe"},
    {"name": "Milk Coffee (Kiyansh)", "tags": ["warm", "comforting", "simple", "light"], "price": 30, "restaurant": "Kiyansh Cafe"},
    {"name": "Cold Coffee (Kiyansh)", "tags": ["cold", "energizing", "refreshing", "simple"], "price": 60, "restaurant": "Kiyansh Cafe"},
    {"name": "Oreo Shake (Kiyansh)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 80, "restaurant": "Kiyansh Cafe"},
    {"name": "Lassi (Kiyansh)", "tags": ["cold", "refreshing", "comforting", "light"], "price": 40, "restaurant": "Kiyansh Cafe"},
    {"name": "Lemon Soda Water (Kiyansh)", "tags": ["cold", "fizzy", "refreshing", "tangy"], "price": 30, "restaurant": "Kiyansh Cafe"},
 
    # ─── 5. Aru's ─────────────────────────────────────────────────────────────
 
    # Veg Paneer
    {"name": "Kadhai Paneer (Aru's)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 180, "restaurant": "Aru's"},
    {"name": "Paneer Makki Masala (Aru's)", "tags": ["spicy", "high protein", "unique", "filling"], "price": 190, "restaurant": "Aru's"},
    {"name": "Paneer Do Pyaza (Aru's)", "tags": ["spicy", "high protein", "onion-rich", "bold"], "price": 190, "restaurant": "Aru's"},
    {"name": "Paneer Bhurji (Aru's)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 150, "restaurant": "Aru's"},
    {"name": "Paneer Butter Masala (Aru's)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 190, "restaurant": "Aru's"},
    {"name": "Mater Paneer (Aru's)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 160, "restaurant": "Aru's"},
    {"name": "Paneer Lababdar (Aru's)", "tags": ["rich", "high protein", "indulgent", "creamy"], "price": 200, "restaurant": "Aru's"},
    {"name": "Shahi Paneer (Aru's)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 200, "restaurant": "Aru's"},
 
    # Other Veg
    {"name": "Dal Tadka (Aru's)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 100, "restaurant": "Aru's"},
    {"name": "Dal Makhani (Aru's)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 130, "restaurant": "Aru's"},
    {"name": "Chana Masala (Aru's)", "tags": ["spicy", "filling", "vegetarian", "bold"], "price": 110, "restaurant": "Aru's"},
    {"name": "Rajmah Masala (Aru's)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 100, "restaurant": "Aru's"},
    {"name": "Malai Kofta (Aru's)", "tags": ["rich", "creamy", "indulgent", "vegetarian"], "price": 210, "restaurant": "Aru's"},
    {"name": "Mix Veg (Aru's)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 120, "restaurant": "Aru's"},
    {"name": "Jeera Aaloo (Aru's)", "tags": ["simple", "comforting", "home-style", "light"], "price": 70, "restaurant": "Aru's"},
    {"name": "Soya Chap Masala (Aru's)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 160, "restaurant": "Aru's"},
    {"name": "Soya Butter Masala (Aru's)", "tags": ["rich", "high protein", "creamy", "vegetarian"], "price": 180, "restaurant": "Aru's"},
    {"name": "Mushroom Masala (Aru's)", "tags": ["earthy", "spicy", "vegetarian", "filling"], "price": 160, "restaurant": "Aru's"},
    {"name": "Mater Mushroom (Aru's)", "tags": ["earthy", "vegetarian", "balanced", "filling"], "price": 170, "restaurant": "Aru's"},
    {"name": "Mushroom Methi Mater Malai (Aru's)", "tags": ["creamy", "earthy", "vegetarian", "premium"], "price": 190, "restaurant": "Aru's"},
    {"name": "Veg Kolapuri (Aru's)", "tags": ["spicy", "bold", "vegetarian", "filling"], "price": 160, "restaurant": "Aru's"},
    {"name": "Veg Handi (Aru's)", "tags": ["rich", "comforting", "vegetarian", "filling"], "price": 190, "restaurant": "Aru's"},
    {"name": "Paneer Nan with Gravy (Aru's)", "tags": ["filling", "high protein", "comforting", "complete meal"], "price": 120, "restaurant": "Aru's"},
 
    # Non-Veg
    {"name": "Rara Chicken (Aru's)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 250, "restaurant": "Aru's"},
    {"name": "Chicken Masala (Aru's)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 220, "restaurant": "Aru's"},
    {"name": "Kadai Chicken (Aru's)", "tags": ["spicy", "non-veg", "bold", "comforting"], "price": 210, "restaurant": "Aru's"},
    {"name": "Butter Chicken (Aru's)", "tags": ["creamy", "non-veg", "rich", "comforting"], "price": 230, "restaurant": "Aru's"},
    {"name": "Chicken Curry (Aru's)", "tags": ["comforting", "non-veg", "home-style", "filling"], "price": 220, "restaurant": "Aru's"},
    {"name": "Egg Curry (Aru's)", "tags": ["comforting", "high protein", "home-style", "simple"], "price": 140, "restaurant": "Aru's"},
 
    # Biryani
    {"name": "Veg Biryani (Aru's)", "tags": ["aromatic", "vegetarian", "filling", "comfort food"], "price": 170, "restaurant": "Aru's"},
    {"name": "Egg Biryani (Aru's)", "tags": ["aromatic", "non-veg", "filling", "comfort food"], "price": 190, "restaurant": "Aru's"},
    {"name": "Chicken Biryani (Aru's)", "tags": ["aromatic", "non-veg", "filling", "comfort food"], "price": 220, "restaurant": "Aru's"},
    {"name": "Chicken Hydrabadi Biryani (Aru's)", "tags": ["aromatic", "spicy", "non-veg", "premium"], "price": 250, "restaurant": "Aru's"},
 
    # Thali
    {"name": "Special Veg Thali (Aru's)", "tags": ["balanced", "vegetarian", "filling", "variety"], "price": 160, "restaurant": "Aru's"},
    {"name": "Special Non-Veg Thali (Aru's)", "tags": ["balanced", "non-veg", "filling", "variety"], "price": 200, "restaurant": "Aru's"},
 
    # Rice Dishes
    {"name": "SPL Rajmah Rice (Aru's)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 50, "restaurant": "Aru's"},
    {"name": "Steam Rice (Aru's)", "tags": ["simple", "light", "budget", "home-style"], "price": 60, "restaurant": "Aru's"},
    {"name": "Jeera Rice (Aru's)", "tags": ["light", "aromatic", "simple", "comforting"], "price": 70, "restaurant": "Aru's"},
    {"name": "Lemon Rice (Aru's)", "tags": ["tangy", "light", "South Indian", "refreshing"], "price": 90, "restaurant": "Aru's"},
    {"name": "Onion Tomato Pulao (Aru's)", "tags": ["aromatic", "light", "vegetarian", "balanced"], "price": 100, "restaurant": "Aru's"},
    {"name": "Green Peas Pulao (Aru's)", "tags": ["light", "aromatic", "vegetarian", "balanced"], "price": 100, "restaurant": "Aru's"},
 
    # Breads/Papad
    {"name": "Tandoori Roti (Aru's)", "tags": ["simple", "light", "budget", "home-style"], "price": 10, "restaurant": "Aru's"},
    {"name": "Butter Roti (Aru's)", "tags": ["simple", "comforting", "budget", "home-style"], "price": 15, "restaurant": "Aru's"},
    {"name": "Plain Nan (Aru's)", "tags": ["soft", "simple", "light", "classic"], "price": 25, "restaurant": "Aru's"},
    {"name": "Butter Nan (Aru's)", "tags": ["soft", "comforting", "buttery", "classic"], "price": 35, "restaurant": "Aru's"},
    {"name": "Lacha Prantha (Aru's)", "tags": ["flaky", "comforting", "layered", "classic"], "price": 35, "restaurant": "Aru's"},
    {"name": "Garlic Nan (Aru's)", "tags": ["aromatic", "soft", "savory", "classic"], "price": 40, "restaurant": "Aru's"},
    {"name": "Fried Papad (Aru's)", "tags": ["crispy", "light", "simple", "snack"], "price": 20, "restaurant": "Aru's"},
    {"name": "Masala Papad (Aru's)", "tags": ["spicy", "crispy", "snack", "light"], "price": 30, "restaurant": "Aru's"},
    {"name": "Roasted Papad (Aru's)", "tags": ["light", "crispy", "simple", "healthy"], "price": 15, "restaurant": "Aru's"},
 
    # South Indian
    {"name": "Veg Uttapam (Aru's)", "tags": ["South Indian", "light", "vegetarian", "comfort food"], "price": 110, "restaurant": "Aru's"},
    {"name": "Masala Uttapam (Aru's)", "tags": ["South Indian", "spicy", "vegetarian", "filling"], "price": 120, "restaurant": "Aru's"},
    {"name": "Cheese Uttapam (Aru's)", "tags": ["South Indian", "cheesy", "indulgent", "filling"], "price": 140, "restaurant": "Aru's"},
    {"name": "Onion Tomato Uttapam (Aru's)", "tags": ["South Indian", "tangy", "vegetarian", "light"], "price": 100, "restaurant": "Aru's"},
    {"name": "Idli Sambar (Aru's)", "tags": ["South Indian", "light", "healthy", "comfort food"], "price": 70, "restaurant": "Aru's"},
    {"name": "Fried Chilly Idli (Aru's)", "tags": ["South Indian", "spicy", "crispy", "snack"], "price": 120, "restaurant": "Aru's"},
    {"name": "Plain Dosa (Aru's)", "tags": ["South Indian", "light", "crispy", "simple"], "price": 80, "restaurant": "Aru's"},
    {"name": "Masala Dosa (Aru's)", "tags": ["South Indian", "filling", "crispy", "classic"], "price": 100, "restaurant": "Aru's"},
    {"name": "Mysore Masala Dosa (Aru's)", "tags": ["South Indian", "spicy", "crispy", "bold"], "price": 130, "restaurant": "Aru's"},
    {"name": "Mushroom Chilly Fry Dosa (Aru's)", "tags": ["South Indian", "earthy", "spicy", "unique"], "price": 130, "restaurant": "Aru's"},
    {"name": "Spring Dosa (Aru's)", "tags": ["South Indian", "crispy", "filling", "unique"], "price": 120, "restaurant": "Aru's"},
    {"name": "Paneer Masala Dosa (Aru's)", "tags": ["South Indian", "high protein", "filling", "spicy"], "price": 130, "restaurant": "Aru's"},
    {"name": "Schezwan Masala Dosa (Aru's)", "tags": ["South Indian", "spicy", "fusion", "bold"], "price": 110, "restaurant": "Aru's"},
    {"name": "Paper Plain Dosa (Aru's)", "tags": ["South Indian", "crispy", "light", "simple"], "price": 90, "restaurant": "Aru's"},
    {"name": "Cheese Masala Dosa (Aru's)", "tags": ["South Indian", "cheesy", "indulgent", "filling"], "price": 150, "restaurant": "Aru's"},
    {"name": "Egg Dosa (Aru's)", "tags": ["South Indian", "high protein", "filling", "crispy"], "price": 140, "restaurant": "Aru's"},
 
    # Chinese Snacks (Aru's Veg)
    {"name": "Honey Chilli Potato (Aru's)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 130, "restaurant": "Aru's"},
    {"name": "Chilly Cauliflower (Aru's)", "tags": ["spicy", "vegetarian", "crispy", "snack"], "price": 140, "restaurant": "Aru's"},
    {"name": "Chilly Cheese (Aru's)", "tags": ["cheesy", "spicy", "indulgent", "snack"], "price": 180, "restaurant": "Aru's"},
    {"name": "Chilly Momos (Aru's)", "tags": ["spicy", "vegetarian", "snack", "bold"], "price": 130, "restaurant": "Aru's"},
    {"name": "Veg Manchurian (Aru's)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 130, "restaurant": "Aru's"},
    {"name": "Chilly Mushroom (Aru's)", "tags": ["spicy", "earthy", "vegetarian", "snack"], "price": 180, "restaurant": "Aru's"},
    {"name": "Veg Fried Rice (Aru's)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 80, "restaurant": "Aru's"},
    {"name": "Veg Chowmein (Aru's)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 45, "restaurant": "Aru's"},
    {"name": "Hakka Noodle (Aru's)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 50, "restaurant": "Aru's"},
    {"name": "Veg Spring Roll (Aru's)", "tags": ["crispy", "light", "vegetarian", "snack"], "price": 90, "restaurant": "Aru's"},
    {"name": "Veg Steam Momos (Aru's)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 45, "restaurant": "Aru's"},
    {"name": "Veg Fried Momos (Aru's)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 50, "restaurant": "Aru's"},
 
    # Non-Veg Chinese (Aru's)
    {"name": "Chilli Chicken (Aru's)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 220, "restaurant": "Aru's"},
    {"name": "Lemon Chicken (Aru's)", "tags": ["tangy", "non-veg", "refreshing", "light"], "price": 230, "restaurant": "Aru's"},
    {"name": "Garlic Chicken (Aru's)", "tags": ["savory", "non-veg", "bold", "aromatic"], "price": 240, "restaurant": "Aru's"},
    {"name": "Lemon Coriander Chicken (Aru's)", "tags": ["tangy", "non-veg", "refreshing", "light"], "price": 230, "restaurant": "Aru's"},
    {"name": "Chicken 65 (Aru's)", "tags": ["spicy", "crispy", "non-veg", "snack"], "price": 240, "restaurant": "Aru's"},
    {"name": "Chilli Chicken Boneless (Aru's)", "tags": ["spicy", "non-veg", "bold", "premium"], "price": 260, "restaurant": "Aru's"},
    {"name": "Chicken Chowmein (Aru's)", "tags": ["quick", "non-veg", "filling", "comfort food"], "price": 60, "restaurant": "Aru's"},
    {"name": "Chicken Fried Rice (Aru's)", "tags": ["filling", "non-veg", "quick", "comfort food"], "price": 120, "restaurant": "Aru's"},
    {"name": "Egg Fried Rice (Aru's)", "tags": ["filling", "non-veg", "quick", "comfort food"], "price": 100, "restaurant": "Aru's"},
    {"name": "Egg Chowmein (Aru's)", "tags": ["quick", "non-veg", "light", "comfort food"], "price": 50, "restaurant": "Aru's"},
 
    # Soups
    {"name": "Manchow Soup Veg (Aru's)", "tags": ["warm", "light", "spicy", "soup"], "price": 40, "restaurant": "Aru's"},
    {"name": "Manchow Soup Non-Veg (Aru's)", "tags": ["warm", "light", "spicy", "soup"], "price": 60, "restaurant": "Aru's"},
    {"name": "Hot & Sour Soup Veg (Aru's)", "tags": ["warm", "tangy", "spicy", "soup"], "price": 40, "restaurant": "Aru's"},
    {"name": "Hot & Sour Soup Non-Veg (Aru's)", "tags": ["warm", "tangy", "spicy", "soup"], "price": 60, "restaurant": "Aru's"},
    {"name": "Thupka Veg (Aru's)", "tags": ["warm", "soupy", "light", "comfort food"], "price": 50, "restaurant": "Aru's"},
    {"name": "Thupka Non-Veg (Aru's)", "tags": ["warm", "soupy", "filling", "comfort food"], "price": 65, "restaurant": "Aru's"},
    {"name": "Lemon Coriander Soup Veg (Aru's)", "tags": ["warm", "tangy", "light", "refreshing"], "price": 50, "restaurant": "Aru's"},
    {"name": "Lemon Coriander Soup Non-Veg (Aru's)", "tags": ["warm", "tangy", "light", "non-veg"], "price": 65, "restaurant": "Aru's"},
 
    # Quick Bites
    {"name": "Veg Sandwich (Aru's)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 40, "restaurant": "Aru's"},
    {"name": "Veg Grilled Sandwich (Aru's)", "tags": ["quick", "light", "vegetarian", "grilled"], "price": 60, "restaurant": "Aru's"},
    {"name": "Cheese Grilled Sandwich (Aru's)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 100, "restaurant": "Aru's"},
    {"name": "Veg Burger (Aru's)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 50, "restaurant": "Aru's"},
    {"name": "Veg Cheese Burger (Aru's)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 70, "restaurant": "Aru's"},
    {"name": "Plain Maggi (Aru's)", "tags": ["quick", "simple", "comfort food", "budget"], "price": 30, "restaurant": "Aru's"},
    {"name": "Veg Masala Maggi (Aru's)", "tags": ["spicy", "quick", "comfort food", "vegetarian"], "price": 40, "restaurant": "Aru's"},
    {"name": "Egg Masala Maggi (Aru's)", "tags": ["spicy", "quick", "non-veg", "comfort food"], "price": 60, "restaurant": "Aru's"},
    {"name": "Paneer Roll (Aru's)", "tags": ["filling", "high protein", "quick", "snack"], "price": 80, "restaurant": "Aru's"},
    {"name": "Veg Roll (Aru's)", "tags": ["quick", "light", "vegetarian", "snack"], "price": 60, "restaurant": "Aru's"},
    {"name": "Veg Pakora (Aru's)", "tags": ["crispy", "warm", "vegetarian", "snack"], "price": 90, "restaurant": "Aru's"},
    {"name": "Paneer Pakora (Aru's)", "tags": ["crispy", "high protein", "warm", "snack"], "price": 150, "restaurant": "Aru's"},
    {"name": "Chicken Grilled Sandwich (Aru's)", "tags": ["non-veg", "quick", "grilled", "filling"], "price": 110, "restaurant": "Aru's"},
    {"name": "Chicken Kathi Roll (Aru's)", "tags": ["non-veg", "filling", "quick", "spicy"], "price": 120, "restaurant": "Aru's"},
    {"name": "Chicken Pakora (Aru's)", "tags": ["crispy", "non-veg", "snack", "spicy"], "price": 230, "restaurant": "Aru's"},
    {"name": "Chicken Burger (Aru's)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 90, "restaurant": "Aru's"},
    {"name": "Egg Roll (Aru's)", "tags": ["non-veg", "quick", "light", "snack"], "price": 80, "restaurant": "Aru's"},
 
    # ─── 6. Yellow Chilly ─────────────────────────────────────────────────────
 
    # Himachal Specials
    {"name": "Sweet Siddu (Yellow Chilly)", "tags": ["local", "sweet", "warm", "himachali"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Salt Burst Siddu (Yellow Chilly)", "tags": ["local", "savory", "warm", "himachali"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Mix Onion Siddu (Yellow Chilly)", "tags": ["local", "savory", "warm", "himachali"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Shobla Himachal (Yellow Chilly)", "tags": ["local", "traditional", "filling", "himachali"], "price": 180, "restaurant": "Yellow Chilly"},
 
    # Paneer
    {"name": "Paneer Bhurji (Yellow Chilly)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 180, "restaurant": "Yellow Chilly"},
    {"name": "Paneer Butter Masala (Yellow Chilly)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 100, "restaurant": "Yellow Chilly"},
    {"name": "Kadhai Paneer (Yellow Chilly)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Paneer Lababdar (Yellow Chilly)", "tags": ["rich", "high protein", "indulgent", "creamy"], "price": 100, "restaurant": "Yellow Chilly"},
    {"name": "Mutter Paneer (Yellow Chilly)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 90, "restaurant": "Yellow Chilly"},
    {"name": "Shahi Paneer (Yellow Chilly)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 250, "restaurant": "Yellow Chilly"},
 
    # Other Veg
    {"name": "Mix Veg (Yellow Chilly)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 110, "restaurant": "Yellow Chilly"},
    {"name": "Jeera Aloo (Yellow Chilly)", "tags": ["simple", "comforting", "home-style", "light"], "price": 100, "restaurant": "Yellow Chilly"},
    {"name": "Dal Makhani (Yellow Chilly)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 120, "restaurant": "Yellow Chilly"},
    {"name": "Dal Tadka (Yellow Chilly)", "tags": ["warm", "comforting", "balanced", "home-style"], "price": 90, "restaurant": "Yellow Chilly"},
    {"name": "Rajma (Yellow Chilly)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 70, "restaurant": "Yellow Chilly"},
    {"name": "Kadhi Pakoda (Yellow Chilly)", "tags": ["tangy", "comforting", "home-style", "warm"], "price": 150, "restaurant": "Yellow Chilly"},
 
    # Combos & Meals
    {"name": "Plain Chawal (Yellow Chilly)", "tags": ["simple", "light", "budget", "home-style"], "price": 60, "restaurant": "Yellow Chilly"},
    {"name": "Rajma Chawal (Yellow Chilly)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 50, "restaurant": "Yellow Chilly"},
    {"name": "Kadi Chawal (Yellow Chilly)", "tags": ["tangy", "comforting", "home-style", "filling"], "price": 50, "restaurant": "Yellow Chilly"},
    {"name": "Veg Thali (Yellow Chilly)", "tags": ["balanced", "vegetarian", "filling", "variety"], "price": 100, "restaurant": "Yellow Chilly"},
    {"name": "Special Thali (Yellow Chilly)", "tags": ["balanced", "premium", "filling", "variety"], "price": 180, "restaurant": "Yellow Chilly"},
    {"name": "Noodles+Manchurian+Momo Combo (Yellow Chilly)", "tags": ["filling", "combo", "comfort food", "variety"], "price": 180, "restaurant": "Yellow Chilly"},
    {"name": "Fried Rice + Manchurian Combo (Yellow Chilly)", "tags": ["filling", "combo", "comfort food", "quick"], "price": 140, "restaurant": "Yellow Chilly"},
 
    # Chinese
    {"name": "Veg Fried Rice (Yellow Chilly)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Manchurian (Yellow Chilly)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Paneer Chilli (Yellow Chilly)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 170, "restaurant": "Yellow Chilly"},
    {"name": "Mushroom Chilli (Yellow Chilly)", "tags": ["spicy", "earthy", "vegetarian", "bold"], "price": 160, "restaurant": "Yellow Chilly"},
    {"name": "Mushroom Fried Rice (Yellow Chilly)", "tags": ["earthy", "vegetarian", "filling", "comfort food"], "price": 100, "restaurant": "Yellow Chilly"},
    {"name": "Veg Noodles (Yellow Chilly)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Chilly Garlic Noodle (Yellow Chilly)", "tags": ["spicy", "bold", "vegetarian", "quick"], "price": 70, "restaurant": "Yellow Chilly"},
    {"name": "Hakka Noodle (Yellow Chilly)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 60, "restaurant": "Yellow Chilly"},
 
    # Snacks
    {"name": "Pakora Veg (Yellow Chilly)", "tags": ["crispy", "warm", "vegetarian", "snack"], "price": 60, "restaurant": "Yellow Chilly"},
    {"name": "Paneer Pakora (Yellow Chilly)", "tags": ["crispy", "high protein", "warm", "snack"], "price": 70, "restaurant": "Yellow Chilly"},
    {"name": "French Fries (Yellow Chilly)", "tags": ["crispy", "snack", "quick", "budget"], "price": 60, "restaurant": "Yellow Chilly"},
    {"name": "Sandwich (Yellow Chilly)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 60, "restaurant": "Yellow Chilly"},
    {"name": "Paneer Grilled Sandwich (Yellow Chilly)", "tags": ["filling", "high protein", "grilled", "quick"], "price": 90, "restaurant": "Yellow Chilly"},
    {"name": "Veg Burger (Yellow Chilly)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 50, "restaurant": "Yellow Chilly"},
    {"name": "Paneer Crispy Burger (Yellow Chilly)", "tags": ["crispy", "high protein", "filling", "vegetarian"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Spring Rolls (Yellow Chilly)", "tags": ["crispy", "light", "vegetarian", "snack"], "price": 60, "restaurant": "Yellow Chilly"},
    {"name": "Cheese Garlic Spring Rolls (Yellow Chilly)", "tags": ["cheesy", "crispy", "savory", "snack"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Bread Pakora (Yellow Chilly)", "tags": ["crispy", "budget", "snack", "comfort food"], "price": 50, "restaurant": "Yellow Chilly"},
 
    # Momos
    {"name": "Veg Momos (Yellow Chilly)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 50, "restaurant": "Yellow Chilly"},
    {"name": "Veg Fried Momos (Yellow Chilly)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 60, "restaurant": "Yellow Chilly"},
    {"name": "Paneer Momos (Yellow Chilly)", "tags": ["filling", "high protein", "steamed", "snack"], "price": 70, "restaurant": "Yellow Chilly"},
 
    # Beverages
    {"name": "Lemon Lime Soda (Yellow Chilly)", "tags": ["cold", "fizzy", "refreshing", "tangy"], "price": 40, "restaurant": "Yellow Chilly"},
    {"name": "Bloody Fang (Yellow Chilly)", "tags": ["cold", "unique", "refreshing", "bold"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Virgin Mojito (Yellow Chilly)", "tags": ["cold", "refreshing", "minty", "premium"], "price": 120, "restaurant": "Yellow Chilly"},
    {"name": "Lime Water (Yellow Chilly)", "tags": ["cold", "refreshing", "tangy", "light"], "price": 20, "restaurant": "Yellow Chilly"},
    {"name": "Strawberry Shake (Yellow Chilly)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 70, "restaurant": "Yellow Chilly"},
    {"name": "Oreo Shake (Yellow Chilly)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Vanilla Shake (Yellow Chilly)", "tags": ["cold", "sweet", "classic", "light"], "price": 70, "restaurant": "Yellow Chilly"},
    {"name": "Chocolate Shake (Yellow Chilly)", "tags": ["cold", "sweet", "comforting", "indulgent"], "price": 80, "restaurant": "Yellow Chilly"},
    {"name": "Tea (Yellow Chilly)", "tags": ["warm", "simple", "light", "budget"], "price": 20, "restaurant": "Yellow Chilly"},
    {"name": "Black Tea (Yellow Chilly)", "tags": ["warm", "light", "simple", "budget"], "price": 20, "restaurant": "Yellow Chilly"},
    {"name": "Green Tea (Yellow Chilly)", "tags": ["warm", "healthy", "light", "refreshing"], "price": 30, "restaurant": "Yellow Chilly"},
    {"name": "Lemon Tea (Yellow Chilly)", "tags": ["warm", "tangy", "refreshing", "light"], "price": 30, "restaurant": "Yellow Chilly"},
    {"name": "Coffee (Yellow Chilly)", "tags": ["warm", "comforting", "simple", "energizing"], "price": 40, "restaurant": "Yellow Chilly"},
    {"name": "Cold Coffee (Yellow Chilly)", "tags": ["cold", "energizing", "refreshing", "simple"], "price": 60, "restaurant": "Yellow Chilly"},
 
    # Desserts
    {"name": "Gulab Jamun (Yellow Chilly)", "tags": ["sweet", "warm", "dessert", "classic"], "price": 60, "restaurant": "Yellow Chilly"},
    {"name": "Brownie (Yellow Chilly)", "tags": ["sweet", "rich", "indulgent", "dessert"], "price": 110, "restaurant": "Yellow Chilly"},
    {"name": "Served Ice Cream (Yellow Chilly)", "tags": ["sweet", "cold", "light", "dessert"], "price": 60, "restaurant": "Yellow Chilly"},
 
    # ─── 7. Zaika Restaurant ──────────────────────────────────────────────────
 
    # Non-Veg Bites
    {"name": "Chicken Grilled Sandwich (Zaika)", "tags": ["non-veg", "quick", "grilled", "filling"], "price": 90, "restaurant": "Zaika Restaurant"},
    {"name": "Chicken Kathi Roll (Zaika)", "tags": ["non-veg", "filling", "quick", "spicy"], "price": 120, "restaurant": "Zaika Restaurant"},
    {"name": "Chicken Pakoda (Zaika)", "tags": ["crispy", "non-veg", "snack", "spicy"], "price": 190, "restaurant": "Zaika Restaurant"},
    {"name": "Chicken Burger (Zaika)", "tags": ["non-veg", "filling", "quick", "comfort food"], "price": 80, "restaurant": "Zaika Restaurant"},
    {"name": "Egg Roll (Zaika)", "tags": ["non-veg", "quick", "light", "snack"], "price": 80, "restaurant": "Zaika Restaurant"},
    {"name": "Chicken Fingers (Zaika)", "tags": ["crispy", "non-veg", "snack", "filling"], "price": 170, "restaurant": "Zaika Restaurant"},
    {"name": "Chilli Chicken (Zaika)", "tags": ["spicy", "non-veg", "bold", "comfort food"], "price": 210, "restaurant": "Zaika Restaurant"},
    {"name": "Lemon Chicken (Zaika)", "tags": ["tangy", "non-veg", "refreshing", "light"], "price": 220, "restaurant": "Zaika Restaurant"},
    {"name": "Garlic Chicken (Zaika)", "tags": ["savory", "non-veg", "bold", "aromatic"], "price": 230, "restaurant": "Zaika Restaurant"},
    {"name": "Lemon Coriander Chicken (Zaika)", "tags": ["tangy", "non-veg", "refreshing", "light"], "price": 230, "restaurant": "Zaika Restaurant"},
    {"name": "Chilli Fish (Zaika)", "tags": ["spicy", "non-veg", "seafood", "bold"], "price": 220, "restaurant": "Zaika Restaurant"},
 
    # Veg Quick Bites
    {"name": "Veg Sandwich (Zaika)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 40, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Grilled Sandwich (Zaika)", "tags": ["quick", "light", "grilled", "vegetarian"], "price": 50, "restaurant": "Zaika Restaurant"},
    {"name": "Cheese Grilled Sandwich (Zaika)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 80, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Burger (Zaika)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 50, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Cheese Burger (Zaika)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 60, "restaurant": "Zaika Restaurant"},
    {"name": "Plain Maggi (Zaika)", "tags": ["quick", "simple", "comfort food", "budget"], "price": 30, "restaurant": "Zaika Restaurant"},
    {"name": "Masala Maggi (Zaika)", "tags": ["spicy", "quick", "comfort food", "bold"], "price": 50, "restaurant": "Zaika Restaurant"},
    {"name": "Paneer Roll (Zaika)", "tags": ["filling", "high protein", "quick", "snack"], "price": 80, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Pakoda (Zaika)", "tags": ["crispy", "warm", "vegetarian", "snack"], "price": 90, "restaurant": "Zaika Restaurant"},
    {"name": "Paneer Pakoda (Zaika)", "tags": ["crispy", "high protein", "warm", "snack"], "price": 140, "restaurant": "Zaika Restaurant"},
 
    # Chinese Snacks (Zaika)
    {"name": "Crispy Chilli Potato (Zaika)", "tags": ["spicy", "crispy", "snack", "bold"], "price": 130, "restaurant": "Zaika Restaurant"},
    {"name": "Honey Chilli (Zaika)", "tags": ["sweet", "spicy", "crispy", "snack"], "price": 140, "restaurant": "Zaika Restaurant"},
    {"name": "Chilli Cauliflower (Zaika)", "tags": ["spicy", "vegetarian", "crispy", "snack"], "price": 160, "restaurant": "Zaika Restaurant"},
    {"name": "Chilli Mushroom (Zaika)", "tags": ["spicy", "earthy", "vegetarian", "snack"], "price": 150, "restaurant": "Zaika Restaurant"},
    {"name": "Chilli Paneer (Zaika)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 200, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Fried Rice (Zaika)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 90, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Chowmein (Zaika)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 45, "restaurant": "Zaika Restaurant"},
    {"name": "Hakka Noodles (Zaika)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 45, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Steam Momo (Zaika)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 60, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Fried Momo (Zaika)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 70, "restaurant": "Zaika Restaurant"},
 
    # Indian Veg (Zaika)
    {"name": "Veg Thali (Zaika)", "tags": ["balanced", "vegetarian", "filling", "variety"], "price": 120, "restaurant": "Zaika Restaurant"},
    {"name": "Special Thali (Zaika)", "tags": ["balanced", "premium", "filling", "variety"], "price": 180, "restaurant": "Zaika Restaurant"},
    {"name": "Poha (Zaika)", "tags": ["light", "simple", "quick", "home-style"], "price": 80, "restaurant": "Zaika Restaurant"},
    {"name": "Paneer Bhurji (Zaika)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 140, "restaurant": "Zaika Restaurant"},
    {"name": "Mix Veg (Zaika)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 110, "restaurant": "Zaika Restaurant"},
    {"name": "Jeera Aloo (Zaika)", "tags": ["simple", "comforting", "home-style", "light"], "price": 70, "restaurant": "Zaika Restaurant"},
    {"name": "Jeera Rice (Zaika)", "tags": ["light", "aromatic", "simple", "comforting"], "price": 80, "restaurant": "Zaika Restaurant"},
    {"name": "Chole Masala (Zaika)", "tags": ["spicy", "filling", "vegetarian", "bold"], "price": 110, "restaurant": "Zaika Restaurant"},
    {"name": "Dal Makhani (Zaika)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 140, "restaurant": "Zaika Restaurant"},
    {"name": "Paneer Do Pyaza (Zaika)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 180, "restaurant": "Zaika Restaurant"},
    {"name": "Mater Paneer (Zaika)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 170, "restaurant": "Zaika Restaurant"},
    {"name": "Shahi Paneer (Zaika)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 210, "restaurant": "Zaika Restaurant"},
    {"name": "Kadhi Paneer (Zaika)", "tags": ["tangy", "high protein", "comforting", "home-style"], "price": 190, "restaurant": "Zaika Restaurant"},
    {"name": "Paneer Butter Masala (Zaika)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 200, "restaurant": "Zaika Restaurant"},
    {"name": "Paneer Lababdar (Zaika)", "tags": ["rich", "high protein", "indulgent", "creamy"], "price": 190, "restaurant": "Zaika Restaurant"},
 
    # Indian Non-Veg (Zaika)
    {"name": "Chicken Masala (Zaika)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 200, "restaurant": "Zaika Restaurant"},
    {"name": "Kadhai Chicken (Zaika)", "tags": ["spicy", "non-veg", "bold", "comforting"], "price": 220, "restaurant": "Zaika Restaurant"},
    {"name": "Butter Chicken (Zaika)", "tags": ["creamy", "non-veg", "rich", "comforting"], "price": 230, "restaurant": "Zaika Restaurant"},
    {"name": "Rara Chicken (Zaika)", "tags": ["spicy", "non-veg", "bold", "filling"], "price": 250, "restaurant": "Zaika Restaurant"},
    {"name": "Chicken Curry (Zaika)", "tags": ["comforting", "non-veg", "home-style", "filling"], "price": 200, "restaurant": "Zaika Restaurant"},
    {"name": "Egg Curry (Zaika)", "tags": ["comforting", "high protein", "home-style", "simple"], "price": 130, "restaurant": "Zaika Restaurant"},
    {"name": "Egg Bhurji (Zaika)", "tags": ["high protein", "spicy", "quick", "simple"], "price": 70, "restaurant": "Zaika Restaurant"},
 
    # Pizza (Zaika)
    {"name": "Veg Pizza (Zaika)", "tags": ["vegetarian", "cheesy", "filling", "comfort food"], "price": 220, "restaurant": "Zaika Restaurant"},
 
    # Pasta (Zaika)
    {"name": "Veg Red Sauce Pasta (Zaika)", "tags": ["tangy", "vegetarian", "filling", "comfort food"], "price": 140, "restaurant": "Zaika Restaurant"},
    {"name": "Veg White Sauce Pasta (Zaika)", "tags": ["creamy", "vegetarian", "filling", "comfort food"], "price": 160, "restaurant": "Zaika Restaurant"},
    {"name": "Veg Mix Sauce Pasta (Zaika)", "tags": ["creamy", "tangy", "vegetarian", "filling"], "price": 170, "restaurant": "Zaika Restaurant"},
    {"name": "Mac & Cheese Veg (Zaika)", "tags": ["cheesy", "comforting", "vegetarian", "indulgent"], "price": 90, "restaurant": "Zaika Restaurant"},
    {"name": "Non-Veg Red Sauce Pasta (Zaika)", "tags": ["tangy", "non-veg", "filling", "comfort food"], "price": 160, "restaurant": "Zaika Restaurant"},
    {"name": "Non-Veg White Sauce Pasta (Zaika)", "tags": ["creamy", "non-veg", "filling", "comfort food"], "price": 180, "restaurant": "Zaika Restaurant"},
    {"name": "Non-Veg Mix Sauce Pasta (Zaika)", "tags": ["creamy", "tangy", "non-veg", "filling"], "price": 180, "restaurant": "Zaika Restaurant"},
    {"name": "Mac & Cheese Non-Veg (Zaika)", "tags": ["cheesy", "non-veg", "indulgent", "comfort food"], "price": 110, "restaurant": "Zaika Restaurant"},
 
    # Chaat
    {"name": "Samosa Chaat (Zaika)", "tags": ["tangy", "spicy", "snack", "street food"], "price": 60, "restaurant": "Zaika Restaurant"},
    {"name": "Aloo Chaat (Zaika)", "tags": ["tangy", "spicy", "snack", "street food"], "price": 50, "restaurant": "Zaika Restaurant"},
    {"name": "Peanuts Masala (Zaika)", "tags": ["spicy", "crunchy", "snack", "light"], "price": 90, "restaurant": "Zaika Restaurant"},
    {"name": "Fruit Chaat (Zaika)", "tags": ["fresh", "tangy", "light", "healthy"], "price": 90, "restaurant": "Zaika Restaurant"},
 
    # Breakfast (Zaika)
    {"name": "Aloo Pyaaz Paratha (Zaika)", "tags": ["filling", "comforting", "home-style", "budget"], "price": 35, "restaurant": "Zaika Restaurant"},
    {"name": "Gobhi Paratha (Zaika)", "tags": ["filling", "comforting", "home-style", "vegetarian"], "price": 40, "restaurant": "Zaika Restaurant"},
    {"name": "Mix Paratha (Zaika)", "tags": ["filling", "variety", "comforting", "home-style"], "price": 50, "restaurant": "Zaika Restaurant"},
    {"name": "Cheese Paratha (Zaika)", "tags": ["cheesy", "indulgent", "filling", "comforting"], "price": 70, "restaurant": "Zaika Restaurant"},
    {"name": "Paneer Paratha (Zaika)", "tags": ["filling", "high protein", "comforting", "home-style"], "price": 60, "restaurant": "Zaika Restaurant"},
    {"name": "Plain Paratha (Zaika)", "tags": ["simple", "light", "budget", "home-style"], "price": 20, "restaurant": "Zaika Restaurant"},
    {"name": "Muli Paratha (Zaika)", "tags": ["light", "home-style", "simple", "comforting"], "price": 50, "restaurant": "Zaika Restaurant"},
    {"name": "Dal Paratha (Zaika)", "tags": ["filling", "protein-rich", "home-style", "comforting"], "price": 40, "restaurant": "Zaika Restaurant"},
    {"name": "Onion Paratha (Zaika)", "tags": ["simple", "home-style", "comforting", "budget"], "price": 35, "restaurant": "Zaika Restaurant"},
    {"name": "Chole Bhature (Zaika)", "tags": ["filling", "energizing", "spicy", "classic"], "price": 90, "restaurant": "Zaika Restaurant"},
    {"name": "Bhaji Puri (Zaika)", "tags": ["filling", "spicy", "comfort food", "classic"], "price": 80, "restaurant": "Zaika Restaurant"},
    {"name": "Samosa (Zaika)", "tags": ["crispy", "snack", "street food", "budget"], "price": 15, "restaurant": "Zaika Restaurant"},
    {"name": "Egg Paratha (Zaika)", "tags": ["high protein", "filling", "comforting", "non-veg"], "price": 60, "restaurant": "Zaika Restaurant"},
    {"name": "Plain Omelette (Zaika)", "tags": ["high protein", "simple", "quick", "light"], "price": 30, "restaurant": "Zaika Restaurant"},
    {"name": "Masala Omelette (Zaika)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 40, "restaurant": "Zaika Restaurant"},
    {"name": "Bread Omelette (Zaika)", "tags": ["high protein", "filling", "quick", "budget"], "price": 50, "restaurant": "Zaika Restaurant"},
    {"name": "Cheese Omelette (Zaika)", "tags": ["cheesy", "high protein", "indulgent", "quick"], "price": 60, "restaurant": "Zaika Restaurant"},
 
    # ─── 8. Chai Vyanjan ──────────────────────────────────────────────────────
 
    # Chai
    {"name": "Adrak Chai (Chai Vyanjan)", "tags": ["warm", "comforting", "simple", "budget"], "price": 20, "restaurant": "Chai Vyanjan"},
    {"name": "Rose Chai (Chai Vyanjan)", "tags": ["warm", "aromatic", "light", "refreshing"], "price": 20, "restaurant": "Chai Vyanjan"},
    {"name": "Chocolate Chai (Chai Vyanjan)", "tags": ["warm", "sweet", "indulgent", "unique"], "price": 20, "restaurant": "Chai Vyanjan"},
    {"name": "Elaichi Chai (Chai Vyanjan)", "tags": ["warm", "aromatic", "comforting", "classic"], "price": 20, "restaurant": "Chai Vyanjan"},
    {"name": "Masala Chai (Chai Vyanjan)", "tags": ["warm", "spicy", "comforting", "energizing"], "price": 20, "restaurant": "Chai Vyanjan"},
    {"name": "Paan Chai (Chai Vyanjan)", "tags": ["warm", "unique", "aromatic", "refreshing"], "price": 22, "restaurant": "Chai Vyanjan"},
    {"name": "Kesar Chai (Chai Vyanjan)", "tags": ["warm", "aromatic", "premium", "comforting"], "price": 22, "restaurant": "Chai Vyanjan"},
    {"name": "Butter Scotch Chai (Chai Vyanjan)", "tags": ["warm", "sweet", "indulgent", "unique"], "price": 22, "restaurant": "Chai Vyanjan"},
    {"name": "Gurh Chai (Chai Vyanjan)", "tags": ["warm", "earthy", "natural", "comforting"], "price": 24, "restaurant": "Chai Vyanjan"},
 
    # Coffee
    {"name": "Hot Coffee (Chai Vyanjan)", "tags": ["warm", "comforting", "classic", "energizing"], "price": 45, "restaurant": "Chai Vyanjan"},
    {"name": "Black Coffee (Chai Vyanjan)", "tags": ["warm", "bold", "energizing", "simple"], "price": 45, "restaurant": "Chai Vyanjan"},
    {"name": "Strong Coffee (Chai Vyanjan)", "tags": ["warm", "bold", "energizing", "intense"], "price": 50, "restaurant": "Chai Vyanjan"},
    {"name": "Choco Coffee (Chai Vyanjan)", "tags": ["warm", "sweet", "indulgent", "comforting"], "price": 35, "restaurant": "Chai Vyanjan"},
    {"name": "Hazelnut Coffee (Chai Vyanjan)", "tags": ["warm", "aromatic", "premium", "sweet"], "price": 65, "restaurant": "Chai Vyanjan"},
    {"name": "Brush Coffee (Chai Vyanjan)", "tags": ["warm", "unique", "bold", "premium"], "price": 65, "restaurant": "Chai Vyanjan"},
 
    # Cold Coffee
    {"name": "Cold Coffee (Chai Vyanjan)", "tags": ["cold", "energizing", "refreshing", "classic"], "price": 105, "restaurant": "Chai Vyanjan"},
    {"name": "Choco Cold Coffee (Chai Vyanjan)", "tags": ["cold", "sweet", "indulgent", "energizing"], "price": 115, "restaurant": "Chai Vyanjan"},
    {"name": "Irish Coffee Cold (Chai Vyanjan)", "tags": ["cold", "premium", "bold", "rich"], "price": 125, "restaurant": "Chai Vyanjan"},
    {"name": "Hazelnut Cold Coffee (Chai Vyanjan)", "tags": ["cold", "aromatic", "premium", "sweet"], "price": 125, "restaurant": "Chai Vyanjan"},
 
    # Shakes
    {"name": "Mango Shake (Chai Vyanjan)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 105, "restaurant": "Chai Vyanjan"},
    {"name": "Strawberry Shake (Chai Vyanjan)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 105, "restaurant": "Chai Vyanjan"},
    {"name": "Butter Scotch Shake (Chai Vyanjan)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 105, "restaurant": "Chai Vyanjan"},
    {"name": "Pineapple Shake (Chai Vyanjan)", "tags": ["cold", "fruity", "tropical", "refreshing"], "price": 105, "restaurant": "Chai Vyanjan"},
    {"name": "Black Current Shake (Chai Vyanjan)", "tags": ["cold", "fruity", "unique", "sweet"], "price": 105, "restaurant": "Chai Vyanjan"},
    {"name": "Chocolate Shake (Chai Vyanjan)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 115, "restaurant": "Chai Vyanjan"},
    {"name": "Oreo Shake (Chai Vyanjan)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 125, "restaurant": "Chai Vyanjan"},
 
    # Summer Special
    {"name": "Nimboo Pani (Chai Vyanjan)", "tags": ["cold", "refreshing", "tangy", "light"], "price": 40, "restaurant": "Chai Vyanjan"},
    {"name": "Jaljeera (Chai Vyanjan)", "tags": ["cold", "tangy", "spicy", "refreshing"], "price": 40, "restaurant": "Chai Vyanjan"},
    {"name": "Aam Panna (Chai Vyanjan)", "tags": ["cold", "tangy", "sweet", "refreshing"], "price": 40, "restaurant": "Chai Vyanjan"},
    {"name": "Ice Tea (Chai Vyanjan)", "tags": ["cold", "refreshing", "light", "sweet"], "price": 70, "restaurant": "Chai Vyanjan"},
    {"name": "Lemon Ice Tea (Chai Vyanjan)", "tags": ["cold", "tangy", "refreshing", "light"], "price": 75, "restaurant": "Chai Vyanjan"},
 
    # Wraps
    {"name": "Herb Chilli Wrap (Chai Vyanjan)", "tags": ["spicy", "vegetarian", "filling", "quick"], "price": 125, "restaurant": "Chai Vyanjan"},
    {"name": "Vegetable Wrap (Chai Vyanjan)", "tags": ["light", "vegetarian", "quick", "balanced"], "price": 125, "restaurant": "Chai Vyanjan"},
    {"name": "CV Special Wrap (Chai Vyanjan)", "tags": ["signature", "filling", "spicy", "unique"], "price": 139, "restaurant": "Chai Vyanjan"},
    {"name": "Wow Paneer Wrap (Chai Vyanjan)", "tags": ["filling", "high protein", "vegetarian", "premium"], "price": 179, "restaurant": "Chai Vyanjan"},
    {"name": "Chicken Wow Wrap (Chai Vyanjan)", "tags": ["non-veg", "filling", "high protein", "premium"], "price": 189, "restaurant": "Chai Vyanjan"},
 
    # Burgers
    {"name": "Maska Bun (Chai Vyanjan)", "tags": ["simple", "light", "budget", "quick"], "price": 49, "restaurant": "Chai Vyanjan"},
    {"name": "Veg Surprise Burger (Chai Vyanjan)", "tags": ["quick", "vegetarian", "simple", "budget"], "price": 75, "restaurant": "Chai Vyanjan"},
    {"name": "Veg Delight Burger (Chai Vyanjan)", "tags": ["vegetarian", "filling", "quick", "simple"], "price": 79, "restaurant": "Chai Vyanjan"},
    {"name": "CV Special Burger (Chai Vyanjan)", "tags": ["signature", "filling", "vegetarian", "premium"], "price": 99, "restaurant": "Chai Vyanjan"},
    {"name": "Paneer Wow Burger (Chai Vyanjan)", "tags": ["high protein", "filling", "vegetarian", "premium"], "price": 149, "restaurant": "Chai Vyanjan"},
    {"name": "Chicken Wow Burger (Chai Vyanjan)", "tags": ["non-veg", "filling", "high protein", "premium"], "price": 165, "restaurant": "Chai Vyanjan"},
 
    # Sandwiches
    {"name": "Bombay Kaccha Sandwich (Chai Vyanjan)", "tags": ["tangy", "street food", "vegetarian", "quick"], "price": 109, "restaurant": "Chai Vyanjan"},
    {"name": "Bread Toast (Chai Vyanjan)", "tags": ["simple", "light", "quick", "budget"], "price": 109, "restaurant": "Chai Vyanjan"},
    {"name": "Veg Grill Sandwich (Chai Vyanjan)", "tags": ["quick", "light", "vegetarian", "grilled"], "price": 125, "restaurant": "Chai Vyanjan"},
    {"name": "CV Special Sandwich (Chai Vyanjan)", "tags": ["signature", "filling", "vegetarian", "premium"], "price": 139, "restaurant": "Chai Vyanjan"},
    {"name": "Paneer Sandwich (Chai Vyanjan)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 179, "restaurant": "Chai Vyanjan"},
 
    # Maggi
    {"name": "Hostel Maggi (Chai Vyanjan)", "tags": ["quick", "simple", "comfort food", "classic"], "price": 50, "restaurant": "Chai Vyanjan"},
    {"name": "Double Masala Maggi (Chai Vyanjan)", "tags": ["spicy", "quick", "comfort food", "bold"], "price": 60, "restaurant": "Chai Vyanjan"},
    {"name": "Veggie Maggi (Chai Vyanjan)", "tags": ["quick", "light", "vegetarian", "comfort food"], "price": 70, "restaurant": "Chai Vyanjan"},
    {"name": "Tandoori Maggi (Chai Vyanjan)", "tags": ["spicy", "smoky", "comfort food", "unique"], "price": 75, "restaurant": "Chai Vyanjan"},
    {"name": "CV Special Maggi (Chai Vyanjan)", "tags": ["signature", "indulgent", "comfort food", "premium"], "price": 75, "restaurant": "Chai Vyanjan"},
 
    # Snacks & Pasta
    {"name": "French Fries (Chai Vyanjan)", "tags": ["crispy", "snack", "quick", "comfort food"], "price": 105, "restaurant": "Chai Vyanjan"},
    {"name": "Peri Peri Fries (Chai Vyanjan)", "tags": ["spicy", "crispy", "bold", "snack"], "price": 115, "restaurant": "Chai Vyanjan"},
    {"name": "Tandoori Fries (Chai Vyanjan)", "tags": ["spicy", "smoky", "snack", "unique"], "price": 115, "restaurant": "Chai Vyanjan"},
    {"name": "CV Special Fries (Chai Vyanjan)", "tags": ["signature", "indulgent", "snack", "premium"], "price": 135, "restaurant": "Chai Vyanjan"},
    {"name": "Pizza Puff (Chai Vyanjan)", "tags": ["cheesy", "warm", "snack", "quick"], "price": 119, "restaurant": "Chai Vyanjan"},
    {"name": "Podi Idli (Chai Vyanjan)", "tags": ["South Indian", "spicy", "light", "unique"], "price": 149, "restaurant": "Chai Vyanjan"},
    {"name": "Red Sauce Pasta (Chai Vyanjan)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 115, "restaurant": "Chai Vyanjan"},
    {"name": "White Sauce Pasta (Chai Vyanjan)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 115, "restaurant": "Chai Vyanjan"},
    {"name": "Mix Sauce Pasta (Chai Vyanjan)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 125, "restaurant": "Chai Vyanjan"},
 
    # Desserts
    {"name": "Choco Lava Cake (Chai Vyanjan)", "tags": ["sweet", "warm", "indulgent", "dessert"], "price": 109, "restaurant": "Chai Vyanjan"},
    {"name": "Choco Walnut Brownie (Chai Vyanjan)", "tags": ["sweet", "rich", "indulgent", "dessert"], "price": 109, "restaurant": "Chai Vyanjan"},
    {"name": "Choco Brownie Sundae (Chai Vyanjan)", "tags": ["sweet", "indulgent", "premium", "dessert"], "price": 139, "restaurant": "Chai Vyanjan"},
    {"name": "Cookies (Chai Vyanjan)", "tags": ["sweet", "simple", "light", "snack"], "price": 19, "restaurant": "Chai Vyanjan"},
 
    # ─── 9. Friends Corner ────────────────────────────────────────────────────
 
    # Noodles
    {"name": "Veg Noodles (Friends Corner)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 60, "restaurant": "Friends Corner"},
    {"name": "Garlic Noodles (Friends Corner)", "tags": ["savory", "bold", "vegetarian", "quick"], "price": 130, "restaurant": "Friends Corner"},
    {"name": "Chilli Garlic Noodles (Friends Corner)", "tags": ["spicy", "bold", "vegetarian", "quick"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Gravy Noodles (Friends Corner)", "tags": ["saucy", "comforting", "vegetarian", "filling"], "price": 140, "restaurant": "Friends Corner"},
    {"name": "Mushroom Noodles (Friends Corner)", "tags": ["earthy", "vegetarian", "filling", "comfort food"], "price": 140, "restaurant": "Friends Corner"},
    {"name": "Paneer Noodles (Friends Corner)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Sezwaan Noodles (Friends Corner)", "tags": ["spicy", "bold", "vegetarian", "quick"], "price": 130, "restaurant": "Friends Corner"},
    {"name": "Singapuri Noodles (Friends Corner)", "tags": ["spicy", "unique", "vegetarian", "filling"], "price": 170, "restaurant": "Friends Corner"},
    {"name": "Hakka Noodles (Friends Corner)", "tags": ["quick", "vegetarian", "light", "comfort food"], "price": 130, "restaurant": "Friends Corner"},
 
    # Rice Dishes
    {"name": "Veg Fried Rice (Friends Corner)", "tags": ["filling", "vegetarian", "quick", "comfort food"], "price": 60, "restaurant": "Friends Corner"},
    {"name": "Mushroom Fried Rice (Friends Corner)", "tags": ["earthy", "vegetarian", "filling", "comfort food"], "price": 140, "restaurant": "Friends Corner"},
    {"name": "Paneer Fried Rice (Friends Corner)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Mix Fried Rice (Friends Corner)", "tags": ["variety", "filling", "vegetarian", "comfort food"], "price": 160, "restaurant": "Friends Corner"},
    {"name": "Crunchy Fried Rice (Friends Corner)", "tags": ["crispy", "unique", "vegetarian", "filling"], "price": 130, "restaurant": "Friends Corner"},
    {"name": "Schezwan Fried Rice (Friends Corner)", "tags": ["spicy", "bold", "vegetarian", "filling"], "price": 130, "restaurant": "Friends Corner"},
    {"name": "Chilli Garlic Fried Rice (Friends Corner)", "tags": ["spicy", "savory", "vegetarian", "bold"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Singapuri Fried Rice (Friends Corner)", "tags": ["spicy", "unique", "vegetarian", "filling"], "price": 170, "restaurant": "Friends Corner"},
    {"name": "Triple Veg Fried Rice (Friends Corner)", "tags": ["variety", "vegetarian", "filling", "balanced"], "price": 170, "restaurant": "Friends Corner"},
    {"name": "Jeera Rice (Friends Corner)", "tags": ["light", "aromatic", "simple", "comforting"], "price": 80, "restaurant": "Friends Corner"},
    {"name": "Plain Rice (Friends Corner)", "tags": ["simple", "light", "budget", "home-style"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Veg Biryani (Friends Corner)", "tags": ["aromatic", "vegetarian", "filling", "comfort food"], "price": 170, "restaurant": "Friends Corner"},
 
    # Mains (Chinese)
    {"name": "Veg Manchurian (Friends Corner)", "tags": ["spicy", "vegetarian", "comfort food", "bold"], "price": 130, "restaurant": "Friends Corner"},
    {"name": "Cheese Manchurian (Friends Corner)", "tags": ["cheesy", "spicy", "indulgent", "comfort food"], "price": 200, "restaurant": "Friends Corner"},
    {"name": "Paneer Chilli (Friends Corner)", "tags": ["spicy", "high protein", "vegetarian", "bold"], "price": 220, "restaurant": "Friends Corner"},
    {"name": "Mushroom Chilli (Friends Corner)", "tags": ["spicy", "earthy", "vegetarian", "bold"], "price": 170, "restaurant": "Friends Corner"},
    {"name": "Mushroom Manchurian (Friends Corner)", "tags": ["spicy", "earthy", "vegetarian", "comfort food"], "price": 170, "restaurant": "Friends Corner"},
 
    # Burgers & Wraps
    {"name": "Veg Burger (Friends Corner)", "tags": ["quick", "simple", "vegetarian", "budget"], "price": 50, "restaurant": "Friends Corner"},
    {"name": "Paneer Burger (Friends Corner)", "tags": ["filling", "high protein", "vegetarian", "quick"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Double Cheese Veg Burger (Friends Corner)", "tags": ["cheesy", "indulgent", "filling", "comfort food"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Aloo Cheese Wrap (Friends Corner)", "tags": ["cheesy", "quick", "vegetarian", "comfort food"], "price": 80, "restaurant": "Friends Corner"},
    {"name": "Paneer Cheese Wrap (Friends Corner)", "tags": ["cheesy", "high protein", "vegetarian", "filling"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Double Cheese Paneer Wrap (Friends Corner)", "tags": ["cheesy", "indulgent", "high protein", "filling"], "price": 120, "restaurant": "Friends Corner"},
 
    # Sandwiches
    {"name": "Veg Sandwich (Friends Corner)", "tags": ["quick", "light", "vegetarian", "budget"], "price": 80, "restaurant": "Friends Corner"},
    {"name": "Grilled Sandwich (Friends Corner)", "tags": ["quick", "light", "grilled", "vegetarian"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Double Cheese Grilled Sandwich (Friends Corner)", "tags": ["cheesy", "grilled", "indulgent", "filling"], "price": 120, "restaurant": "Friends Corner"},
    {"name": "Paneer Grill Sandwich (Friends Corner)", "tags": ["filling", "high protein", "grilled", "vegetarian"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Club Sandwich (Friends Corner)", "tags": ["loaded", "vegetarian", "filling", "premium"], "price": 180, "restaurant": "Friends Corner"},
    {"name": "Butter Toast (Friends Corner)", "tags": ["simple", "light", "quick", "budget"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Butter Jam Toast (Friends Corner)", "tags": ["sweet", "light", "quick", "simple"], "price": 80, "restaurant": "Friends Corner"},
 
    # Momos
    {"name": "Veg Momos (Friends Corner)", "tags": ["light", "healthy", "vegetarian", "snack"], "price": 50, "restaurant": "Friends Corner"},
    {"name": "Fried Momos (Friends Corner)", "tags": ["crispy", "vegetarian", "snack", "quick"], "price": 60, "restaurant": "Friends Corner"},
    {"name": "Crunchy Momos (Friends Corner)", "tags": ["crispy", "unique", "vegetarian", "snack"], "price": 90, "restaurant": "Friends Corner"},
    {"name": "Peri Peri Momos (Friends Corner)", "tags": ["spicy", "crispy", "bold", "snack"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Chilli Dry Momos (Friends Corner)", "tags": ["spicy", "dry", "vegetarian", "snack"], "price": 120, "restaurant": "Friends Corner"},
    {"name": "Chilli Gravy Momos (Friends Corner)", "tags": ["spicy", "saucy", "vegetarian", "filling"], "price": 140, "restaurant": "Friends Corner"},
 
    # Pasta & Soup
    {"name": "White Sauce Pasta (Friends Corner)", "tags": ["creamy", "comfort food", "vegetarian", "filling"], "price": 180, "restaurant": "Friends Corner"},
    {"name": "Red Sauce Pasta (Friends Corner)", "tags": ["tangy", "comfort food", "vegetarian", "filling"], "price": 170, "restaurant": "Friends Corner"},
    {"name": "Mix Sauce Pasta (Friends Corner)", "tags": ["creamy", "tangy", "comfort food", "filling"], "price": 180, "restaurant": "Friends Corner"},
    {"name": "Chilli Sauce Pasta (Friends Corner)", "tags": ["spicy", "vegetarian", "bold", "comfort food"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Mix Veg Soup (Friends Corner)", "tags": ["warm", "light", "healthy", "soup"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Hot n Sour Soup (Friends Corner)", "tags": ["warm", "tangy", "spicy", "soup"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Manchow Soup (Friends Corner)", "tags": ["warm", "spicy", "light", "soup"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Sweet Corn Soup (Friends Corner)", "tags": ["warm", "sweet", "light", "soup"], "price": 70, "restaurant": "Friends Corner"},
 
    # Snacks
    {"name": "French Fries (Friends Corner)", "tags": ["crispy", "snack", "quick", "comfort food"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Peri Peri Fries (Friends Corner)", "tags": ["spicy", "crispy", "bold", "snack"], "price": 130, "restaurant": "Friends Corner"},
    {"name": "Chilli Potato (Friends Corner)", "tags": ["spicy", "crispy", "snack", "bold"], "price": 140, "restaurant": "Friends Corner"},
    {"name": "Honey Chilli Potato (Friends Corner)", "tags": ["sweet", "spicy", "snack", "crispy"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Honey Cauliflower (Friends Corner)", "tags": ["sweet", "spicy", "vegetarian", "snack"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Veg Spring Rolls (Friends Corner)", "tags": ["crispy", "light", "vegetarian", "snack"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Crunchy Spring Roll (Friends Corner)", "tags": ["crispy", "unique", "vegetarian", "snack"], "price": 130, "restaurant": "Friends Corner"},
 
    # Thali & Indian
    {"name": "Friends Corner Thali", "tags": ["balanced", "filling", "variety", "premium"], "price": 180, "restaurant": "Friends Corner"},
    {"name": "Special Thali (Friends Corner)", "tags": ["balanced", "premium", "filling", "variety"], "price": 160, "restaurant": "Friends Corner"},
    {"name": "Regular Thali (Friends Corner)", "tags": ["balanced", "simple", "filling", "budget"], "price": 140, "restaurant": "Friends Corner"},
 
    # Main Course (Indian)
    {"name": "Dal Makhani (Friends Corner)", "tags": ["rich", "comforting", "warm", "home-style"], "price": 200, "restaurant": "Friends Corner"},
    {"name": "Mix Veg (Friends Corner)", "tags": ["balanced", "vegetarian", "comforting", "home-style"], "price": 200, "restaurant": "Friends Corner"},
    {"name": "Mutter Mushroom (Friends Corner)", "tags": ["earthy", "vegetarian", "balanced", "filling"], "price": 200, "restaurant": "Friends Corner"},
    {"name": "Kadahi Paneer (Friends Corner)", "tags": ["spicy", "high protein", "filling", "bold"], "price": 230, "restaurant": "Friends Corner"},
    {"name": "Paneer Bhurji (Friends Corner)", "tags": ["high protein", "spicy", "quick", "filling"], "price": 250, "restaurant": "Friends Corner"},
    {"name": "Mutter Paneer (Friends Corner)", "tags": ["comforting", "high protein", "home-style", "vegetarian"], "price": 230, "restaurant": "Friends Corner"},
    {"name": "Shahi Paneer (Friends Corner)", "tags": ["rich", "creamy", "high protein", "indulgent"], "price": 250, "restaurant": "Friends Corner"},
    {"name": "Paneer Butter Masala (Friends Corner)", "tags": ["rich", "creamy", "high protein", "comforting"], "price": 250, "restaurant": "Friends Corner"},
    {"name": "Lababdhar Paneer (Friends Corner)", "tags": ["rich", "high protein", "indulgent", "creamy"], "price": 240, "restaurant": "Friends Corner"},
    {"name": "Jeera Aloo (Friends Corner)", "tags": ["simple", "comforting", "home-style", "light"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Rajmah Masala (Friends Corner)", "tags": ["warm", "comforting", "filling", "home-style"], "price": 150, "restaurant": "Friends Corner"},
    {"name": "Mushroom Masala (Friends Corner)", "tags": ["earthy", "spicy", "vegetarian", "filling"], "price": 200, "restaurant": "Friends Corner"},
    {"name": "Kadi Tadka (Friends Corner)", "tags": ["tangy", "comforting", "home-style", "warm"], "price": 150, "restaurant": "Friends Corner"},
 
    # Breakfast
    {"name": "Aloo Prantha (Friends Corner)", "tags": ["comforting", "filling", "home-style", "simple"], "price": 50, "restaurant": "Friends Corner"},
    {"name": "Gobi Prantha (Friends Corner)", "tags": ["comforting", "filling", "home-style", "vegetarian"], "price": 60, "restaurant": "Friends Corner"},
    {"name": "Muli Prantha (Friends Corner)", "tags": ["light", "home-style", "simple", "comforting"], "price": 50, "restaurant": "Friends Corner"},
    {"name": "Mix Prantha (Friends Corner)", "tags": ["filling", "variety", "comforting", "home-style"], "price": 60, "restaurant": "Friends Corner"},
    {"name": "Paneer Prantha (Friends Corner)", "tags": ["filling", "high protein", "comforting", "home-style"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Onion Prantha (Friends Corner)", "tags": ["simple", "light", "comforting", "home-style"], "price": 50, "restaurant": "Friends Corner"},
    {"name": "Plain Prantha (Friends Corner)", "tags": ["simple", "light", "budget", "home-style"], "price": 30, "restaurant": "Friends Corner"},
    {"name": "Lacha Prantha (Friends Corner)", "tags": ["flaky", "comforting", "layered", "classic"], "price": 40, "restaurant": "Friends Corner"},
    {"name": "Chole Bhature (Friends Corner)", "tags": ["filling", "energizing", "spicy", "classic"], "price": 80, "restaurant": "Friends Corner"},
    {"name": "Puri Bhaji (Friends Corner)", "tags": ["filling", "spicy", "comfort food", "classic"], "price": 70, "restaurant": "Friends Corner"},
    {"name": "Poha (Friends Corner)", "tags": ["light", "simple", "easy to digest", "quick"], "price": 100, "restaurant": "Friends Corner"},
    {"name": "Tawa Roti (Friends Corner)", "tags": ["simple", "light", "budget", "home-style"], "price": 8, "restaurant": "Friends Corner"},
 
    # Beverages
    {"name": "Tea (Friends Corner)", "tags": ["warm", "simple", "light", "budget"], "price": 20, "restaurant": "Friends Corner"},
    {"name": "Black Coffee (Friends Corner)", "tags": ["warm", "bold", "energizing", "budget"], "price": 20, "restaurant": "Friends Corner"},
    {"name": "Hot Coffee (Friends Corner)", "tags": ["warm", "comforting", "simple", "energizing"], "price": 30, "restaurant": "Friends Corner"},
    {"name": "Cold Coffee (Friends Corner)", "tags": ["cold", "energizing", "refreshing", "simple"], "price": 60, "restaurant": "Friends Corner"},
    {"name": "Lemon Tea (Friends Corner)", "tags": ["warm", "tangy", "refreshing", "light"], "price": 20, "restaurant": "Friends Corner"},
    {"name": "Mint Mojito (Friends Corner)", "tags": ["cold", "refreshing", "minty", "energizing"], "price": 80, "restaurant": "Friends Corner"},
    {"name": "Blueberry Mojito (Friends Corner)", "tags": ["cold", "fruity", "refreshing", "sweet"], "price": 80, "restaurant": "Friends Corner"},
    {"name": "Green Apple Mojito (Friends Corner)", "tags": ["cold", "fruity", "refreshing", "unique"], "price": 100, "restaurant": "Friends Corner"},
 
    # Shakes
    {"name": "Banana Shake (Friends Corner)", "tags": ["cold", "filling", "energizing", "high protein"], "price": 90, "restaurant": "Friends Corner"},
    {"name": "Strawberry Shake (Friends Corner)", "tags": ["cold", "fruity", "sweet", "refreshing"], "price": 90, "restaurant": "Friends Corner"},
    {"name": "Chocolate Shake (Friends Corner)", "tags": ["cold", "sweet", "indulgent", "comforting"], "price": 90, "restaurant": "Friends Corner"},
    {"name": "Oreo Shake (Friends Corner)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 90, "restaurant": "Friends Corner"},
    {"name": "Vanilla Shake (Friends Corner)", "tags": ["cold", "sweet", "classic", "light"], "price": 90, "restaurant": "Friends Corner"},
    {"name": "Butter Scotch Shake (Friends Corner)", "tags": ["cold", "sweet", "indulgent", "comfort food"], "price": 90, "restaurant": "Friends Corner"},
]