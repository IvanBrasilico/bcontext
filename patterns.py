'''Configuration of the routes, or vocabulary of the bot'''
from bottery.conf.patterns import Pattern, DefaultPattern
from bottery.views import pong
from botteryext.bcontext.patterns import first_word, FunctionPattern, HangUserPattern
from views import note_view, notebook_view, help_text, say_help
from app import ch


hang_user_pattern_notebook = HangUserPattern(notebook_view)
hang_user_pattern_note = HangUserPattern(note_view)

ch.set_hang(hang_user_pattern_notebook, 'notebook')
ch.set_hang(hang_user_pattern_note, 'note')


patterns = [
    hang_user_pattern_notebook,
    hang_user_pattern_note,
    FunctionPattern('notebook', notebook_view, first_word),
    FunctionPattern('note', note_view, first_word),
    Pattern('ping', pong),
    Pattern('help', help_text),
    DefaultPattern(say_help)
]
