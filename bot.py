from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse
import requests,os
from openai import OpenAI

app = Flask(__name__)

@app.route("/", methods=["POST"])

def bot():
    IEX_CloudAPI_TOKEN = os.getenv("CloudAPI")
    client = OpenAI()

    # user input
    user_msg = request.values.get('Body', '').lower()

    # creating object of MessagingResponse
    response = MessagingResponse()

    # Help / welcome message.
    if user_msg in ("help"):

        response.message('''Hi, I'm a Bot 🤖. I can search google for you, provide real-time stock information, or we can Just talk. 

To search for information, reply with the word "search" followed by your search query and I'll return the top 3 Google results.
\n - For example, to search for Python, type: 'search python'.

Alternatively, To provide real-time stock information. Simply enter 'stock' followed by the stock ticket.
\n - For example, type: 'stock AAPL'.

Otherwise we can just talk. 
        ''')


    # google search - returning top 3 results
    elif user_msg.startswith('search'):
        #message before the loop
        response.message(f"Here are the top three Google results for '{user_msg[6:]}':")

        # searching and storing urls
        for url in search(user_msg[6:], num_results=3):
        # creating a separate message for each URL
            msg = response.message()
            msg.body(url)



    # stock market - returns current price, 52week high/low, and if the market is currently opened.
    elif user_msg.lower().startswith("stock"):
        symbol = user_msg[5:].strip()

        try:
            url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CloudAPI_TOKEN}'

            # Make a GET request to the API endpoint
            api_response = requests.get(url)
            data = api_response.json()

            is_market_open = 'Closed' if data['isUSMarketOpen'] == False else "Open"
            current_price = data['latestPrice']

            response.message(f''' {data['companyName']}\n
Current price: ${current_price}
52 week high : ${data['week52High']}
52 week low  : ${data['week52Low']}\n
market is currently {is_market_open}''')


        except:response.message(f"No stock ticket with the value '{symbol}' found on the US Stock Market. "

                     f"Please enter 'stock' followed by a valid ticket. \n"

                     f"For example, for Apple Inc., enter 'stock AAPL'.")



    # adding the openai api to the chat bot.
    else:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[

                {"role": "user", "content": user_msg}
            ]
        )

        chatgpt = completion.choices[0].message.content
        if "help" in user_msg:
            chatgpt += "\n \n Remember you can always type 'help' to see the various options on how to use this bot "

        response.message(chatgpt)





    return str(response)


if __name__ == "__main__":
    app.run()
