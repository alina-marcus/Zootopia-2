# 🐾 Zootopia - Animal Info Website Generator

This Python project uses the [API Ninjas Animal API](https://api-ninjas.com/api/animals) to fetch information about animals and automatically generate a styled HTML website displaying those details.

## 📁 Project Structure

Zootopia/
│
├── animals_web_generator.py # Main script for generating the website
├── data_fetcher.py # Module that fetches data from the API
├── animals_template.html # HTML template with a placeholder
├── animals.html # Automatically generated website (output)
├── .env # File storing your API key (optional)
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🚀 How It Works

1. The user types in the name of an animal (e.g., `cheetah`).
2. The script fetches animal data from the API.
3. If the animal is found, an HTML file is created using a template.
4. If the animal is not found, a friendly message is shown, and no file is created.

---

## ▶️ Getting Started

### Requirements

- Python 3.7+
- Internet connection
- API key from [API Ninjas](https://api-ninjas.com/register)

### Installation
1. Clone the repository: git clone https://github.com/your-username/zootopia.git -> cd zootopia
2. (Optional but recommended) Create a virtual environment: python3 -m venv .venv --> source .venv/bin/activate (On Windows: .venv\Scripts\activate)
3. Install dependencies: pip install -r requirements.txt 
4. Create a .env file and add your API key:
   API_KEY=your_api_key_here

### Run the App
python animals_web_generator.py

### Modules
data_fetcher.py
- Contains load_data_from_api(name) to fetch animal info.
- Loads the API key from the .env file.

animals_web_generator.py
- Calls load_data_from_api()
- Converts the data into HTML 
- Injects it into animals_template.html 
- Writes the final result into animals.html

### Example
What is your animal's name? cheetah
Website was successfully generated to the file animals.html.

### Error Handling
If no animal is found:
What is your animal's name? dragonbanana
Sorry, no animal found with the name 'dragonbanana'. Please try again with a different name.

### License
MIT License – feel free to use, modify, and distribute.

### Future Ideas
- Allow multiple animals to be searched at once
- Display animal images (if available)
- Improve the design with CSS and animations
