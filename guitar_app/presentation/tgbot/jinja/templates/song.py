from aiogram_dialog.widgets.text import Jinja

SONG_CHORDS_WITHOUT_TABS_TEMPLATE = Jinja(
    "Аккорды для песни '{{ song_title }}'\n"
    "{% for verse in verses %}"
    "{% if not verse.strings  %}"
    "\n\n{{ verse.title }}\n"
    "{% else %}"
    "\n\n{{ verse.title }}:\n"
    "{% for verse_string in verse.strings %}"
    "{% if verse_string.lyrics %}"
    "{% if not verse_string.chords %}"
    "{{ verse_string.space_between_chords }}"
    "{% else %}"
    "{% if verse_string.chords|length == 1 %}"
    "{{ verse_string.chords|join(' ', attribute='title') }} {{ verse_string.space_between_chords }}"
    "{% else %}"
    "{% for chord in verse_string.chords %}"
    "{% if loop.last %}"
    "{{ chord.title }} "
    "{% else %}"
    "{{ chord.title }} {{ verse_string.space_between_chords }}"
    "{% endif %}"
    "{% endfor %}"
    "{% endif %}"   
    "{% endif %}"
    "{% if verse_string.end_chords %}"
    "{{ verse_string.end_chords|join(' ', attribute='title')}}"
    "{% endif %}" 
    "\n\n{{ verse_string.lyrics|safe }}\n"
    "{% else %}"
    "{{ verse_string.chords|join(' ', attribute='title')}}\n"
    "{% endif %}"
    "{% endfor %}"
    "{% endif %}"
    "{% endfor %}"
)

SONG_CHORDS_WITH_TABS_TEMPLATE = Jinja(
    "Аппликатура аккордов для песни '{{ song_title }}'\n\n"
    "{% for chord in chords_tabs %}"
    "{{ chord.title }}:"
    "{{ chord.tab }}\n"
    "{% endfor %}"
) + SONG_CHORDS_WITHOUT_TABS_TEMPLATE
