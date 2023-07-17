<h1 align="center" style="border-botom: none">
  <b>
    🐍 Un metodo di campionamento a blocchi per serie storiche debolmente dipendenti 🐍     
  </b>
</h1>

Metodologia proposta nell'articolo del 1994 di [Politis & Romano](https://www.researchgate.net/publication/254287565_The_Stationary_Bootstrap).

## Problema
Quando si utilizzano modelli non parametrici per generare scenari o distribuzioni empiriche, i metodi di bootstrap si sono dimostrati strumenti potenti e facili da usare. Tuttavia, il bootstrap nella sua implementazione più semplice assume una serie temporale in cui le osservazioni sono indipendenti. In molte applicazioni questo non è il caso.

Un esempio di ciò è la modellazione dei tassi di interesse quando è necessario considerare i cicli economici. La presenza dei cicli economici rende la serie temporale debolmente dipendente nel tempo. Per tener conto di questa proprietà, vengono utilizzate tecniche di campionamento a blocchi.

## Soluzione

Bootstrap stazionario è una tecnica di campionamento a blocchi che rilassa l'assunzione di un bootstrap classico in cui il blocco di campionamento ha una lunghezza fissa. L'utente deve comunque specificare una lunghezza media, ma poiché questa viene poi applicata come una media statistica, blocchi più corti/più lunghi sono presenti anche nel campione finale.

L'algoritmo funziona selezionando casualmente un punto di partenza nella serie temporale e ad ogni passo aumenta la dimensione del blocco di uno o seleziona un nuovo blocco con un nuovo punto di partenza. Questa scelta avviene con una probabilità fissa governata dalla parametrizzazione.

### Input
 - Una serie temporale da campionare tramite bootstrap.
 - Il parametro `m` che descrive la durata media dei blocchi nel campione.
 - La lunghezza del campione di output.
 
 ### Output
  - Vettore di valori bootstrap della lunghezza specificata.

## Come iniziare
Data una serie temporale con i valori osservati 0.4, 0.2, 0.1, 0.4, 0.3, 0.1, 0.3, 0.4, 0.2, 0.5, 0.1 e 0.2, l'utente desidera generare un nuovo campione di lunghezza 9 in cui la dimensione media del blocco è 4.


```python
import numpy as np
from BootstrapStazionario import BootstrapStazionario

# Serie temporale originale
data = np.array([0.4,0.2,0.1,0.4,0.3,0.1,0.3,0.4,0.2,0.5,0.1,0.2])

# Lunghezza media del blocco
m = 4

# Lunghezza del campione di output
lunghezzaCampione = 12

risposta = BootstrapStazionario(data, m, lunghezzaCampione)

print(risposta)
```
