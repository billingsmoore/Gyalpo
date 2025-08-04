import json
from datetime import datetime
from pathlib import Path

def log_interaction(agent_name: str, user_input: str, response: str, log_dir: str = "./logs"):
    """Log agent interactions to JSON files"""
    # Ensure log directory exists
    Path(log_dir).mkdir(exist_ok=True)
    
    # Create log entry
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent_name,
        "input": user_input,
        "response": response
    }
    
    # Write to file (using timestamp in filename)
    filename = f"{datetime.now().strftime('%Y%m%d')}.json" # THIS MUST BE CHANGED FOR PRODUCTION
    filepath = Path(log_dir) / filename
    
    with open(filepath, 'a') as f:
        json.dump(log_entry, f, indent=2)
    
    return filepath