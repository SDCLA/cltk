"""Module for tokenizers."""

from typing import List

from cltk.exceptions import UnknownLanguageError


def tokenizer_latin(text: str) -> List[str]:
    """Latin word tokenizer.

    >>> catiline = 'Quo usque tandem abutere'
    >>> tokenizer_latin(text=catiline)
    ['Quo', 'usque', 'tandem', 'abutere']
    """
    words = text.split(' ')
    return words


class Tokenize:
    """Class for word tokenizing."""

    def __init__(self, language: str) -> None:
        """Constructor for Tokenizer class.

        >>> tokenize = Tokenize(language='la')
        >>> catiline = 'Quo usque tandem abutere'
        >>> tokenize.tokenize_text(catiline)
        ['Quo', 'usque', 'tandem', 'abutere']

        >>> tokenize = Tokenize(language='id')
        Traceback (most recent call last):
          ...
        cltk.exceptions.exceptions.UnknownLanguageError
        """
        self.language = language
        if self.language == 'la':
            self.tokenizer = tokenizer_latin
        else:
            raise UnknownLanguageError

    def tokenize_text(self, text: str) -> List[str]:
        """Tokenize text with appropriate tokenizer."""
        tokens = self.tokenizer(text=text)
        return tokens
