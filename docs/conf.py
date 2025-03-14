import os
import sys

# Основные настройки
project = 'ATCP'
copyright = '2025, Arigadam'
author = 'Arigadam'

# Версия проекта
release = '1.0.0'

# Список поддерживаемых языков
language = 'en'

# Кодировка исходных файлов
source_encoding = 'utf-8-sig'

# Директория с исходными файлами
source_parsers = {
    '.md': 'ecommonmark.parser.CommonMarkParser',
}

# Директория с шаблонами
templates_path = ['_templates']

# Директория с статическими файлами
static_path = ['_static']

# Список исключаемых файлов и директорий
exclude_patterns = ['_build', '__pycache__']

# Основной файл индекса
master_doc = 'index'

# Шаблон для главной страницы
html_theme = 'classic'

# Параметры шаблона
html_theme_options = {
    'canonical_url': 'https://atcp.readthedocs.io/',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'tyle_external_links': False,
    'vcs_pageview_mode': '',
    'tyle_nav_header_background': '#2980B9',
}

# Дополнительные статические файлы
html_static_path = ['_static']

# Настройки для PDF
latex_documents = [
    (master_doc, 'atcp.tex', 'ATCP Documentation', author, 'manual'),
]

# Настройки для EPUB
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_theme = 'default'
epub_tocdepth = 3
epub_language = language
epub_cover = ('_static/cover.png', '_static/cover.jpg')
epub_guide = ()

# Настройки для ссылок
extlinks = {
    'atcp': ('https://atcp.readthedocs.io/%s', 'atcp '),
}

# Автоматическое создание ссылок на исходный код
html_show_sourcelink = False

# Автоматическое создание ссылок на исходный код на GitHub
html_context = {
    'display_github': True,
    'github_user': 'wer310',
    'github_repo': 'atcp',
    'github_version': 'aster',
}
