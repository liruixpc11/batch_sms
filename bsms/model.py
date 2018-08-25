from dataclasses import dataclass
import xlrd


@dataclass
class SnsEntry:
    phone_number: str = None
    msg_template: str = None
    additional_attrs: dict = None

    @property
    def msg(self):
        return self.msg_template.format(**self.additional_attrs)

    def __str__(self):
        return '{}: {}'.format(self.phone_number, self.msg)


def load_from_excel(excel_file_name, default_msg_template):
    attr_indices = {
        '手机号': None,
        '短信模板': None
    }
    additional_attrs = dict()

    workbook = xlrd.open_workbook(excel_file_name)
    sheet = workbook.sheet_by_index(0)

    for i in range(sheet.ncols):
        attr_name = str(sheet.cell_value(0, i)).strip()
        if not attr_name:
            continue

        if attr_name in attr_indices:
            attr_indices[attr_name] = i
        else:
            additional_attrs[attr_name] = i

    if attr_indices['手机号'] is None:
        raise Exception('没找到手机号字段')

    entries = []
    for i in range(1, sheet.nrows):
        phone_number = str(int(sheet.cell_value(i, attr_indices['手机号']))).strip()
        msg_template = (str(sheet.cell_value(i, attr_indices['短信模板'])).strip()
                        if attr_indices['短信模板'] is not None
                        else default_msg_template)
        if not msg_template:
            msg_template = default_msg_template

        entry = SnsEntry(phone_number=phone_number, msg_template=msg_template, additional_attrs=dict())

        for name, col in additional_attrs.items():
            entry.additional_attrs[name] = str(sheet.cell_value(i, col)).strip()

        entries.append(entry)

    return entries
