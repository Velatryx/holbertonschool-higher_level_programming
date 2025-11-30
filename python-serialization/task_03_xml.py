#!/usr/bin/python3
"""XML serialization and deserialization utilities."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): Output XML filename.
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Build XML tree and write to the file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Deserialize XML content into a Python dictionary.

    Args:
        filename (str): XML file to read.

    Returns:
        dict: Deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text  # XML stores everything as strings

        return result

    except Exception:
        return None
