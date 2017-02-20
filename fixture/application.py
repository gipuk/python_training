from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesion import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.sesion = SessionHelper(self)


    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def go_to_home(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def add_osoba(self, person):
        wd = self.wd
        wd.find_element_by_link_text("nowy wpis").click()
        # add_1st_name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(person.first_name)
        # add_middle_name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(person.middle)
        # add_2nd_name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(person.last)
        # add_nick
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(person.nick)
        # add_title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(person.title)
        # add_company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(person.company)
        # add_company_address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(person.comaddr)
        # add_private_tel
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(person.homenr)
        # add_mobile
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(person.mobile)
        # add_work_tel
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(person.worknr)
        # add_fax_no
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(person.faxnr)
        # add_email1
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(person.email_1)
        # add_email2
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(person.email_2)
        # add_email3
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(person.email_3)
        # add_homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(person.home_page)
        # add_birth
        wd.find_element_by_css_selector("body").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[19]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(person.year_b)
        # add_anniver=
        wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[20]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[20]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[13]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[13]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(person.year_a)
        wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[3]").click()
        # add_home_add
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(person.home_add)
        # add_home_tel
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(person.home_phone)
        # add_notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(person.note)
        # submit_accept
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_groups_page(self):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("grupy").click()


    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
