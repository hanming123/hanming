from test_frame.app import App


def test_addmember():
    app = App()
    result = app.start().goto_main().goto_addresslist_page().goto_add_member().add_member()
    assert result == True
