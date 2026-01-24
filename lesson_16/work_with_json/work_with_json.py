import json
import logging
import os


logging.basicConfig(
    filename="json__hridina.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_json_files():
    folder_path = "."

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            try:
                with open(file_name, encoding="utf-8") as file:
                    json.load(file)
            except json.JSONDecodeError as error:
                logging.error(f"{file_name} is invalid JSON: {error}")


validate_json_files()
