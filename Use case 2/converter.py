import json
import csv
import re
import logging
import yaml

logging.basicConfig(
    filename="conversion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config(config_path="config.yaml"):
    with open(config_path) as f:
        return yaml.safe_load(f)

def extract_record(record, fields):
    """Parse nested JSON safely, flattening contact info"""
    flat = {
        "id": record.get("id", ""),
        "name": record.get("name", ""),
        "email": record.get("contact", {}).get("email", ""),
        "phone": record.get("contact", {}).get("phone", "")
    }
    return {field: flat.get(field, "") for field in fields}

def validate_email(email):
    """Regex check — used as a data-quality example"""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email)) if email else False

def main():
    config = load_config()
    logging.info("Loaded config successfully")

    with open(config["input_path"]) as f:
        data = json.load(f)
    logging.info(f"Loaded {len(data)} records from {config['input_path']}")

    with open(config["output_path"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=config["fields"])
        writer.writeheader()
        for record in data:
            row = extract_record(record, config["fields"])
            if row["email"] and not validate_email(row["email"]):
                logging.warning(f"Invalid email format for record id={row['id']}")
            writer.writerow(row)
            logging.info(f"Converted record id={row['id']}")

    logging.info("Conversion complete")
    print(f"Done. Output written to {config['output_path']}")

if __name__ == "__main__":
    main()