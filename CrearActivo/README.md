## 3.  Crear tu propio activo

El protocolo Algorand permite la creación de activos *on-chain* o *tokens* (criptomonedas personalizadas) que tendran la misma seguridad, compatibilidad, velocidad y facilidad de uso que el Algo. El nombre oficial de los activos en Algorand es *Activos Estándar de Algorand (ASA)*.
Los ASA se usan para representar monedas estables (*stablecoins*), recompensas por lealtad, créditos del sistema, puntos para un juego u objetos coleccionables, por nombrar sólo algunos. También pueden representar activos únicos, como la escritura de una casa, objetos coleccionables, piezas únicas en una cadena de suministro, etc. Además, existen funciones opcionales para imponer restricciones de transferencia a un activo, lo que ayuda a respaldar casos de uso de valores, cumplimiento y certificación. Si quieres conocer mas puedes consultar [la documentación para desarrolladores](https://developer.algorand.org/docs/features/asa/).

### 3.1 Crear un activo

Para crear tu propio activo en Algorand primero debes de tener una cuenta que será la cradora de dicho activo. Esta cuenta debe de tener como mínimo 10 algos. Le debes dar un nombre a este activo, un nombre de unidad, el número de décimales y una URL en la que puede obtenerse más información sobre el activo.

Existen 4 operaciones a realizar sobre activos: (1) Gestionar, (2) Reservar, (3) Congelar y (4) Recuperar. Cuando se crea el activo se debe indicar que dirección de cuenta puede realizar estas operaciones sobre este nuevo activo.

En el siguiente segmento de código podemos ver como se configura el nuevo activo usando el método `AssetConfigTxn`  el cual requiere indicar que dirección o direcciones tendrán los permisos para realizar las operaciones mencionadas. La creación de un activo es tratada como otra transacción por lo que después de crearla, se firma y se envía a la red.

```python
# La cuenta 1 crea un activo llamado MiMoneda y
# estabece los permisos para administrar, reservar, congelar y recuperar a la dirección de la cuenta 2

txn = AssetConfigTxn(
    sender=accounts[1]['pk'],
    sp=params,
    total=1000,
    default_frozen=False,
    unit_name="MIMONEDA",
    asset_name="MiMoneda",
    manager=accounts[2]['pk'],
    reserve=accounts[2]['pk'],
    freeze=accounts[2]['pk'],
    clawback=accounts[2]['pk'],
    url="https://path/to/my/asset/details",
    decimals=0)
# Se firma la transacción con la llave privada del creador 

stxn = txn.sign(accounts[1]['sk'])

# Se envía la transacción a la red de la misma manera que se describió previamente
```



Una vea creado nuestro activo podemos buscarlo en el explorador de Algorand usando el ID del activo.![Transaccion en AlgoExplorer](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/AssetExplorer.png)



### 3.2 Modificando un activo

Bla, bla...

### 3.3 Recibir un activo (*Opt.in*)

Antes de que una cuenta pueda recibir un activo específico, debe "optar" por recibirlo, es decir debe de realizar la operación de *opt-in*. 

La operación de *opt-in* es simplemente una transferencia de activos con una cantidad de 0, tanto hacia como desde la cuenta realizando dicha operación.

El siguiente código muestra esta operación donde podemos ver...



### 3.4  Transferir un activo

Los activos pueden transferirse entre cuentas que hayan optado por recibirlos (operación anterior). Son análogas a las transacciones de pago estándar, pero para los ASAs

.

### 3.5 Congelar un activo

Bla, bla...



### 3.6 Revocar un activo

Bla, bla...



### 3.7 Destruir un activo

Bla, bla...



> **Saldo mínimo**
>
> Cualquier cuenta Algorand debe mantener un saldo mínimo de 0,1 Algo para evitar que personas malintencionadas creen demasiadas cuentas, lo que podría hacer que el tamaño de la tabla de cuentas (almacenada por todos los nodos de la blockchain) explote.
> Por cada activo que una cuenta opte o cree, el saldo mínimo se incrementa en 0,1 Algo.

