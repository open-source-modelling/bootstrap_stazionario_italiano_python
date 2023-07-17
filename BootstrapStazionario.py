import numpy as np

def BootstrapStazionario(data: np.ndarray, m, lunghezzaCampione)-> np.ndarray:
    """
    Restituisce un campione bootstrap della serie temporale "data" di lunghezza "lunghezzaCampione".
    L'algoritmo utilizzato è il bootstrap stazionario di Politis & Romano del 1994.

    Argomenti:     
        data ... ndarray. Un vettore di numeri che contiene la serie temporale da qualle si fa il bootstrap.
        m    ... numero decimale. Parametro per il bootstrap stazionario che indica la lunghezza media di ogni blocco nel campione.
        lunghezzaCampione ... numero intero. Lunghezza del campione bootstrap restituito in output.
    
     
    Ritorna:     
        campione ... ndarray che contiene il campione bootstrap finale.
      
    Esempio di utilizzo:
    >>> import numpy as np
    >>> data = np.array([1,2,3,4,5,6,7,8,9,10])
    >>> m = 4
    >>> lunghezzaCampione = 12
    >>> BootstrapStazionario(data, m, lunghezzaCampione)
    Out[0]:  array([[9.],
                    [3.],
                    [4.],
                    [5.],
                    [6.],
                    [7.],
                    [8.],
                    [7.],
                    [2.],
                    [3.],
                    [4.],
                    [2.]])

    Articolo originale sul bootstrap stazionario:
    Dimitris N. Politis & Joseph P. Romano (1994) The Stationary Bootstrap, Journal of the American Statistical 
    Association, 89:428, 1303-1313, DOI: 10.1080/01621459.1994.10476870    

    mplementato da Gregor Fabjan di Open Source Modelling il 18/07/2023.
    """
    
    accetta  = 1/m  
    lunghezzaDati  = data.shape[0]

    indiceCampione = np.random.randint(0,high =lunghezzaDati ,size=1)

    campione = np.zeros((lunghezzaCampione,1))
    for iCampione in range(lunghezzaCampione):
        if np.random.uniform(0,1,1)>=accetta:
            indiceCampione += 1
            if indiceCampione >= lunghezzaDati :
                indiceCampione=0        
        else:
            indiceCampione = np.random.randint(0,high = lunghezzaDati ,size=1)

        campione[iCampione,0] = data[indiceCampione]
    return campione
