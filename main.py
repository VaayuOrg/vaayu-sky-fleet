import os

def create_sky_fleet_structure(base_dir="app"):
    structure = [
        f"{base_dir}/database/models",
        f"{base_dir}/factories/missions",
        f"{base_dir}/services",
        f"{base_dir}/api",
        f"{base_dir}/utils",
        "migrations",
        "tests"
    ]

    files = {
        f"{base_dir}/__init__.py": "",
        f"{base_dir}/main.py": "",
        f"{base_dir}/config.py": "# Configuration settings\n",
        f"{base_dir}/database/__init__.py": "",
        f"{base_dir}/database/db.py": "# SQLAlchemy setup\n",
        f"{base_dir}/database/models/__init__.py": "",
        f"{base_dir}/database/models/pilot.py": "# Pilot ORM model\n",
        f"{base_dir}/database/models/vehicle.py": "# UAV ORM model\n",
        f"{base_dir}/database/models/mission.py": "# Base mission model\n",
        f"{base_dir}/factories/__init__.py": "",
        f"{base_dir}/factories/mission_factory.py": "# Factory method for missions\n",
        f"{base_dir}/factories/missions/__init__.py": "",
        f"{base_dir}/factories/missions/agriculture.py": "# Agriculture mission class\n",
        f"{base_dir}/factories/missions/disaster.py": "# Disaster mission class\n",
        f"{base_dir}/factories/missions/inspection.py": "# Inspection mission class\n",
        f"{base_dir}/services/__init__.py": "",
        f"{base_dir}/services/pilot_service.py": "# Logic for pilots\n",
        f"{base_dir}/services/vehicle_service.py": "# Logic for UAVs\n",
        f"{base_dir}/services/mission_service.py": "# Logic for missions\n",
        f"{base_dir}/api/__init__.py": "",
        f"{base_dir}/api/pilot_routes.py": "# Pilot endpoints\n",
        f"{base_dir}/api/vehicle_routes.py": "# Vehicle endpoints\n",
        f"{base_dir}/api/mission_routes.py": "# Mission endpoints\n",
        f"{base_dir}/utils/__init__.py": "",
        f"{base_dir}/utils/validators.py": "# Input validation\n",
        f"{base_dir}/utils/helpers.py": "# Utility functions\n",
        "requirements.txt": "# Add your dependencies here\n",
        ".env": "# Environment variables\n",
        "README.md": "# Sky Fleet Manager\n",
        "migrations/__init__.py": "",
        "tests/__init__.py": "",
        "tests/test_pilot.py": "",
        "tests/test_vehicle.py": "",
        "tests/test_missions.py": ""
    }

    # Create directories
    for path in structure:
        os.makedirs(path, exist_ok=True)

    # Create files
    for path, content in files.items():
        with open(path, "w") as f:
            f.write(content)

    print("✅ Sky Fleet Manager project structure created successfully.")

if __name__ == "__main__":
    create_sky_fleet_structure()
