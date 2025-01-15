from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    #Utilisation du model llama
    model=Groq(id="llama-3.3-70b-versatile"),
    #Utilisation des outils de Yahoo Finance pour fetch l'information
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=[
        "Use tables to display data.",
    ],
    #show_tool_calls=True,
    #markdown=True,
    #Montrer les méthodes appelé par le model
    #debug_mode=True,

)
ask = input("Quel stock voulez-vous analyser en premier ? ")
ask2 = input("Quel stock voulez-vous analyser en second pour les comparez ? ")
question = ("Summarize and compare analyst recommendations and fundamentaks for "+ ask + ask2 +" and NVDA in french")
agent.print_response(question)