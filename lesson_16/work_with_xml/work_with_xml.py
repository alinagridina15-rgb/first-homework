import xml.etree.ElementTree as ET
import logging
import os

# Налаштовуємо логер
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_incoming_by_group_number(file_path, group_number):
    """
    Шукає group по number і повертає timingExbytes/incoming.
    Ігнорує групи без incoming.
    """
    try:
        tree = ET.parse(file_path)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None

    root = tree.getroot()

    for group in root.findall('group'):
        number_elem = group.find('number')
        if number_elem is None:
            continue

        number = number_elem.text.strip()
        if number != str(group_number):
            continue

        incoming_elem = group.find('timingExbytes/incoming')
        if incoming_elem is not None:
            incoming = incoming_elem.text.strip()
            logger.info(f"Group {group_number} incoming: {incoming}")
            return incoming
        else:
            logger.warning(f"Group {group_number} has no timingExbytes/incoming")
            return None

    # Якщо групу не знайдено
    all_numbers = [g.find('number').text.strip() for g in root.findall('group') if g.find('number') is not None]
    logger.info(f"Group {group_number} not found. Available groups: {', '.join(all_numbers)}")
    return None


file_path = os.path.join(os.path.dirname(__file__), 'groups.xml')

# Приклади виклику
get_incoming_by_group_number(file_path, 0)
get_incoming_by_group_number(file_path, 5)
get_incoming_by_group_number(file_path, 1)  # попередження, немає incoming
get_incoming_by_group_number(file_path, 101)  # групи немає
