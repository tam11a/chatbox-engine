from bot import Bot

# Get Response
while True:
    try:
        user_input = input('--> ')

        bot_response = Bot.get_response(user_input)

        print('Rheo: ', bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break