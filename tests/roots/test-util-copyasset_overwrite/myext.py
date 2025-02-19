from pathlib import Path

from sphinx.util.fileutil import copy_asset


def _copy_asset_overwrite_hook(app):
    css = app.outdir / '_static' / 'custom-styles.css'
    # html_static_path is copied by default
    css_content = css.read_text(encoding='utf-8')
    assert css_content == '/* html_static_path */\n', 'invalid default text'
    # warning generated by here
    copy_asset(
        Path(__file__).resolve().parent.joinpath('myext_static', 'custom-styles.css'),
        app.outdir / '_static',
    )
    # This demonstrates that no overwriting occurs
    css_content = css.read_text(encoding='utf-8')
    assert css_content == '/* html_static_path */\n', 'file overwritten!'
    return []


def setup(app):
    app.connect('html-collect-pages', _copy_asset_overwrite_hook)
    app.add_css_file('custom-styles.css')
