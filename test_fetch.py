from playwright.sync_api import Page
from page_fetch import FetchPage


def test_find_fake_gold_bar(page: Page):

    expected_dialog_text = 'Yay! You find it!'
    gold_bars = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    fetch_page = FetchPage(page)

    fetch_page.navigate()

    fake_gold_bar = fetch_page.find_the_fake_gold_bar(gold_bars)

    actual_dialog_text = fetch_page.click_the_fake_gold_bar_and_get_dialog_text(fake_gold_bar)

    weighings_count = fetch_page.get_weighings_count()

    weighings_text = fetch_page.get_weighings_text()
    
    print(f"\nThe fake gold bar is number {fake_gold_bar}.")
    print(f"The text of the dialog is '{actual_dialog_text}'.")
    print(f"The fake gold bar was found in {weighings_count} weighings.")
    print(f"The weighings text is: \n{weighings_text}")

    assert actual_dialog_text == expected_dialog_text
