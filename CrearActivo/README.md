## 3.  Crear y administrar tu propio activo

El protocolo Algorand permite la creación de activos *on-chain* o *tokens* (criptomonedas personalizadas) que tendran la misma seguridad, compatibilidad, velocidad y facilidad de uso que el Algo. El nombre oficial de los activos en Algorand es *Activos Estándar de Algorand (ASA)*.
Los ASA se usan para representar monedas estables (*stablecoins*), recompensas por lealtad, créditos del sistema, puntos para un juego u objetos coleccionables, por nombrar sólo algunos. También pueden representar activos únicos, como la escritura de una casa, objetos coleccionables, piezas únicas en una cadena de suministro, etc. Además, existen funciones opcionales para imponer restricciones de transferencia a un activo, lo que ayuda a respaldar casos de uso de valores, cumplimiento y certificación.

### 3.1 Crear un activo

Para crear tu propio activo en Algorand primero debes de tener una cuenta que será la cradora de dicho activo. Esta cuenta debe de tener como mínimo 10 algos. Le debes dar un nombre a este activo, un nombre de unidad, el número de décimales y una URL en la que puede obtenerse más información sobre el activo.

Existen 4 operaciones a realizar sobre activos: (1) Gestionar, (2) Reservar, (3) Congelar y (4) Recuperar. Cuando se crea el activo se debe indicar que dirección de cuenta puede realizar estas operaciones sobre este nuevo activo.

En el siguiente segmento de código podemos ver como se configura el nuevo activo usando el método `AssetConfigTxn`  el cual requiere indicar que dirección o direcciones tendrán los permisos para realizar las operaciones mencionadas. La creación de un activo es tratada como otra transacción por lo que después de crearla, se firma y se envía a la red.

```python
# La cuenta 1 crea un activo llamado MiMoneda y
# estabece los permisos para administrar, reservar, congelar y recuperar a la dirección de la cuenta 2

txn = AssetConfigTxn(
    sender=accounts[0],
    sp=params,
    total=1000,
    default_frozen=False,
    unit_name="MIMONEDA",
    asset_name="MiMoneda",
    manager=accounts[1],
    reserve=accounts[1],
    freeze=accounts[1],
    clawback=accounts[1],
    url="https://path/to/my/asset/details",
    decimals=0)
# Se firma la transacción con la llave privada del creador 

stxn = txn.sign("{}".format(SKs[0]))

# Se envía la transacción a la red de la misma manera que se describió previamente
```

Una vea creado nuestro activo podemos buscarlo en el explorador de Algorand usando el ID del activo.![Transaccion en AlgoExplorer](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/AssetExplorer.png)

### 3.2 Modificando un activo

Una vez creado un activo, sólo se pueden modificar las direcciones de las cuentas que tendrán  permisos para realizar las operaciones mencionadas anteriormente. El resto de los parámetros están bloqueados durante la vida del activo. 

Si alguna de estas direcciones se establece en "", la dirección previa se desactivará y nunca podrá restablecerse durante la vida del activo. Sólo la cuenta gestora puede realizar y autorizar cambios de configuración.

En el siguiente código se muestra la modificación del administrador de un activo.

```python
# Cambiando administrador
# El administrador actual (la cuenta 2) emite una transacción de configuración de activos que asigna la cuenta 1 como nuevo administrador. El resto de las operaciones quedan igual.

txn = AssetConfigTxn(
    sender=accounts[1],
    sp=params,
    index=asset_id,
    manager=accounts[0],
    reserve=accounts[1],
    freeze=accounts[1],
    clawback=accounts[1])

# La transacción se firma por el administrador actual (la cuenta 2)

stxn = txn.sign(SKs[1])

# Esperamos por la confirmación de la transacción
# Se envía la transacción a la red
try:
    txid = algod_client.send_transaction(stxn)
    print("Signed transaction with txID: {}".format(txid))
    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4) 
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))   
except Exception as err:
    print(err)
```

### 3.3 Recibir un activo (*Opt.in*)

Antes de que una cuenta pueda recibir un activo específico, debe "optar" por recibirlo, es decir debe de realizar la operación de *opt-in*. 

La operación de *opt-in* es simplemente una transferencia de activos con una cantidad de 0, tanto hacia como desde la cuenta realizando dicha operación.

El siguiente código muestra esta operación para la cuenta 3.

```python
# Verificar si asset_id esta en la cuenta 3 antes del opt-in
account_info = algod_client.account_info(accounts[2])
holding = None
idx = 0
for my_account_info in account_info['assets']:
    scrutinized_asset = account_info['assets'][idx]
    idx = idx + 1
    if (scrutinized_asset['asset-id'] == asset_id):
        holding = True
        break
if not holding:
# Usamos la clase AssetTransferTxn para transferir y realizar opt-in
    txn = AssetTransferTxn(
        sender=accounts[2],
        sp=params,
        receiver=accounts[2],
        amt=0,
        index=asset_id)
    stxn = txn.sign(SKs[2])
    # Se envia la transacción a la red
    try:
        txid = algod_client.send_transaction(stxn)
        print("Signed transaction with txID: {}".format(txid))
        confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
        print("TXID: ", txid)
        print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))

    except Exception as err:
        print(err)
    # Verificamos que el activo pertenece a esta cuenta
    # Este debe mostrar balance de 0
    print_asset_holding(algod_client, accounts[2], asset_id)
```

