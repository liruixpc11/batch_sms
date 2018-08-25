import chardet
from .model import load_from_excel
from .sms import send_sms


def main(phone_list_excel, default_msg_template_txt):
    with open(default_msg_template_txt, 'rb') as f:
        content = f.read()
        encoding = chardet.detect(content)['encoding']
        default_msg_template = content.decode(encoding)

    entries = load_from_excel(phone_list_excel, default_msg_template)

    for entry in entries:
        send_sms(entry.msg, entry.phone_number)
