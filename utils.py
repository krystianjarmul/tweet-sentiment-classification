from __future__ import annotations
from string import punctuation

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from spacy.lang.en.stop_words import STOP_WORDS
import spacy

stopwords = list(STOP_WORDS)
nlp = spacy.load("en_core_web_sm")


class Preprocessor(BaseEstimator, TransformerMixin):
    """Transformer class for tokenizing and cleaning a data"""
    def fit(self, X: pd.Series, y: pd.Series = None) -> Preprocessor:
        return self

    def transform(self, X: pd.Series, y: pd.Series = None) -> pd.Series:
        X_ = X.copy()
        X_ = X_.map(lambda row: self.preprocess(row))
        return X_

    @staticmethod
    def preprocess(tweet: str) -> str:
        doc = nlp(tweet)
        tokens = []
        for token in doc:
            if token.lemma_ != '-PRON-':
                new_token = token.lemma_.lower().strip()
            else:
                new_token = token.lower_
            if new_token not in punctuation and new_token not in stopwords:
                tokens.append(new_token)
        return ' '.join(tokens)
