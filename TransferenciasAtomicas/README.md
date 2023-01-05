## Administrar activos con transferencias atómicas

En los pasos anteriores, hemos visto cómo transferir Algos, crear activos y transferir activos.
En muchas situaciones, sin embargo, necesitamos comerciar o intercambiar un activo por y Algos (o y otros activos).
Por ejemplo, la cuenta A puede vender su activo a la cuenta B en lugar de regalarlo.
Una solución es que la cuenta B envíe primero algunos Algos para pagar el activo, y luego la cuenta A envíe el activo. Pero entonces la cuenta B no puede estar segura de que la cuenta A no huirá con el dinero.

Las transferencias atómicas resuelven completamente este problema.
Las transferencias atómicas permiten agrupar dos transacciones (transferencia de activo de A a B, y transferencia de Algos de B a A) de tal forma que:

* Ambas transacciones tengan éxito: A obtiene sus Algos y B obtiene su activo.
* O ambas transacciones fracasen: A conserve su activo y B conserve sus Algos.

Veamos como crear transferencias atómicas.

Los pasos a seduir son los siguientes:

1. Crear una transacción de pago de cierta cantidad de Algos de B a A sin firmar.
2. Crear una transferencia del activo de A a B sin firmar.
3. Agrupar estas dos transacciones. Hay que tener en cuenta que esto modifica las transacciones para garantizar que una no se pueda confirmar sin la otra.
4. Firmar la primera transacción utilizando la llave privada de la cuenta B.
5. Firmar la segunda transacción utilizando la llave privada de la cuenta A.
6. Envíar ambas transacciones juntas. 
7. Comprobar en el explorador que el grupo de transacciones se confirmo correctamente.

En [AlgoExplorer](https://testnet.algoexplorer.io) puedes ver que las transacciones se agrupan de dos maneras:

1. Cada transacción del grupo tiene un ID de grupo, que enlaza con una página con todas las transacciones del grupo. 
   ![](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/step4AlgoExplorerTxn.png)
2. Si varias transacciones de un grupo afectan a la misma cuenta, en la página de la cuenta aparecerá un pequeño icono junto a las transacciones. Véase la captura de pantalla siguiente:
   ![](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/step4AlgoExplorerAccount.png)

Si no ves lo anterior, significa que enviaste dos transacciones independientes en lugar de hacer una transferencia atómica.