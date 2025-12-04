# Tutor Agent Backend

## Setup

1. Copy the example environment file:
   ```bash
   cp backend/.env.example backend/.env
   ```

2. Edit `backend/.env` and replace `your_openai_api_key_here` with your actual OpenAI API key.

3. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   cd backend
   python main.py
   ```

## Important Security Note

Never commit your actual API keys to the repository. The `.env` file is ignored by git to prevent this.