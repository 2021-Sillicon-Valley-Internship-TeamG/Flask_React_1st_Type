##Server driver
from app import app

if __name__ == "__main__":
    #Load this config object for development mode
    app.config.from_object('config.DevelopmentConfig')
    app.run(debug=True)