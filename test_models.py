from models import Deck

import pytest

# Test to check if deck is created
def test_create_deck():
    deck = Deck()

    assert len(deck.playing_cards) == 40
    assert "Ac" in deck.playing_cards
    assert "7o" in deck.playing_cards
    assert "Kb" in deck.playing_cards
    assert "4e" in deck.playing_cards

# Test to check if deck is mixed
def test_mix_deck():
    deck = Deck()
    deck.playing_cards = []
    ordened_deck = deck.get_playing_cards()
    deck.shuffle()

    assert len(deck.playing_cards) == 40
    assert deck.playing_cards != ordened_deck

