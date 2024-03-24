<h1 align="center">WhatsAppBot-OpenAI-Twilio-IEXCloud</h1>

<br>
<br>

WhatsApp bot integrating ChatGPT, live stock updates, and Google search. Users can interact with the bot to retrieve top Google search results, obtain live stock information (including current price, 52-week high, 52-week low, and market status), or engage in conversation with ChatGPT over WhatsApp messages.


**video**

<h1>Requirements</h1>

**Python Version** 

`Python: 3.7.1 or later`

<br>
  
**Python Libraries**

`• twilio`

`• flask`

`• requests`

`• googlesearch-python`

`• openai`

<br>

**Other Requirements**

`• Twilio account`

`• Tool for exposing a local server to the internet. I’ve used Local Tunnel but you can use ngrok or any other alternative,`
   
    • npm install -g localtunnel

<br>

**API Access**

For live stock updates and chatgpt integration you are going to need to make an account with api access on [OpenAI](https://openai.com/blog/openai-api) and [IEX cloud](https://iexcloud.io/data-group/market-data). IEX cloud provides a free 7 day trial and openAI provides some users with free credits for signing up otherwise they have a pay as you go model which can be toped up with as little as $5. 

Note: If you do not have access to the APIs or prefer not to use them, you can still utilize the bot's basic Google search functionality.


<br>

<h1>Installation</h1>
<br>

**1.) Install the required Python libraries**:

    • pip install -r requirements.txt
<br>

**2.) Update API keys in the env file with your own API keys.**
<br><br>


**3.) Run Flask:**

    • flask --app bot run
<br>

**4.) Run Local Tunnel:**

    • lt --port 5000
<br>
<br>
<br>
<h1>Setting Up Twilio</h1>

**1.) Create a Twilio account.**

**2.) Navigate to the Messaging -> try it out -> send a WhatsApp message.**

**3.) Configure the sandbox.**

**4.) Set up the forwarding URL (provided by Local Tunnel) in the sandbox settings.**

















