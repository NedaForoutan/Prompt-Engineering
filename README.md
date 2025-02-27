# Prompt-Engineering
Prompts for generating and detecting misinformation using Llama, Vicuna, and OpenAI models.

## Overview  
This repository contains prompt engineering scripts designed for **generating and detecting misinformation** using **Llama, Vicuna, and OpenAI models**. These scripts demonstrate how to design prompts to generate a dataset of misinformation using large language models (LLMs) and how to leverage LLMs for misinformation detection. The repository provides a foundation for studying AI-generated misinformation and developing improved detection strategies.

## Scripts  

### 1️⃣ Prompt-using-Llama-and-Vicuna.py  
**Description:**  
- Uses **Meta's Llama-2-7b** and **LMSYS's Vicuna-7b-v1.3** to generate misinformation by paraphrasing misleading content.  
- The script loads both models, tokenizes an input passage, and generates new text while keeping the original message intact.  

**Dependencies:**  
- `transformers`
- `torch`
- `accelerate`
- `huggingface_hub`  

**Usage:**  
1. Install dependencies:  
   ```sh
   pip install transformers torch accelerate huggingface_hub

2. Run the script:
python prompts/Prompt-using-Llama-and-Vicuna.py

3. Output is saved in misinfo_generated.txt

   
2️⃣ Prompt-using-OpenAI.py
Description:

  * Uses OpenAI's GPT-4o to generate misinformation and then detects whether a given passage is misinformation.
  * The script also prompts ChatGPT to determine if a passage is misinformation, returning either "YES" or "NO".
    
Dependencies:
  - openai
  - python-dotenv (optional for API key management)
  
Usage:
  1- Install dependencies:
    pip install --upgrade openai python-dotenv
    
  2- Set up your OpenAI API Key in the script:
    OPEN_API_KEY = "your_openai_api_key"
   
  3- Run the script:
    python prompts/Prompt-using-OpenAI.py
 
  4- Outputs are the misinformation generation and the misinformation detection result for the given text.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.  
