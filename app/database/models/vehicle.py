# UAV ORM model

from datetime import datetime

class Vehicle_Schema:
    def __init__(self, data: dict):
        # Basic Info
        self.vehicle_id = data.get("vehicle_id")
        self.name = data.get("name")
        self.model = data.get("model")
        self.manufacturer = data.get("manufacturer")
        self.type = data.get("type")  

        # Registration & Compliance
        self.registration_id = data.get("registration_id")
        self.certifications = data.get("certifications", [])

        # Performance Specs
        self.max_flight_time_minutes = data.get("max_flight_time_minutes", 0)
        self.max_range_km = data.get("max_range_km", 0)
        self.max_altitude_feet = data.get("max_altitude_feet", 0)
        self.max_speed_kmph = data.get("max_speed_kmph", 0)

        # Battery / Power
        self.battery_capacity_mah = data.get("battery_capacity_mah", 0)
        self.charge_cycles = data.get("charge_cycles", 0)

        # Payload & Sensors
        self.payload_capacity_kg = data.get("payload_capacity_kg", 0)
        self.sensor_package = data.get("sensor_package", [])  

        # Control & Communication
        self.controller_type = data.get("controller_type") 
        self.communication_protocol = data.get("communication_protocol")
        self.gnss_support = data.get("gnss_support", True)

        # Maintenance & Logs
        self.last_maintenance = data.get("last_maintenance")
        self.operational_status = data.get("operational_status", "active") 
        self.flight_logs = data.get("flight_logs", [])

        # Timestamps
        self.created_at = data.get("created_at", datetime.now())
        self.updated_at = data.get("created_at", datetime.now())
        