import os
import requests
from dotenv import load_dotenv

def get_user_input():
    name = input("What is your animal's name? ")
    return name

def load_data_from_api(name):
    """
    Loads and returns JSON data from an api endpoint.
    :param name:
    :param file_path: Path to the JSON file (not used anymore).
    :return: Parsed JSON data.
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'RcTj7nZso0kat5oeGilX8A==PdBWgVexlPBwB1Gt'})

    if response.status_code == requests.codes.ok:
        animals_data = response.json()
        return animals_data
    else:
        print("Error!", response.status_code, response.text)
        return []


def serialize_animal(animal):
    """
    Generates HTML string for one animal.

    :param animal: Dictionary containing animal data.
    :return: HTML string for the animal.
    """
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    locations = animal.get("locations", [])
    # in case of empty locations this will set 'Unknown' as the location
    location = locations[0] if locations else "Unknown"
    html_parts = [
        '<li class="cards__item">',
        f'<div class="card__title">{name}</div>',
        '<p class="card__text">',
        f'<strong>Diet:</strong> {diet}<br/>',
        f'<strong>Location:</strong> {location}<br/>'
    ]

    animal_type = characteristics.get("type")
    if animal_type:
        html_parts.append(f'<strong>Type:</strong> {animal_type}<br/>')
    else:
        html_parts.append('<br/>')

    html_parts.append('</p>')
    html_parts.append('</li>')

    return "\n".join(html_parts)



def generate_html(animals_data):
    """
    Iterates over list of animals and generates HTML string by calling serialize_animal()

    :param animals_data: List of dictionaries with animal data.
    :return: HTML string with formatted animal info.
    """
    return "\n".join(serialize_animal(animal) for animal in animals_data)


def inject_html(template_path, output_html, output_path, placeholder="__REPLACE_ANIMALS_INFO__"):
    """
    Replaces a placeholder in an HTML template and writes the result to a new file.

    :param template_path: Path to the HTML template file.
    :param output_html: HTML string to inject.
    :param output_path: Path to write the new HTML file.
    :param placeholder: Placeholder string to be replaced.
    """
    with open(template_path, "r", encoding="utf-8") as file:
        data = file.read()
        data = data.replace(placeholder, output_html)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(data)
    print("Website was successfully generated to the file animals.html.")


def main():
    name = get_user_input()
    animals_data = load_data_from_api(name)

    if not animals_data:
        print(f"Sorry, no animal found with the name '{name}'. Please try again with a different name.")
        return  # stop the program

    output_html = generate_html(animals_data)
    inject_html(
        template_path="animals_template.html",
        output_html=output_html,
        output_path="animals.html"
    )




if __name__ == "__main__":
    main()

