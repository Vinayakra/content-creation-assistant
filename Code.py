import google.generativeai as genai
genai.configure(api_key="AIzaSyCoYzJU2VHpaOgBq0CoElAuy_MyRJIhVhw")

model = genai.GenerativeModel("gemini-1.5-flash")

def get_user_input():
    print("\nLet's customize your Content Muse bot!")
    target_audience = input("Who is your target audience? (e.g., 'social media influencers', 'bloggers') ")
    platform = input("Which platform are you focusing on? (e.g., 'Instagram', 'YouTube', 'Blog') ")
    return target_audience, platform

def create_system_prompt(target_audience, platform):
    system_prompt = f"""
    You are a content creation assistant. You provide creative ideas for posts, videos, 
    blog articles, and content calendars tailored to {target_audience} on {platform}. 
    Be helpful, inspiring, and provide ideas that will engage the target audience on that platform.
    """
    return system_prompt

def generate_content_ideas(user_input, system_prompt):
    try:
        prompt = system_prompt + " " + user_input
        response = model.generate_content(prompt)
        if response:
            return response.text
        else:
            return "Hmm, I didn't catch that. Could you try asking differently?"
    except Exception as e:
        return f"An error occurred while generating content: {e}"

if __name__ == "__main__":
    while True:
        # Get target audience and platform from the user
        target_audience, platform = get_user_input()
        system_prompt = create_system_prompt(target_audience, platform)

        print(f"\nWelcome to Content Muse! Ask me for content ideas for {platform} and more.")
        
        while True:
            user_input = input(f"\nYou: What type of content are you looking for on {platform}? (e.g., 'post idea', 'video idea', etc.) ")
            if user_input.lower() == "exit":
                print("Goodbye! Happy creating!")
                exit()
            elif user_input.lower() == "change":
                # Breaks inner loop to re-prompt for audience and platform
                break
            else:
                response = generate_content_ideas(user_input, system_prompt)
                print(f"Bot: {response}")

# Instructions:
# - Type "exit" to end the program.
# - Type "change" to switch to a new target audience and platform.
