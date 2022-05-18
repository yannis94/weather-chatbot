import bot

print("------- Weather chatbot ------\n")
while True:
    user_input = bot.ask_user()

    if user_input == "quit":
        break

    city = bot.get_city(user_input)

    if city == "":
        bot.show_error()
        continue
    elif city == 0:
        break

    data = bot.get_weather(city)
    bot.display_answer(data)

print("\nChatbot: Au revoir !")
