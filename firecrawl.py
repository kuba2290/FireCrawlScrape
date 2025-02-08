import os
import json
from datetime import datetime
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from pydantic import BaseModel


load_dotenv()

website_url = ""

# Initialize the FirecrawlApp with your API key
app  = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

class ExtractSchema(BaseModel):
 
    Target_Audience_Market: str
    Unique_Value_Propositions: str
    Your_Top_AI_Consulting_Questions_Answered: str

data = app.extract([
  website_url, 
], {
    'prompt': 'Extract the following information about the company, Target Audience_Market,Unique Value Propositions,Please provide detailed information in a well-structured format',
    'schema': ExtractSchema.model_json_schema(),
})
formatted_data = json.dumps(data['data'], indent=2, ensure_ascii=False)
print(formatted_data)
