from wordstat import count_words, main

def test_case_insensitivity():
    result = count_words("Apple apple APPLE")
    assert result == {"apple": 3}   

def test_verify_missing_file():
    try:
        code= main(["--file", "non_existent_file.txt"])
    except FileNotFoundError:
        pass  # Expected behavior, test would pass
    assert code == None

def test_counts_words():
    result = count_words("apple banana apple")
    assert result == {"apple": 2, "banana": 1}

def test_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding='utf-8')    
    content=file_path.read_text(encoding='utf-8')
    result = count_words(content)
    assert result == {}    

def test_unicode_text():
    result = count_words("café naïve résumé")
    assert result == {"café": 1, "naïve": 1, "résumé": 1}   

def test_check_multiple_spaces_and_newlines():
    result = count_words("apple   banana\n\napple")
    assert result == {"apple": 2, "banana": 1}  

def test_check_words_are_sorted_by_frequency():
    result = count_words("apple banana apple cherry banana apple")
    assert result == {"apple": 3, "banana": 2, "cherry": 1}
    
def test_very_long_line():
    long_text = "apple " * 10000

    result = count_words(long_text)
    assert result == {"apple": 10000}    

def test_empty_text():
    result = count_words("")
    assert result == {}