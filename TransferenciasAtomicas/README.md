## Administrar activos con transferencias atómicas

En las finanzas tradicionales, el comercio de activos suele requerir un tercero de confianza, como un banco, para asegurarse de que ambas partes reciben lo acordado. En la cadena de bloques Algorand, este tipo de comercio se implementa dentro del protocolo como una **transferencia atómica**. Esto significa que un conjunto de transacciones se ven como una sola de tal manera que todas tienen éxito o todas fracasan. Las transferencias atómicas permiten a completos desconocidos intercambiar activos sin necesidad de un intermediario de confianza, garantizando al mismo tiempo que cada parte recibirá lo que acordó.

Las transferencias atómicas se pueden usar en casos como los siguientes.

- **Operaciones circulares:** Alice paga a Bob si y sólo si Bob paga a Claire si y sólo si Claire paga a Alice.
- **Pagos en grupo:**  Todos pagan o nadie paga.
- **Intercambios descentralizados:** Intercambiar un activo por otro sin pasar por un intercambio centralizado.
- **Pagos distribuidos:** Pagos a múltiples destinatarios.
- **Comisiones de transacción agrupadas**: Una transacción paga las comisiones de otras.

En temas anteriores, hemos visto cómo transferir Algos (Tema 2), como crear activos y como transferir activos (Tema 3). En este tema revisaremos como realizar **transferencias atómicas**.

Las transferencias atómicas permiten agrupar dos transacciones de tal forma que ambas transacciones tengan éxito o ambas transacciones fracasen.

Para crear este tipo de transacciones hay que seguir los siguientes pasos:

1. **Crear las transacciones y/o transferencias de activos.** Crear una transacción como se explicó en el Tema 2 sin firmar. Si como consecuencia de esta transacción se transferirá un activo también se de crear esta transferencia como se explicó en el Tema 3 sin firmar.
2. **Agrupar las transacciones.** Estas dos (o más) transacciones se agrupan creando un identificador para este grupo de transacciones.
3. **Firmar las transacciones agrupadas.** Se firman las transacciones agrupadas con sus respectivas llaves privadas.
4. **Enviar las transacciones unidas a la red.** Combinar las transacciones y enviarlas a la red.
5. **Comprobar en el explorador** que el grupo de transacciones se confirmo correctamente.

Ahora veamos un ejemplo.

#### Crear transacciones

Crear dos o más (hasta 16) transacciones sin firmar de cualquier tipo. Esto se hace siguiendo los pasos del Tema 2 o del Tema 3.

Estas transacciones pueden ser creadas por un servicio o por cada una de las partes implicadas en la transacción. Por ejemplo, una aplicación de intercambio de activos puede crear la transferencia atómica y permitir que las partes individuales firmen desde su ubicación.

El ejemplo siguiente ilustra la Cuenta A enviando una transacción a la Cuenta C y la Cuenta B enviando una transacción a la Cuenta A.

```python
# de la cuenta 1 a la cuenta 3
txn_1 = transaction.PaymentTxn(account_1, params, account_3, 100000)

# de la cuenta 2 a la cuenta 1
txn_2 = transaction.PaymentTxn(account_2, params, account_1, 200000)
```

#### Agrupar transacciones

Combinar transacciones sólo significa concatenar estas transacciones en un único archivo o en un arreglo para poder asignarles un ID de grupo. 

El resultado de este paso es lo que, en última instancia, garantiza que una transacción concreta pertenece a un grupo y no es válida si se envía sola (aunque esté debidamente firmada). 

Un identificador de grupo se calcula aplicando un hash a la concatenación del conjunto de transacciones relacionadas. El hash resultante se asigna al campo *group* dentro de cada transacción. Este mecanismo permite a cualquiera recrear todas las transacciones y recalcular el ID de grupo para verificar que el contenido es el acordado por todas las partes. Además, debe mantenerse el orden del conjunto de transacciones para que este hash siga siendo el mismo.

```python
# obtener un identificador de grupo y asignarlo a las transacciones
gid = transaction.calculate_group_id([txn_1, txn_2])
txn_1.group = gid
txn_2.group = gid
```

#### Firmar transacciones

Con un ID de grupo asignado, cada remitente de transacción debe autorizar su transacción respectiva con su correspondiente llave privada.

```python
# firmar las transacciones
stxn_1 = txn_1.sign(sk_1)    
stxn_2 = txn_2.sign(sk_2)
```

#### Crear un grupo de transacciones

Todas las transacciones ya firmadas se unen en una nueva estructura que mantiene el orden original que se le asignó a las transacciones no firmadas.

```python
# crear el grupo de transacciones firmadas
signed_group =  [stxn_1, stxn_2]
```

#### Enviar el grupo de transacciones

Este grupo de transacciones ya sólo se envía a la red.

```python
tx_id = algod_client.send_transactions(signed_group)

# esperar confirmación

confirmed_txn = wait_for_confirmation(algod_client, tx_id, 4)
print("txID: {}".format(tx_id), " confirmed in round: {}".format(
confirmed_txn.get("confirmed-round", 0)))   
```

#### Visualizar un grupo de transacciones

En [AlgoExplorer](https://testnet.algoexplorer.io) puedes ver que las transacciones se agrupan de dos maneras:

1. Cada transacción del grupo tiene un ID de grupo, que enlaza con una página con todas las transacciones del grupo. 
   ![](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/step4AlgoExplorerTxn.png)
2. Si varias transacciones de un grupo afectan a la misma cuenta, en la página de la cuenta aparecerá un pequeño icono junto a las transacciones. Véase la captura de pantalla siguiente:
   ![](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/step4AlgoExplorerAccount.png)

Si no ves lo anterior, significa que enviaste dos transacciones independientes en lugar de hacer una transferencia atómica.