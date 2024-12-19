# ProPrompter

ProPrompter is a web application designed to help users generate structured prompts effortlessly. Built with Python and Flask, it offers a user-friendly interface for creating and managing prompt blocks.

## Features

- **Dynamic Prompt Generation:** Add, edit, and delete prompt blocks with ease.
- **Real-time Preview:** See the formatted prompt as you build it.
- **Copy to Clipboard:** Easily copy your generated prompt for use elsewhere.
- **Responsive Design:** Accessible on various devices with a clean and modern UI.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/ProPrompter.git
    cd ProPrompter
    ```

2. **Set Up Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Running the Application

### Locally

1. **Set Environment Variables**

    ```bash
    export PORT=8000
    ```

2. **Start the Server**

    ```bash
    python src/app.py
    ```

    The application will be accessible at `http://localhost:8000`.

### Using Docker

1. **Build the Docker Image**

    ```bash
    docker build -t prompter .
    ```

2. **Run the Docker Container**

    ```bash
    docker run -d -p 8000:8000 prompter
    ```

    The application will be accessible at `http://localhost:8000`.
