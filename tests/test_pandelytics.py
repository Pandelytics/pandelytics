from . import __version__
import pandelytics.search as search

def test_version():
    assert __version__ == '0.1.0'

def test_jhu():
    news = search.search("jhu", "Data")
    assert len(news) == 264