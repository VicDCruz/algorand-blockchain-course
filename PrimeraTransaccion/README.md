## Paso 2 - Tu primera transacción

Una transacción es la transferencia de Algos de una cuenta a otra.

Cualquier transacción puede incluir una "nota" arbitraria de hasta 1kb. En otras palabras, las notas permiten almacenar una pequeña cantidad de datos en la cadena de bloques que nos permitirá identificar una transacción de otra de manera local.

### Paso 2.1 Conecta con el cliente

El SDK de Python permite enviar transacciones a través de su cliente. El cliente debe ser instanciado antes de hacer llamadas a los puntos finales de la API y se deben proporcionar valores para `algod-address` y `algod-token`. 

Para utilizar el servicio API de PureStake,  `algod_client` debe incluir la llave PureStake API que obtuviste en el paso 0.3 como se muestra a continuación:

```python
algod_client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "YOUR PURESTAKE API KEY"}
)
```

### Paso 2.2 Revisa el saldo de tu cuenta

Antes de pasar al siguiente paso, verifiquemos el saldo de nuestra(s) cuenta(s) usando las siguientes líneas de código.

```python
account_info = algod_client.account_info(my_address)
print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
```

Hay que tener en cuenta que el importe del saldo se especifica en microAlgos: 1.000.000 microAlgo = 1 Algo.

### Paso 2.3 Crea una transacción

Las transacciones se utilizan para interactuar con la red Algorand. Para crear una transacción podemos usar siguiente código. Como se puede ver se debe indicar la dirección a donde se depositara la cantidad de Algos que indiquemos además de una nota.  

```python
from algosdk.future import transaction
from algosdk import constants

    params = algod_client.suggested_params()
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE 
    receiver = "DIRECCION DEL RECEPTOR"
    note = "Hello World".encode() #Nota a
    amount = 1000000
    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)

```

### Paso 2.4 Firmar una transacción 

Antes de enviar la transacción, esta tiene que ser firmada con la llave privada del creador de la misma. Para eso puedes usar el siguiente código.

```python
signed_txn = unsigned_txn.sign(private_key)
```

### Paso 2.5 Enviar una transacción

La transacción firmada puede ahora ser enviada a la red. `wait_for_confirmation` es un método que es llamado después de que la transacción es enviada para esperar hasta que la transacción sea transmitida a la blockchain de Algorand y esta sea confirmada. Esto puede verse en el siguiente código.

```python
`<code>`
import json
import base64

    #submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation 
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print(err)

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transfered: {} microAlgos".format(amount) )    
    print("Fee: {} microAlgos".format(params.fee) ) 


    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

```

Puedes confirmar que la transacción fue registrada en la cadena de bloques en el [explorador](https://testnet.algoexplorer.io) de Algorand, buscando la dirección de tu cuenta y haciendo clic en la transacción correspondiente. 

![Transaccion en AlgoExplorer](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/step2AlgoExplorer.png)

### Comisión por transacción

Para enviar una transacción en Algorand, hay que pagar una comisión. La tarifa mínima es de 0.001 Algo (es decir, 1.000 microAlgos). La tarifa requerida puede aumentar en caso de congestión. 
Consulte la [documentación para desarrolladores](https://developer.algorand.org/docs/features/transactions/#fees) para más detalles.

