from services.summarizer import summarize

def test_summary():
    result = summarize("One. Two. Three.")
    assert result.startswith("One.")
