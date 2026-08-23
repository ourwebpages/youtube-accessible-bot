from bot.commands.start import HELP

def test_help_has_core_commands():
    for command in ("/yt", "/search", "/playlist", "/favorites", "/favorite", "/delete", "/stats"):
        assert command in HELP
