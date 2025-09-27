from pages.NaVi_Roster import NaviRosterPage


def test_button1_clicked(browser):
    teams_page = NaviRosterPage(browser)
    teams_page.open()
    teams_page.click_button()
    assert 'seized' == teams_page.result_text()
