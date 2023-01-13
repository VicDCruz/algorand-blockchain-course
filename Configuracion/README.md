# Configuración Inicial

Aquí aprenderemos como configurar los elementos principales para construir transacciones y contratos inteligentes en Algorand.

## Conceptos Básicos

Hay que tener en cuenta algunos conceptos clave a lo largo de este tema.

El primero es que la cadena de bloques o blockchain con la que vas a interactuar puede considerarse como una instanciación de un protocolo, en este caso el protocolo Algorand. Este protocolo define una red de nodos (nodos Algorand), que a un nivel muy básico son computadoras de todo el mundo que ejecutan el software Algorand y que implementa el protocolo Algorand. 

Existen múltiples instancias de esta red. Las dos instancias más grandes se llaman *MainNet* y *TestNet*. Ambas son redes públicas, esto quiere decir que cualquiera puede acceder a ellas e interactuar con ellas. Sin embargo, la MainNet utiliza un suministro fijo de la moneda nativa llamada Algo, y en ella tiene un valor monetario real. Por otro lado la *TestNet*, que es también pública, se usa para pruebas y por tanto tiene una moneda Algo "falsa" que puede generarse de la nada (en lugar de comprarla con dinero real). En este tutorial trabajaremos con la TestNet y no con la MainNet.

También es posible crear tus propias instancias privadas de la red Algorand generando una red queconsiste de un solo nodo, como por ejemplo tu laptop. Esto lo revisaremos en otro tutorial.

### Antecedentes

Algorand soporta oficialmente 4 Kits de Desarrollo de Software (SDK) para el desarrollo de aplicaciones: Python, Javascript, Java y Go. Además, Algorand tiene SDKs comunitarios para Rust y C#. Los SDKs son como bibliotecas específicas del lenguaje que te permiten interactuar con la cadena de bloques de Algorand. En este curso utilizaremos el SDK de Python. 

