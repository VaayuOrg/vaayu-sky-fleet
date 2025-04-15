# Base mission model

from datetime import datetime

class Mission_Schema:
    def __init__(self, data: dict):
        # Mission Basics
        self.mission_id = data.get("mission_id")
        self.mission_name = data.get("mission_name")
        self.purpose = data.get("purpose") 
        self.description = data.get("description", "")
        self.status = data.get("status", "planned") 

        # Vehicle Assignment
        self.vehicle_id = data.get("vehicle_id")
        self.pilot_id = data.get("pilot_id")

        # Mission Timeline
        self.scheduled_start = data.get("scheduled_start")
        self.actual_start = data.get("actual_start")
        self.actual_end = data.get("actual_end")

        # Geo-coordinates / Area of Operation
        self.area_coordinates = data.get("area_coordinates", []) 
        self.altitude_ft = data.get("altitude_ft", 0)
        self.max_distance_km = data.get("max_distance_km", 0)

        # Environmental Data Collected
        self.pollutants_monitored = data.get("pollutants_monitored", []) 
        self.data_logs_uri = data.get("data_logs_uri")  

        # Risk and Safety
        self.weather_conditions = data.get("weather_conditions", "unknown")
        self.risks_identified = data.get("risks_identified", []) 
        self.emergency_protocol_triggered = data.get("emergency_protocol_triggered", False)

        # Performance Summary
        self.distance_covered_km = data.get("distance_covered_km", 0)
        self.flight_duration_minutes = data.get("flight_duration_minutes", 0)

        # Timestamp
        self.created_at = data.get("created_at", datetime.now())
        self.updated_at = data.get("updated_at", datetime.now())

