# Pilot ORM model

from datetime import datetime

class Pilot_Schema:
    def __init__(self, data: dict):
        self.pilot_id = data.get("pilot_id")
        self.name = data.get("name")
        self.email = data.get("email")
        self.phone = data.get("phone")
        self.license_id = data.get("license_id")
        self.certifications = data.get("certifications", []) 
        self.experience_years = data.get("experience_years", 0)
        self.specializations = data.get("specializations", [])  
        self.created_at = datetime.now()
