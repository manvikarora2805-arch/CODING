import random
from colorama import Fore, Style, init

# Initialize colorama (required for Windows compatibility)
init(autoreset=True)

# ==========================================
# 5. Organize Code with Functions
# ==========================================

def get_weather():
    """Simulates weather responses."""
    weathers = ["Sunny and 25°C", "Rainy with a chance of thunderstorms", "Chilly and overcast"]
    return random.choice(weathers)

def get_news():
    """Simulates recent news updates."""
    news_headlines = [
        "Local cat climbs highest tree, successfully rescued!",
        "New breakthrough in pizza technology: crust is now fluffier.",
        "Scientists declare tomorrow is officially 'Stay in Bed' day."
    ]
    return random.choice(news_headlines)

def get_time():
    """Simulates local times in different cities."""
    times = [
        "New York: 02:00 AM",
        "London: 07:00 AM",
        "Tokyo: 03:00 PM"
    ]
    return "\n" + "\n".join(times)

# ==========================================
# 2. Improve Input Handling & Matching
# ==========================================
def chatbot_response(user_input):
    # Convert input to lowercase to handle variations (e.g., "Hi", "HI", "hi")
    user_input = user_input.lower()
    
    # 1. Expand Conversation Topics (Lists of keywords)
    greeting_keywords = ["hi", "hello", "hey", "sup"]
    weather_keywords = ["weather", "rain", "sun", "temperature"]
    news_keywords = ["news", "updates", "headlines"]
    time_keywords = ["time", "clock", "zone"]
    
    # Check for matches
    if any(word in user_input for word in greeting_keywords):
        # 3. Enhance User Interaction (Custom colors)
        return Fore.CYAN + "Hello there! How can I help you today?"
        
    elif any(word in user_input for word in weather_keywords):
        return Fore.YELLOW + f"Here is the simulated weather: {get_weather()}"
        
    elif any(word in user_input for word in news_keywords):
        return Fore.MAGENTA + f"Today's top headline: {get_news()}"
        
    elif any(word in user_input for word in time_keywords):
        return Fore.GREEN + f"Current world times:{get_time()}"
        
    elif "bye" in user_input or "exit" in user_input:
        return Fore.RED + "Goodbye! Have a wonderful day!"
        
    else:
        return Fore.WHITE + "I'm not sure I understand that. Try asking about the weather, news, or time!"

# ==========================================
# Main Chat Loop
# ==========================================
def main():
    print(Fore.BLUE + Style.BRIGHT + "=== Welcome to your Multi-Functional Chatbot! ===")
    print("Type 'weather', 'news', 'time', or 'bye' to exit.\n")
    
    while True:
        # Get input from the user
        user_input = input(Fore.WHITE + "You: ")
        
        # Get the chatbot's response
        response = chatbot_response(user_input)
        
        # Print the response
        print(f"Chatbot: {response}\n")
        
        # Break out of the loop if the user says goodbye
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main()