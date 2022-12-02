# Configuración Inicial

Aquí aprenderemos como configurar los elementos principales para construir transacciones y contratos inteligentes en Algorand.

## Conceptos Básicos

Hay que tener en cuenta algunos conceptos clave a lo largo de esta tarea.

El primero es que la cadena de bloques o blockchain con la que vas a interactuar puede considerarse como una instanciación de un protocolo, en este caso el protocolo Algorand. Este protocolo define una red de nodos (nodos Algorand), que a un nivel muy básico son computadoras de todo el mundo que ejecutan el software Algorand, que implementa el protocolo Algorand. 

Existen múltiples instancias de esta red. Las dos instancias más grandes se llaman *MainNet* y *TestNet*. Ambas son redes públicas, esto quiere decir que  cualquiera puede acceder a ellas e interactuar con ellas. Sin embargo la MainNet utiliza un suministro fijo de la moneda nativa llamada Algo, que tiene un valor monetario real. Por otro lado la *TestNet*, que es también pública, se usa para pruebas y, por tanto, tiene una moneda Algo "falsa" que puede generarse de la nada (en lugar de comprarla con dinero real). En este tutorial trabajaremos con la TestNet y no con la MainNet.

También es posible crear tus propias instancias privadas de la red Algorand al grado de que esta red puede consistir en un solo nodo, como por ejemplo tu laptop.

## Paso 0

### Antecedentes

Algorand soporta oficialmente 4 Kits de Desarrollo de Software (SDK) para el desarrollo de aplicaciones: Python, Javascript, Java y Go. Además, Algorand tiene SDKs comunitarios para Rust y C#. Puedes pensar en los SDKs como bibliotecas específicas del lenguaje que te permiten interactuar con la cadena de bloques de Algorand. En este curso utilizaremos el SDK de Python. 

Para acceder a una cadena de bloques, también se necesita acceso a algún nodo de la red de la cadena de bloques. Para ello, utilizaremos el [servicio gratuito PureStake API](https://www.purestake.com/technology/algorand-api/).

### Paso 0.1 - Instala Python 3.8 y Pip

> **Nota**
>
> Python 2 no funcionará.

Instalar Python 3.8.0 (o posterior) con Pip.

* En Windows 7/8/10: (Windows XP no es soportado)

  1. Baja el instalador de Python en https://www.python.org/downloads/windows/
  2. En la primera pantalla del instalador asegurate de seleccionar "Install launcher for all users" y "Add Python 3.8 to PATH".
     ![Screenshot of Windows Installer with PATH](/Users/raldeco/Documents/Algorand/Primera Transacción /Practical-HW1/img/PythonWindowsPATH.png)

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

### Paso 0.2 - Instala el SDK de Python

Abre una terminal y ejecuta:

```bash
python3 -m pip install py-algorand-sdk --upgrade
```

> **Problemas comunes**
>
> * Si estas usando Windows y obtienes errores, remplaza `python3` por `python` en todos los comandos.
>
> * Si sigues obteniendo errores, comprueba que has añadido `python` al PATH al instalarlo (véase Paso 0.1). Si no es así, desinstala y vuelve a instalar Python.

### Paso 0.3 - Obten una llave PureStake API

Visita https://developer.purestake.io/ y registrare gratuitamente. Posterior mente obten una PureStake API Key para acceder al servicio PureStake API.

> **Nota**
>
> No hagas publica tu API PureStake Key. Cada vez que hagas pñublico tu código, elimina esta llave.

### Paso 0.4 - Instala un IDE

También necesitarás un editor de código, como [Visual Studio Code](https://code.visualstudio.com) o [PyCharm](https://www.jetbrains.com/pycharm/). Si ya tienes un editor, puedes omitir este paso. De lo contrario, descarga e instale uno de los editores mencionados.

(Opcional) Recomendamos usar PyCharm con la extensión [AlgoDEA](https://algodea-docs.bloxbean.com/) que puede instalarse en el menú de "Plugins" como se muestra a continuación:

![Captura de pantalla 2022-12-02 a la(s) 14.40.53](/Users/raldeco/Desktop/Captura de pantalla 2022-12-02 a la(s) 14.40.53.png)

Después de instalar la extensión AlgoDEA en PyCharm:

1. Abre PyCharm
2. Crea un nuevo proyecto Algorand (en lugar del proyecto "Pure Python" que es el predeterminado)
3. Configura el nodo haciendo clic en el "Explorador de Algorand" en la parte superior derecha y luego llena la información como se muestra a continuación:
   ![Screenshot of AlgoDEA PureStake node configuration](/Users/raldeco/Documents/Algorand/Primera Transacción /Practical-HW1/img/step0AlgoDEAPureStakeNodeConfiguration.png)

4. Haz clic en el botón "Fetch Network Info". Los datos "Genesis Hash" y "Genesis ID" deberían rellenarse automáticamente.

   > **Problemas comunes**
   >
   > * Si no ves la pestaña "Algorand Explorer", comprueba que has creado un nuevo proyecto Algorand y no un proyecto Pure Python.

   