# # import requests



# # #API_KEY = "a1bd80233da64779b1277dbc9b5f0c20"

# # API_KEY ="BWAjIzei8VwZXdw8BSCMTBnkxjT7LKEj90UUXwhj"

# # url = f'https://api.thenewsapi.com/v1/news/headlines?locale=us&language=en&api_token={API_KEY}'

# # mainp = requests.get(url).json()


# # print(mainp)
# # article = mainp["data"]

# # head = []

# # for ar in article:
# #     head.append(ar["title"])

# # for i in range(15):
# #     print(f"{i+1} : {head[i]} \n")


# # import http.client, urllib.parse

# # conn = http.client.HTTPSConnection('api.thenewsapi.com')

# # params = urllib.parse.urlencode({
# #     'api_token': 'BWAjIzei8VwZXdw8BSCMTBnkxjT7LKEj90UUXwhj',
# #     'categories': 'business,tech',
# #     'limit': 3,
# #     })

# # conn.request('GET', '/v1/news/all?local=in&language=en&{}'.format(params))

# # res = conn.getresponse()
# # data = res.read()
# # record = data.decode('utf-8')
# # print(record)



# # pub_48565244df63a91c588714930796ea8473814

# from newsdataapi import NewsDataApiClient


# # API key authorization, Initialize the client with your API key

# api = NewsDataApiClient(apikey="pub_48565244df63a91c588714930796ea8473814")

# # You can pass empty or with request parameters {ex. (country = "us")}

# response = api.latest_api( q= "tech" , country = "in")

# rec = response["results"]

# for i in rec:
#     url = i["image_url"]
#     print(url)



# # import torch
# # from transformers import LLMTokenizer

# # def alter_paragraph_length(paragraph, desired_length):
# #     # Load the LLM model and tokenizer
# #     # model = LLMForSequenceClassification.from_pretrained("llm-base-uncased")
# #     tokenizer = LLMTokenizer.from_pretrained("llm-base-uncased")

# #     # Tokenize the paragraph
# #     inputs = tokenizer(paragraph, return_tensors="pt")

# #     # Get the attention mask
# #     attention_mask = inputs["attention_mask"]

# #     # Get the sequence length
# #     sequence_length = attention_mask.sum(dim=1)

# #     # If the sequence length is greater than the desired length, truncate it
# #     if sequence_length > desired_length:
# #         inputs["input_ids"] = inputs["input_ids"][:, :desired_length]
# #         attention_mask = attention_mask[:, :desired_length]

# #     # If the sequence length is less than the desired length, pad it
# #     elif sequence_length < desired_length:
# #         padding_length = desired_length - sequence_length
# #         inputs["input_ids"] = torch.cat((inputs["input_ids"], torch.zeros((1, padding_length), dtype=torch.long)), dim=1)
# #         attention_mask = torch.cat((attention_mask, torch.ones((1, padding_length), dtype=torch.long)), dim=1)

# #     # Decode the altered paragraph
# #     altered_paragraph = tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)

# #     return altered_paragraph

# # paragraph = input("Enter a paragraph: ")
# # desired_length = int(input("Enter the desired length: "))

# # altered_paragraph = alter_paragraph_length(paragraph, desired_length)

# # print("Altered paragraph:")
# # print(altered_paragraph)



# # from transformers import pipeline

# # generator = pipeline("text-generation", model="distilgpt2")

# # res = generator(
# #     "This code uses the Hugging Face Transformers library to load a pre-trained LLM model and tokenizer.",
# #     max_lenght = 30,
# #     num_return_sequence=2,
# # )

# # print(res)
# # import requests

# # def fetch_url_content(url):
# #     """
# #     Fetches and returns the content of the specified URL as a string.
    
# #     Args:
# #         url (str): The URL to fetch content from.
    
# #     Returns:
# #         str: The content of the URL as a string.
# #     """
# #     try:
# #         response = requests.get(url)
# #         response.raise_for_status()  # Raise an exception for HTTP errors
# #         return response.text
# #     except requests.RequestException as e:
# #         print(f"An error occurred: {e}")
# #         return None

