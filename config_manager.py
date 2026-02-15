from typing import Dict, Any
import yaml
import logging

class ConfigurationManager:
    def __init__(self):
        self.config = {}
        logging.basicConfig(level=logging.INFO)

    def load_config(self, filepath: str) -> None:
        """Load configuration from a YAML file."""
        try:
            with open(filepath, 'r') as f:
                self.config = yaml.safe_load(f)
                logging.info("Configuration loaded successfully")
        except Exception as e:
            logging.error(f"Error loading configuration: {str(e)}")

    def get_config_value(self, key: str) -> Any:
        """Retrieve a value from the configuration."""
        return self.config.get(key)

    def update_config(self, updates: Dict[str, Any]) -> None:
        """Update configuration with new values."""
        try:
            self.config.update(updates)
            logging.info("Configuration updated successfully")
        except Exception as e:
            logging.error(f"Error updating configuration: {str(e)}")

    def save_config(self, filepath: str) -> None:
        """Save configuration to a YAML file."""
        try:
            with open(filepath, 'w') as f:
                yaml.dump(self.config, f)
                logging.info("Configuration saved successfully")
        except Exception as e:
            logging.error(f"Error saving configuration: {str(e)}")