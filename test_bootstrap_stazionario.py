import numpy as np
import pytest
from BootstrapStazionario import BootstrapStazionario

DATI = np.array([0.4,0.2,0.1,0.4,0.3,0.1,0.3,0.4,0.2,0.5,0.1,0.2]) # Serie temporale originale

# Comportamento normale: l'output è un ndarray unidimensionale della lunghezza richiesta
def test_normale():
    risposta = BootstrapStazionario(DATI, 4, 12)
    assert isinstance(risposta, np.ndarray), "L'output non è un numpy ndarray."
    assert risposta.shape == (12,), "L'output non ha la forma richiesta."

# I valori del campione provengono dalla serie originale
def test_valori_validi():
    data = np.array([10, 20, 30, 40])
    risposta = BootstrapStazionario(data, 1.5, 15)
    assert np.all(np.isin(risposta, data)), "L'output contiene valori che non sono nella serie originale."

# Con un solo elemento, il campione ripete sempre quell'elemento
def test_un_solo_elemento():
    risposta = BootstrapStazionario(np.array([0.4]), 4, 4)
    assert np.array_equal(risposta, np.array([0.4, 0.4, 0.4, 0.4]))

# Campione di lunghezza 1
def test_campione_di_lunghezza_uno():
    risposta = BootstrapStazionario(np.array([0.5]), 4, 1)
    assert np.array_equal(risposta, np.array([0.5]))

# Lunghezza media del blocco maggiore della lunghezza del campione
def test_blocco_piu_lungo_del_campione():
    risposta = BootstrapStazionario(DATI, 20, 12)
    assert len(risposta) == 12

# Dati negativi
def test_dati_negativi():
    data = np.array([-0.4,0.2,-0.1,0.4,-0.3,0.1,-0.3,0.4,-0.2,-0.5,0.1,-0.2])
    risposta = BootstrapStazionario(data, 4, 12)
    assert np.all(np.isin(risposta, data))

# Lunghezza media del blocco non positiva
def test_lunghezza_blocco_non_valida():
    with pytest.raises(ValueError, match="'m' deve essere positiva"):
        BootstrapStazionario(np.array([1, 2, 3]), 0, 10)

# Lunghezza del campione non positiva
def test_lunghezza_campione_non_valida():
    with pytest.raises(ValueError, match="La lunghezza del campione deve essere positiva"):
        BootstrapStazionario(np.array([1, 2, 3]), 1.0, -5)

# Serie vuota
def test_dati_vuoti():
    with pytest.raises(ValueError, match="data non può essere vuoto"):
        BootstrapStazionario(np.array([]), 2.0, 5)

# Serie passata come colonna
def test_dati_in_colonna():
    with pytest.raises(ValueError, match="data deve essere un array unidimensionale"):
        BootstrapStazionario(DATI.reshape(-1, 1), 4, 12)

# Serie passata come lista invece di numpy array
def test_dati_non_numpy():
    with pytest.raises(ValueError, match="data deve essere un numpy array"):
        BootstrapStazionario(list(DATI), 4, 12)
