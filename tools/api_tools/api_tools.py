from tools.api_tools.db_config import ConnDB as cDB


class MessHandler:

    @staticmethod
    def getmode(bot, update):
        connect = cDB.get_connect()
        cursor = cDB.get_cursor(connect)
        query = cDB.get_query_result(cursor, update)
        if query is None:
            update.message.reply_text('Пожалуйста,выберите один из модов:'
                                      '\n/crypt для зашифровки.' 
                                      '\n/encrypt для расшифровки.')
        else:
            mode = query[0]
            update.message.reply_text(f'Mode is {mode}')

        cursor.close()
        connect.close()

    @staticmethod
    def crypt(bot, update):
        connect = cDB.get_connect()
        cursor = cDB.get_cursor(connect)
        query = cDB.get_query_result(cursor, update)
        if query is None:
            cursor.execute(f"INSERT INTO users (userid, mode)"
                           f" VALUES ('{update.message.chat_id}', '{True}')")
            connect.commit()
        else:
            cursor.execute(f"UPDATE users SET mode='{True}' WHERE userid = '{update.message.chat_id}'")
            connect.commit()
        cursor.close()
        connect.close()

    @staticmethod
    def encrypt(bot, update):
        connect = cDB.get_connect()
        cursor = cDB.get_cursor(connect)
        query = cDB.get_query_result(cursor, update)
        if query is None:
            cursor.execute(f"INSERT INTO users (userid, mode)"
                           f" VALUES ('{update.message.chat_id}', '{False}')")
            connect.commit()
        else:
            cursor.execute(f"UPDATE users SET mode='{False}' WHERE userid = '{update.message.chat_id}'")
            connect.commit()
        cursor.close()
        connect.close()

    @staticmethod
    def start(bot, update):
        update.message.reply_text('Привет! Я бот,который переводит любой текст на русском языке в азбуку Морзе '
                                  'и обратно.'
                                  '\nПопробуй написать что-нибудь!')

    @staticmethod
    def text_handler(bot, update):
        text_message = update.message.text.lower()
        connect = cDB.get_connect()
        cursor = cDB.get_cursor(connect)
        query = cDB.get_query_result(cursor, update)
        if query is None:
            update.message.reply_text('Mode is not selected')
        else:
            mode = query[0]
            if not mode:
                dict2 = {'.- ': 'A', '-... ': 'Б', '.-- ': 'В', '--. ': 'Г', '-.. ': 'Д',
                         '. ': 'Е', '..--..--..--.. ': 'Ё', '...- ': 'Ж', '--.. ': 'З', '.. ': 'И', '.--- ': 'Й',
                         '-.- ': 'К', '.-.. ': 'Л', '-- ': 'М', '-. ': 'Н', '--- ': 'О',
                         '.--. ': 'П', '.-. ': 'Р', '... ': 'С', '- ': 'Т', '..- ': 'У',
                         '..-. ': 'Ф', '.... ': 'Х', '-.-. ': 'Ц', '---. ': 'Ч', '---- ': 'Ш',
                         '--.- ': 'Щ', '.--.-. ': 'Ъ', '-.-- ': 'Ы', '-..- ': 'Ь', '..-.. ': 'Э',
                         '..-- ': 'Ю', '.-.- ': 'Я', '.---- ': '1', '..--- ': '2', '...-- ': '3', '....- ': '4',
                         '..... ': '5', '....-': '6', '--... ': '7', '---.. ': '8', '----. ': '9', '----- ': '0',
                         '...... ': '.', '.-.-.- ': ',', '-..-. ': '/', '..--.. ': '?', '--..-- ': '!',
                         '.--.--. ': '@', '-····- ': '-'}

                input_str = text_message + ' '
                output_str = ''
                answer = ''

                for i in input_str:
                    output_str += i
                    if output_str == ' ':
                        answer += ' '
                        output_str = ''
                        continue
                    if output_str in dict2:
                        answer += dict2[output_str]
                        output_str = ''
                update.message.reply_text(answer.lower())
            else:
                dict1 = {'А': '.- ', 'Б': '-... ', 'В': '.-- ', 'Г': '--. ', 'Д': '-.. ',
                         'Е': '. ', 'Ё': '..--..--..--.. ', 'Ж': '...- ', 'З': '--.. ', 'И': '.. ', 'Й': '.--- ',
                         'К': '-.- ', 'Л': '.-.. ', 'М': '-- ', 'Н': '-. ', 'О': '--- ',
                         'П': '.--. ', 'Р': '.-. ', 'С': '... ', 'Т': '- ', 'У': '..- ',
                         'Ф': '..-. ', 'Х': '.... ', 'Ц': '-.-. ', 'Ч': '---. ', 'Ш': '---- ',
                         'Щ': '--.- ', 'Ъ': '.--.-. ', 'Ы': '-.-- ', 'Ь': '-..- ', 'Э': '..-.. ',
                         'Ю': '..-- ', 'Я': '.-.- ', '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ',
                         '5': '..... ', '6': '.... ', '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ',
                         '.': '...... ', ',': '.-.-.- ', '/': '-..-. ', '?': '..--.. ', '!': '--..-- ', '@': '.--.-. '}

                crypto = ''.join([dict1.get(c.upper(), ' ') for c in text_message])

                update.message.reply_text(crypto)

        cursor.close()
        connect.close()
