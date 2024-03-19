# Neckbeard

Neckbeard provides concise summaries of Reddit discussions relevant to your queries. It leverages Google Search for targeted content extraction and employs a locally-hosted language model for intelligent analysis.

## Functionality

- **Targeted Reddit Search:** Neckbeard uses the Google Custom Search API to pinpoint relevant Reddit threads based on your search query.
- **Reddit Content Extraction:** It gathers the original post content and pertinent comments from the identified Reddit discussions.
- **LLM-Powered Summarization:** The collected content is processed by a local Ollama language model to generate a concise summary of the discussions.

## Prerequisites

- **Python 3.x:** Ensure you have a compatible Python version installed.
- **API Keys:**
  - Google Custom Search API Key: Required for search functionality. Obtain one from the [Google API Console](https://console.cloud.google.com/apis/dashboard).
  - Voyage API Key: Required if using VoyageEmbeddings. Obtain one by signing up on Voyage's website (URL removed).
- **Ollama:**
  - Install Ollama: Refer to the Ollama documentation for setup instructions.
  - Download a compatible 7+ billion parameter model (e.g., Mistral, Dolphin).
  - Configure Ollama to run locally, ensuring the service endpoint is `http://localhost:11434`.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/repo-name.git
   ```

2. **Install virtualenv:**

   ```bash
   pip install virtualenv
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   # Activate the environment (instructions vary by OS)
   ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables:**

   - Open the `.env` file in the project's root directory.
   - Replace the placeholder values with your actual API keys:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key_here
     SEARCH_ENGINE_ID=your_search_engine_id_here
     VOYAGE_API_KEY=your_voyage_key_here
     ```

## Usage

1. **Run the script:**

   ```bash
   python neckbeard.py
   ```

2. **Enter your search query at the prompt.**

3. **Review the generated summary of relevant Reddit discussions.**

## Dependencies

- google-api-client
- requests
- langchain-community
- python-dotenv

## Notes

- **Experiment with Ollama models:** Explore different language models hosted on Ollama to tailor the summarization style to your preferences.
- **Rate Limits and Usage Costs:** Be mindful of API rate limits and potential costs associated with Google Custom Search and Voyage services.
