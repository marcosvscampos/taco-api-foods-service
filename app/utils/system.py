import os

def banner():
    app_version = os.environ.get("APP_VERSION")
    print(f"""
    ==============================
    TACO-API-FOOD-SERVICE 
    VERSION {app_version}         
    ==============================
    """)