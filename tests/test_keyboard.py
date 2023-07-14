def test_keyboard_init(keyboard):
    assert str(keyboard) == 'Dark Project KD87A'
    assert str(keyboard.language) == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"


def test_mixinlog(keyboard):
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "EN"