from playwright.sync_api import expect


class FetchPage:
    def __init__(self, page):
        self.page = page
        self.reset_button = page.get_by_text('Reset')
        self.weigh_button = page.locator('#weigh')        
        self.result_question_mark = page.get_by_text('?')
        self.result_operator = page.locator("xpath=//div[@class='result']/button")
        self.weighings = page.locator("xpath=//div[@class = 'game-info']")

    def navigate(self):
        self.page.goto("http://sdetchallenge.fetch.com/")

    def click_the_fake_gold_bar_and_get_dialog_text(self, fake_gold_bar):
        self.page.on("dialog", lambda dialog: (self.get_dialog_text(dialog.message), dialog.accept()))
        self.page.locator('#coin_' + fake_gold_bar).click()
        return dialog_text

    def click_reset(self):
        self.reset_button.click()

    def click_weigh(self):
        self.weigh_button.click()    

    def fill_bowl(self, left_or_right_bowl, gold_bar_list):
        for i in gold_bar_list:
            self.page.locator('#' + left_or_right_bowl + '_'+ i).fill(i)        

    def find_the_fake_gold_bar(self, all_gold_bars_list):
        suspicious_bars_list = [all_gold_bars_list[x:x+3] for x in range(0, len(all_gold_bars_list), 3)]
        suspicious_bars_count = len(suspicious_bars_list)

        while suspicious_bars_count > 1:
            suspicious_bars_list = self.weigh_and_evaluate_the_gold_bars(suspicious_bars_list[0], suspicious_bars_list[1], suspicious_bars_list[2])
            suspicious_bars_count = len(suspicious_bars_list)

        return suspicious_bars_list            

    def get_dialog_text(self, dialog_message):
        global dialog_text
        dialog_text = dialog_message
        return dialog_text
    
    def get_result_text(self):
        return self.result_operator.inner_text()
    
    def get_weighings_count(self):
        return self.weighings.locator('li').count()

    def get_weighings_text(self):
        return self.weighings.inner_text()
    
    def wait_for_weighing(self):
        expect(self.result_question_mark).not_to_be_visible(timeout=10000)

    def weigh_and_evaluate_the_gold_bars(self, left_list, right_list, unweighed_list):
        self.click_reset()
        self.fill_bowl("left", left_list)
        self.fill_bowl("right", right_list)
        self.click_weigh()
        self.wait_for_weighing()    

        result_operator = self.get_result_text()
        match result_operator:
            case '<':
                remaining_bars = left_list
            case '>':
                remaining_bars = right_list
            case '=':
                remaining_bars = unweighed_list

        return remaining_bars
    