### les amis ne touchez a rien dans ce fichier s' il vous plait###

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Workshop Marketplace"
    debug: bool = True
    database_url: str = "sqlite:///./workshop.db"
    #database_url: str = "postgresql://postgres:postgremedic@localhost:5432/workshop_competition"
    
    # Sécurité pour la page des résultats : passer à True le jour J
    show_results: bool = False
    


settings = Settings()

