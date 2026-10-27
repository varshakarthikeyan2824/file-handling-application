from pathlib import Path

from wordstat import count_words, main


def test_case_insensitivity() -> None:
    result = count_words("Apple apple APPLE")
    assert result == {"apple": 3}


def test_verify_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "non_existent_file.txt"
    main(["--file", str(missing_file)])


def test_counts_words() -> None:
    result = count_words("apple banana apple")
    assert result == {"apple": 2, "banana": 1}


def test_empty_file(tmp_path: Path) -> None:
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")
    content = file_path.read_text(encoding="utf-8")
    result = count_words(content)
    assert result == {}


def test_unicode_text() -> None:
    result = count_words("café naïve résumé")
    assert result == {"café": 1, "naïve": 1, "résumé": 1}


def test_check_multiple_spaces_and_newlines() -> None:
    result = count_words("apple   banana\n\napple")
    assert result == {"apple": 2, "banana": 1}


def test_check_words_are_sorted_by_frequency() -> None:
    result = count_words("apple banana apple cherry banana apple")
    assert result == {"apple": 3, "banana": 2, "cherry": 1}


def test_very_long_line() -> None:
    long_text = "apple " * 10000

    result = count_words(long_text)
    assert result == {"apple": 10000}


def test_empty_text() -> None:
    result = count_words("")
    assert result == {}
