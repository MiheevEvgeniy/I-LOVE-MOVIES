from ui import *


class Loading(UI):
    def __init__(self):
        self.groupbox3 = None
        self.filter_time = None
        self.filter_category = None
        self.filter_status = None
        self.filter_mark = None
        self.filter_name = None
        self.config = None
    def load_settings(self):
        if self.config["application"]["filter_name"] == '1':
            self.filter_name.setChecked(False)
        else:
            self.filter_name.setChecked(True)

        if self.config["application"]["filter_mark"] == '1':
            self.filter_mark.setChecked(False)
        else:
            self.filter_mark.setChecked(True)

        if self.config["application"]["filter_status"] == '1':
            self.filter_status.setChecked(False)
        else:
            self.filter_status.setChecked(True)

        if self.config["application"]["filter_category"] == '1':
            self.filter_category.setChecked(False)
        else:
            self.filter_category.setChecked(True)

        if self.config["application"]["filter_date"] == '1':
            self.filter_time.setChecked(False)
        else:
            self.filter_time.setChecked(True)

        if self.config["application"]["check_add_func"] == '1':
            self.type_adding_btn.setChecked(False)
        else:
            self.type_adding_btn.setChecked(True)

        if self.config["application"]["filters_is_on"] == '1':
            self.groupbox3.setChecked(False)
        else:
            self.groupbox3.setChecked(True)

        if self.config["application"]["list_del_is_on"] == '1':
            self.groupbox2.setChecked(False)
        else:
            self.groupbox2.setChecked(True)

        if self.config["application"]["range_del_is_on"] == '1':
            self.groupbox.setChecked(False)
        else:
            self.groupbox.setChecked(True)