### 3.4  Transferir un activo

Los activos pueden transferirse entre cuentas que hayan optado por recibirlos (operación anterior). Son análogas a las transacciones de pago estándar, pero para los ASAs.

El siguiente código muestra un ejemplo que transfiere 10 activos de la cuenta 1 a la cuenta 3.

```python
txn = AssetTransferTxn(
    sender=accounts[0],
    sp=params,
    receiver=accounts[2],
    amt=10,
    index=asset_id)
stxn = txn.sign(SKs[0])
# Se envia la transacción a la red
try:
    txid = algod_client.send_transaction(stxn)
    print("Signed transaction with txID: {}".format(txid))
    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
except Exception as err:
    print(err)
# El saldo ahora debe ser 10.
print_asset_holding(algod_client, accounts[2], asset_id)
```

### 3.5 Congelar un activo

Congelar o descongelar un activo para una cuenta requiere de una transacción firmada por la cuenta que realizará esta operación. 

El código siguiente muestra como la cuenta 2 congela los activos de la cuenta 3.

```python
txn = AssetFreezeTxn(
    sender=accounts[1],
    sp=params,
    index=asset_id,
    target=accounts[2],
    new_freeze_state=True
)
stxn = txn.sign(SKs[1])

try:
    txid = algod_client.send_transaction(stxn)
    print("Signed transaction with txID: {}".format(txid))
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)  
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))    
except Exception as err:
    print(err)
# El saldo ahora debe ser 10 con el parametro 'frozen' en verdadero
print_asset_holding(algod_client, accounts[2], asset_id)
```

### 3.6 Revocar un activo

La revocación de un activo elimina un número específico de activos de una cuenta desde la cuenta de recuperación de dicho activo.

Para realizar esta operación es necesario especificar un emisor de activos (la cuenta de destino a revocar) y un receptor de activos (la cuenta a la que se transferiran los fondos de regreso). 

El siguiente código muestra la revocación de la cuenta 3 para regresar los activos a la cuenta 1, esto realizado por la cuenta 2.

```python
# La cuenta de recuperación (cuenta 2) revoca 10 MiMoneda de la cuenta 3 y la pone de regreso a la cuenta 1.
txn = AssetTransferTxn(
    sender=accounts[1],
    sp=params,
    receiver=accounts[0],
    amt=10,
    index=asset_id,
    revocation_target=accounts[2]
)
stxn = txn.sign(SKs[1])

try:
    txid = algod_client.send_transaction(stxn)
    print("Signed transaction with txID: {}".format(txid))
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))      
except Exception as err:
    print(err)
# El saldo de la cuenta 3 ahora es 0
print("Account 3")
print_asset_holding(algod_client, accounts[2], asset_id)
# El saldo de la cuenta 1 ahora es 1000 más
print("Account 1")
print_asset_holding(algod_client, accounts[0], asset_id)
```

### 3.7 Destruir un activo

Los activos  pueden ser destruidos por la cuenta administradora. Todos los activos deben ser propiedad del creador del activo antes de que el activo pueda ser eliminado.

El siguiente código muestra un ejemplo donde la cuenta 1 destruye un activo de la cuenta 3.

```python
# Transacción para destruir un activo
txn = AssetConfigTxn(
    sender=accounts[0],
    sp=params,
    index=asset_id,
    strict_empty_address_check=False
    )
stxn = txn.sign(SKs[0])
    try:
        txid = algod_client.send_transaction(stxn)
        print("Signed transaction with txID: {}".format(txid))
        confirmed_txn = wait_for_confirmation(algod_client, txid, 4) 
        print("TXID: ", txid)
        print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))     
    except Exception as err:
        print(err)
    # El activo ha sido destruido
    try:
        print("Account 3 must do a transaction for an amount of 0, ")
        print("with a close_assets_to to the creator account, to clear it from its accountholdings")
        print("For Account 1, nothing should print after this as the asset is destroyed on the creator account")
        print_asset_holding(algod_client, accounts[0], asset_id)
        print_created_asset(algod_client, accounts[0], asset_id)
    except Exception as e:
        print(e)
```


> **Saldo mínimo**
>
> Cualquier cuenta Algorand debe mantener un saldo mínimo de 0,1 Algo para evitar que personas malintencionadas creen demasiadas cuentas, lo que podría hacer que el tamaño de la tabla de cuentas (almacenada por todos los nodos de la blockchain) explote.
> Por cada activo que una cuenta opte o cree, el saldo mínimo se incrementa en 0,1 Algo.

 Si quieres conocer mas puedes consultar [la documentación para desarrolladores](https://developer.algorand.org/docs/features/asa/).
