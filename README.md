# Translator App

A simple translation application built with Streamlit and Hugging Face Transformers. This is my first machine learning application, designed to help users translate text between different languages using pre-trained models.

## Features

- Translate text between multiple languages.
- Select input and output languages from a dropdown menu.
- View translated text in an interactive chat interface.

## Installation

To get started, you need to have Python installed. Follow these steps to set up the project:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/translator-app.git
   cd translator-app
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   
    ```sh
      pip install -r requirements.txt
    ```
## Usage

1. **Run the Streamlit app:**

   ```sh
   streamlit run main.py
   ```

2. **Open your web browser and go to:**

   ```sh
   http://localhost:8501
   ```

3. **Use the dropdown menus to select input and translation languages. Enter text in the input field and click "Submit" to see the translation.**


## Configuration

- The `LANG_OPTIONS` dictionary in `languages.py` contains the available languages and their codes. You can add or remove languages as needed.
- The app uses Hugging Face's `Helsinki-NLP/opus-mt` models for translation. Ensure the selected language pair is supported by the model.


## Acknowledgements

- [Streamlit](https://streamlit.io) - For creating the interactive web app.
- [Hugging Face Transformers](https://huggingface.co/transformers/) - For providing pre-trained translation models.

## Contact

For questions or feedback, please open an issue on the [GitHub repository](https://github.com/m3r41ck/translator-app/issues).
