# Opsis API

## Description

The Opsis API is a simple yet powerful backend service designed to transform visual data into meaningful textual descriptions. Built with FastAPI, it provides a robust and scalable solution for integrating advanced image analysis capabilities into your applications. Whether you're building a content management system, an accessibility tool, or simply need to automate image tagging, Opsis offers a clean and efficient way to achieve accurate visual recognition.

## Installation

To get Opsis API up and running locally, follow these steps:

### 1. Clone the Repository

Start by cloning the project from GitHub:

```bash
git clone https://github.com/isaacszn/Opsis-API.git
cd Opsis-API
```

### 2. Set up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv opsis_env
source opsis_env/bin/activate  # On Windows use `opsis_env\Scripts\activate`
```

### 3. Install Dependencies

Install all the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your Google Gemini API key:

```ini
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

You can obtain a Google Gemini API key from the [Google AI Studio](https://aistudio.google.com/).

## Usage

After completing the installation, you can run the API and interact with its endpoints.

### 1. Run the FastAPI Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will now be accessible at `http://127.0.0.1:8000`.

### 2. Accessing the API

You can test the API using tools like `curl`, Postman, Insomnia, or by integrating it directly into your applications.

For example, to analyze an image, you can use `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your/image.jpg;type=image/jpeg"
```

Replace `/path/to/your/image.jpg` with the actual path to an image file on your system.

## Features

*   **Image Description**: Provides detailed, human-like descriptions of uploaded images.
*   **AI-Powered Analysis**: Leverages Google Gemini 2.5 Flash for advanced visual recognition.
*   **FastAPI Backend**: Built on a modern, high-performance web framework.
*   **CORS Enabled**: Supports Cross-Origin Resource Sharing for flexible client-side integration.
*   **Simple File Upload**: Straightforward API for handling image file uploads.

## Technologies Used

- **Python**: The primary programming language used for the backend.                  
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.    
- **Google Gemini AI**: Powers the image analysis and description generation.
- **Pydantic**: Data validation and settings management using Python type hints.
- **python-dotenv**: For loading environment variables from a `.env` file.
- **Uvicorn**:        | An ASGI web server implementation for Python.                  

## API Documentation

### GET /

**Description**: This endpoint serves as a simple health check for the API, indicating that the backend service is running.

**Request**:
```
No request body required.
```

**Response**:
```json
{
  "message": "Opsis back-end running!!"
}
```

**Errors**:
- No specific error responses for this endpoint beyond standard HTTP errors (e.g., 500 if the server is down).

### POST /analyze

**Description**: This is the main endpoint for image analysis. It receives an image file, sends it to the Google Gemini AI model for processing, and returns a detailed textual description of the image content.

**Request**:
This endpoint expects a `multipart/form-data` request containing an image file.

Example using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your/image.jpg;type=image/jpeg"
```

**Response**:
```json
{
  "success": true,
  "description": "This image features a detailed close-up of a vibrant red rose in full bloom. The petals are soft and velvety, with a slight sheen, and some water droplets are visible, suggesting it might have just rained or been watered. The lighting highlights the intricate layers of the petals and their deep red hue. The background is softly blurred, keeping the focus on the rose itself.",
  "filename": "image.jpg"
}
```

**Errors**:
- **400 Bad Request**: This error will be returned if there's an issue processing the image, the file is corrupted, or if the Gemini AI service encounters an error. The `error` field in the response will provide more details.
  ```json
  {
    "success": false,
    "error": "Failed to read image data"
  }
  ```

### Environment Variables

The following environment variable is required for the project to run:

*   **`GEMINI_API_KEY`**: Your API key for accessing the Google Gemini AI service.
    *   Example: `GEMINI_API_KEY="AIzaSyC0M..."`

## License

This project does not currently specify a license.

## Author Info

*   **LinkedIn**: [Isaac Ugochukwu](https://linkedin.com/in/isaac-ugochukwu)
*   **X (Twitter)**: [@zikk_szn](https://x.com/zikk_szn)

---
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?logo=fastapi&logoColor=white)
![Google Gemini AI](https://img.shields.io/badge/Google%20Gemini%20AI-Flash-4285F4?logo=google&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.24.0-F76900?logo=Uvicorn&logoColor=white)

[![Readme was generated by Dokugen](https://img.shields.io/badge/Readme%20was%20generated%20by-Dokugen-brightgreen)](https://www.npmjs.com/package/dokugen)