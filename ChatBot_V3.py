print("🤖 Welcome to Customer Support Chatbot V3")

name = input("What is your name? ").strip()
print("👋 Nice to meet you, " + name + "!")

print("\nType 'exit' to quit at anytime")

while True:
    choice = input("\nHow can I help you today? ").strip().lower()
    
    if choice == "exit":
        print("👋 Goodbye " + name + "! Have a great day.")
        break
    
    elif "refund" in choice:
        print("💰 " + name + ", refunds take 3-5 working days.")
        
    elif "delivery" in choice:
        print("🚚 " + name + ", delivery usually takes 3-5 working days.")
        
    elif "price" in choice:
        print("💲 Prices are shown on the product pages.")
        
    elif "agent" in choice:
        print("👨‍💼 " + name + ", connecting you to a human agent...")
        
    elif "hello" in choice:
        print("Hello " + name + "! How can I help you?")
        
    else:
        print("🤔 Sorry " + name + ", I didn't understand that.")
    
