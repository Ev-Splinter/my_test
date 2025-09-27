from pages.teams_button import TeamsButtonPage


def test_button1_clicked(browser):
    teams_page = TeamsButtonPage(browser)
    teams_page.open()
    teams_page.click_button()
    assert 'Counter-Strike World ranking on September 22nd, 2025' == teams_page.result_text()

