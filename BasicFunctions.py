from datetime import date
from datetime import datetime
from time import *
import re
import requests
import pytz

# VARIABLES AND DATAS
raw_git_repo_prefix: str = "https://raw.githubusercontent.com/KaziRifatMorshed/tbtku-website/main/articles/"


def get_tbtku_token() -> str:
    try:
        with open(f"/home/noobcoder_rtx/tbtKU.txt", 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        log_manager("!!! ERROR !!! FILE NOT FOUND at \'/home/noobcoder_rtx/tbtKU.txt\' input token plz:")
        t: str = input()
        return t


def get_tbtku_userName() -> str:
    return "@tbtku_bot"


def get_tbtku_tgbot_link() -> str:
    return f"https://t.me/tbtku_bot"

    # def log_printer_console(s: str) -> str:
    #     temp: str = f"{ctime()}:{s}"
    #     print(temp)
    #     return temp
    #


def raw_githubusercontent_finder(s: str) -> str:
    complete_RawGH_url: str = raw_git_repo_prefix + s + ".txt"  # complete web url
    # print(complete_RawGH_url)  # DEBUGGING PURPOSE
    web_content: str = requests.get(complete_RawGH_url).text  # complete webpage text
    # print(web_content)  # DEBUGGING PURPOSE
    # <pre style="word-wrap: break-word; white-space: pre-wrap;">..........</pre>
    # cpat = re.compile(r"<pre style=\"word-wrap: break-word; white-space: pre-wrap;\">.</pre>")
    # result: str = re.findall(cpat, web_content)  # filtered article text only
    # print(result)
    # return result
    return web_content


def log_printer_console(s: str) -> str:
    temp: str = f"{ctime()} : {s}"
    print(temp)
    return temp


def log_manager(s: str):
    log_per_line: str = log_printer_console(s)
    try:
        # with open(f"./logs/LOG_tbtKU_{time.strftime("%Y_%m_%d")}.txt", "a+") as f:
        with open(f"./logs/LOG_tbtKU_tgBOT_{date.today()}.txt", "a+") as f:
            str_to_write: str = log_per_line + "\n"
            f.write(str_to_write)
    except FileNotFoundError:
        print("FILE NOT FOUND || REMEMBER to create \"./logs/\" directory")


def log_activity_tracker():
    try:
        # Asia_Dhaka_tz = pytz.timezone('Asia/Dhaka')
        with open(f"./logs/LOG_log_activity_tracker_tgBOT_{date.today()}.txt", "a+") as f:
            str_to_write: str = + "\n"  # incomplete
            f.write(str_to_write)
    except FileNotFoundError:
        log_manager("for some reason \' log_activity_tracker()\' FAILED")


# def handle_response(_text: str) -> str:
#     # if any(w in text for w in []):
#     text: str = _text.lower()
#     if any(w in text for w in ['ku website', 'kuwebsite']):
#         return "please visit https://ku.ac.bd "
#     if any(w in text for w in ['morsos']):
#         return "ho, morsi"
#     if any(w in text for w in ['hi', 'hello', 'hola', 'hlw']):
#         # return f"Hi there !!!"
#         _current_hour: int = int(datetime.now().hour)
#         _current_greeting: str = ""
#         if 6 <= _current_hour < 12:
#             _current_greeting = "Morning"
#         elif 12 <= _current_hour < 16:
#             _current_greeting = "Noon"
#         elif 16 <= _current_hour < 19:
#             _current_greeting = "Afternoon"
#         else:
#             _current_greeting = "Evening"
#
#         return f"Hi there! Good {_current_greeting}!"
#
#     if 'tbtku website' in text:
#         return "please visit https://tbtku.github.io "
#     if any(w in text for w in ['who are you', 'কে তুমি', 'ke tumi', 'tui keda', 'তুই কেডা']):
#         return ("I am a computer program (aka BOT) for the online community tbtKU (Thoughts Behind The KU)\n["
#                 "https://www.facebook.com/tbtKU]")
#
#     return ("Sorry, I didn't understand that. I am still under development. If you have any suggestions, "
#             "please contact/inform @Napatheparacetamol.\nHope, I will continue this conversation like "
#             "a chatbot ;)")


def handle_response(_text: str) -> str:  # thanks to IA Seam 230201 for enhancing this function
    # if any(w in text for w in []):
    text: set = {re.sub(r'[^\w\s]', '', _text.lower())}

    if "tbtku website" in text:
        return "please visit https://tbtku.github.io "

    if len(set(["ku website", "kuwebsite", "website", "ku"]).intersection(text)) > 0:
        return "please visit https://ku.ac.bd "

    if len(set(["how are you"]).intersection(text)) > 0:
        return "I am fine ;)"

    if len(set(['hi', 'hello', 'hola', 'hlw']).intersection(text)) > 0:
        # return f"Hi there !!!"
        Asia_Dhaka_tz = pytz.timezone('Asia/Dhaka')
        _current_hour: int = int(datetime.now(Asia_Dhaka_tz).hour)
        _current_greeting: str = ""
        if 6 <= _current_hour < 12:
            _current_greeting = "Morning"
        elif 12 <= _current_hour < 16:
            _current_greeting = "Noon"
        elif 16 <= _current_hour < 19:
            _current_greeting = "Afternoon"
        else:
            _current_greeting = "Evening"

        return f"Hi there! Good {_current_greeting}!"

    if len(set(['who are you', 'কে তুমি', 'ke tumi', 'tui keda', 'তুই কেডা']).intersection(text)) > 0:
        return ("I am a computer program (aka BOT) for the online community tbtKU (Thoughts Behind The KU)\n["
                "https://www.facebook.com/tbtKU]")

    return ("Sorry, I didn't understand that. I am still under development.\nIf you have any suggestions, "
            "please fill this form https://forms.gle/KfTayNZj1kZktBF79 to share your feedback.\nHope, I will continue this conversation like "
            "a chatbot in future ;)")


def main():
    print("hello world")
    # print(raw_githubusercontent_finder("dummy/dummy_bangla"))


# token: str = get_tbtku_token()
# _whoami: str = os.system("whoami")
# print(token, " ", get_tbtku_userName(), " ")


if __name__ == '__main__':
    main()