# # # Example usage
# # if __name__ == "__main__":
# #     url = input("Enter the URL: ")
# #     content = fetch_url_content(url)
# #     if content:
# #         print("URL Content as a String:")
# #         print("---------------------------")
# #         print(content)
# #         print("---------------------------")





# "=HYPERLINK("https://docs.google.com/forms/d/e/1FAIpQLSdfSzV-0hkYcZcrgV2lFAuhJgElPrTpsQRIncG6UUzCuRRgiQ/viewform?usp=pp_url&entry.581641062="&B6&"&entry.1062411755="&D6&"&entry.894239866="&E6&"&entry.15512639="&F6&"&entry.1765478877="&G6&"&entry.427229365="&H6&"&entry.1864078634="&I6&"&entry.1453031967="&J6&"&entry.615507778="&K6&"&entry.1469028305="&L6&"&entry.1441539669="&M6&"&entry.1673348502="&N6&"&entry.1238521727="&O6&"&entry.246729773="&P6&"&entry.199671874="&Q6&"&entry.1111302310="&R6&"&entry.663148406="&S6&"&entry.503806731="&T6&"&entry.1693425787="&U6&"&entry.220058580="&V6&"&entry.1129945874="&W6&"&entry.1508907755="&X6&"&entry.175781118="&Y6&"&entry.352671470="&Z6&"&entry.364718028="&AA6&"&entry.643209679="&AB6&"&entry.1012643375="&AC6&"&entry.358621385="&AD6&"&entry.67405102="&AE6&"&entry.1717465049="&AF6&"&entry.1615824519="&AG6&"")

# "


# from transformers import pipeline

# generator = pipeline("summarization", model="distilgpt2")
# title = "Air Arabia launches early bird promotion on 500,000 seats from INR 5,727!"

# des = '''Air Arabia, the leading low-cost carrier in the Middle East and North Africa, unveiled an extraordinary early bird promotion called ‘super seat sale’ with discounted offers on 500,000 seats across the company’s entire network.  
# The promotion includes non-stop flights from India to three airports across the United Arab Emirates (Sharjah, Abu Dhabi, and Ras Al Khaimah) and beyond to other onward destinations like Milan, Warsaw, Krakow, Athens, Moscow, Baku, Tbilisi, Almaty and many more with fares starting from INR 5,727 one way. 
# This early bird offer is available for booking from September 30th to October 20th, 2024, with travel dates spanning from 1st March, 2025, to 25th October, 2025
# The INR 5,727 ticket sale extends to nonstop flights originating from Mumbai, Delhi, Ahmedabad, Jaipur, Nagpur, Kolkata, Goa, Bengaluru, Hyderabad, Chennai, Thiruvananthapuram, Kochi, Coimbatore, and Kozhikode into Sharjah, Abu Dhabi and Ras Al Khaimah in the United Arab Emirates, and beyond.'''

# promt = f'Based on the title of the news given as "{title}" and the description as "{des}.Provide me the summary of the news article in 150 words and in the form of paragrapgh'
    

# res = generator(
#     promt
# )
# text = res['summary_text']
# print(text)

# i= 101
# i_img = f'img_{i}'
# print(i_img)


# import random
# a=0
# while a<=10:   
#     print(round(random.uniform(0.3,0.4),3))
#     a+=1



import requests


q = "crypto"
url = f"https://newsdata.io/api/1/latest?apikey=pub_48565244df63a91c588714930796ea8473814&q={q}"

querystring = {"function":"TIME_SERIES_DAILY","symbol":"MSFT","outputsize":"compact","datatype":"json"}

headers = {
	"x-rapidapi-key": "2f1dbf33b3msh73039fb202106a4p1cbb8fjsn470251daac7c",
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
}

response = requests.get(url)

t = response.json()


# print(t["result"])
news = t["results"]

for i in news:
    print(i)


