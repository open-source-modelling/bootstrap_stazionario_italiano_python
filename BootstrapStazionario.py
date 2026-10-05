import numpy as np

def BootstrapStazionario(data: np.ndarray, m: float, lunghezzaCampione: int)-> np.ndarray:
    """
    Restituisce un campione bootstrap della serie temporale "data" di lunghezza "lunghezzaCampione".
    L'algoritmo utilizzato è il bootstrap stazionario di Politis & Romano del 1994.

    Argomenti:
        data ... ndarray unidimensionale. Un vettore di numeri che contiene la serie temporale dalla quale si fa il bootstrap.
        m    ... numero decimale positivo. Parametro per il bootstrap stazionario che indica la lunghezza media di ogni blocco nel campione.
        lunghezzaCampione ... numero intero positivo. Lunghezza del campione bootstrap restituito in output.


    Ritorna:
        campione ... ndarray unidimensionale di lunghezza lunghezzaCampione che contiene il campione bootstrap finale.

    Esempio di utilizzo:
    >>> import numpy as np
    >>> data = np.array([1,2,3,4,5,6,7,8,9,10])
    >>> m = 4
    >>> lunghezzaCampione = 12
    >>> BootstrapStazionario(data, m, lunghezzaCampione)
    Out[0]:  array([9., 3., 4., 5., 6., 7., 8., 7., 2., 3., 4., 2.])

    Articolo originale sul bootstrap stazionario:
    Dimitris N. Politis & Joseph P. Romano (1994) The Stationary Bootstrap, Journal of the American Statistical 
    Association, 89:428, 1303-1313, DOI: 10.1080/01621459.1994.10476870    

    Implementato da Gregor Fabjan di Open Source Modelling il 18/07/2023.
    """

    # Controllo degli input
    if m <= 0:
        raise ValueError("La lunghezza media del blocco 'm' deve essere positiva")
    if lunghezzaCampione <= 0:
        raise ValueError("La lunghezza del campione deve essere positiva")
    if not isinstance(data, np.ndarray):
        raise ValueError("data deve essere un numpy array")
    if data.size == 0:
        raise ValueError("data non può essere vuoto")
    if data.ndim != 1:
        raise ValueError("data deve essere un array unidimensionale")

    accetta  = 1/m
    lunghezzaDati  = data.shape[0]

    indiceCampione = np.random.randint(0,high =lunghezzaDati ,size=1)[0] # [0] perché l'indice sia uno scalare e non un array di lunghezza 1

    campione = np.zeros((lunghezzaCampione,))
    for iCampione in range(lunghezzaCampione):
        if np.random.uniform(0,1,1)>=accetta:
            indiceCampione += 1
            if indiceCampione >= lunghezzaDati :
                indiceCampione=0
        else:
            indiceCampione = np.random.randint(0,high = lunghezzaDati ,size=1)[0]

        campione[iCampione] = data[indiceCampione]
    return campione