Para acceder a una cadena de bloques, también se necesita acceso a algún nodo de la red de esta cadena de bloques. Para ello, te mostraremos como usar dos tipos de servicios gratuitos [PureStake API](https://www.purestake.com/technology/algorand-api/) y [Algo Node](https://algonode.io/api/). Ambos ofrecen acceso a un nodo de la red a través de su API. 

También puedes hacerlo a través del [Sandbox de Algorand](https://developer.algorand.org/tutorials/exploring-the-algorand-sandbox/) que te permite tener un nodo de manera local en tu computadora. En este tutorial no usaremos este método, pero puedes revisar la documentación del mismo si deseas usarlo.

### Paso 1 - Instala Python 3.8 y Pip

> **Nota**
>
> Python 2, Python 3.7 y previos no funcionarán, no los uses.

Instalar Python 3.8.0 (o posterior) con Pip.

* En Windows 7/8/10: (Windows XP no es soportado)

  1. Baja el instalador de Python en https://www.python.org/downloads/windows/
  2. En la primera pantalla del instalador asegurate de seleccionar "Install launcher for all users" y "Add Python 3.8 to PATH".

![Instalar en Windows](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/PythonWindowsPATH.png)

* En macOS:

  * Si no tienes instalado [HomeBrew](https://brew.sh) abre una terminal y ejecuta:

  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  ```

  * Si tienes instalado [HomeBrew](https://brew.sh) abre una terminal y ejecuta:

  ```bash
  brew install python3
  ```

* En Ubuntu 18.04 o posterior, abre una terminal y ejecuta:

  ```
  sudo apt update
  sudo apt install python3-pip
  ```

### Paso 2 - Instala el SDK de Python

Abre una terminal y ejecuta:

```bash
python3 -m pip install py-algorand-sdk --upgrade
```

Verifica que estas instalando la última version del python algorand sdk. Esto lo puedes revisar en [py-algorand-sdk](https://py-algorand-sdk.readthedocs.io/en/latest/index.html)

> **Problemas comunes**
>
> * Si estas usando Windows y obtienes errores, remplaza `python3` por `python` en todos los comandos.
> * Revisa que estas usando la versión de Python donde instalaste py-algorand-sdk. Esto lo puedes hacer usando el comando 
> >```bash
> >pip list
> >```
> * Si sigues obteniendo errores, comprueba que has añadido `python` al PATH al instalarlo (véase Paso 1). Si no es así, desinstala y vuelve a instalar Python.

### Paso 3 - Conectarse al nodo usando su API

Existen varias maneras de interactuar con una blockchain, en este caso te explicaremos como usar los servivios gratuitos de dos "API-As-A-Service" que proporcionan acceso a las API REST nativas de Algorand para su MainNet y su TestNet.

1. El servicio de [PureStake](https://algobuilder.dev/guide/purestake-api.html). Para poder usarla es necesario registrarse y obtener una API KEY (necesaria para realizar solicitudes). Visita https://developer.purestake.io/ y registrare gratuitamente. Posteriormente obten una PureStake API Key y guardala de manera segura.
2. El servicio de [Algo Node](https://algonode.io/). Para poder usarla NO es necesario registro ni API KEY, sin embargo tiene restricción en el número de solicitudes realizadas a través de su servicio gratuito.

Mas adelante te mostraremos como usar ambas.

> **Nota**
>
> No hagas publica tu API PureStake Key. Cada vez que hagas público tu código, elimina esta llave.

### Paso 4 - Instala un IDE

También necesitarás un editor de código, como [Visual Studio Code](https://code.visualstudio.com) o [PyCharm](https://www.jetbrains.com/pycharm/). Si ya tienes alguno de estos editores, puedes omitir este paso. De lo contrario, descarga e instale uno de los editores mencionados.

### PyCharm
Si desear trabajar con el IDE PyCharm hay que instalar la extensión [AlgoDEA](https://algodea-docs.bloxbean.com/) esto puede hacerse en el menú de "Plugins" como se muestra a continuación:

![Plugin PyCharm](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/PycharmPlugin.png)

Después de instalar la extensión AlgoDEA en PyCharm:

1. Abre PyCharm
2. Crea un nuevo proyecto Algorand (en lugar del proyecto "Pure Python" que es el predeterminado)
3. Configura el nodo haciendo clic en el "Explorador de Algorand" en la parte superior derecha, agrega un nuevo nodo y, dependiendo del servicio usado en el paso 3 deberas incluir las ligas del EndPoint y el Indexer. 
A continuación se muestra el ejemplo con PureStake.

![PureStake](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/PureStakeNodeConfiguration.png)

A continuación se muestra el ejemplo con Algo Node.

![AlgoNode](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/AlgoNodeNodeConfiguration.png)

4. Haz clic en el botón "Fetch Network Info". Los datos "Genesis Hash" y "Genesis ID" deberían rellenarse automáticamente.

   > **Problemas comunes**
   >
   > * Si no ves la pestaña "Algorand Explorer", comprueba que has creado un nuevo proyecto Algorand y no un proyecto Pure Python.

### Visual Studio Code
Si desear trabajar con el IDE Visual Studio Code hay que instalar la extensión [Algorand VS Code Extension](https://marketplace.visualstudio.com/items?itemName=obsidians.vscode-algorand) esto puede hacerse en el menú de "Extensions" como se muestra a continuación:

![VSCode](https://github.com/raldecop/AlgorandEsp/blob/main/Imagenes/VSCodeAlgorand.png)

### Gitpod   

Otra opción es usar el IDE en línea que proporciona el servicio de [Gitpod](gitpod.io). Para acceder a él deberas tener cuenta de GitHub, GitLab o Bitbucket. En estas cuentas deberás crear un repositorio con el código a ejecutar. Si es la primera vez que usas este servicio verifica que este instalada la extensión de python, para posteriormente en su consola instalar el SDK de Python (Paso 2). 

