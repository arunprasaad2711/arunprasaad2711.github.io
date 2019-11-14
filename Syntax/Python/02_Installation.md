<!-- TOC -->

- [Installation](#Installation)
  - [Using a Basic Installer](#Using-a-Basic-Installer)
    - [Using pip installer](#Using-pip-installer)
    - [Installing from scratch](#Installing-from-scratch)
    - [Using Linux/Unix installers](#Using-LinuxUnix-installers)
    - [Using Python Distribution Bundles](#Using-Python-Distribution-Bundles)

<!-- /TOC -->
# Installation

Python is cross platform. And hence, it can be installed in all operating systems namely Linux, Windows, Unix, and MacOS. Python is an interpreted programming language. So, it is required to download an interpreter for the installation. There are many ways to download python.

## Using a Basic Installer

One of the simplest way to install python is by downloading a basic installer from the [Python Software Foundation](python.org). This option is available for Windows, Linux, Mac OS and even other platforms. The installer files are present in the [Downloads page](https://www.python.org/downloads/) of the website. 

This installer comes with an ``Interactive Development Environment`` also known as ``IDE`` called IDLE for writing and testing code. With IDLE and some bare minimum libraries, the set-up gives the user a bare-minimum starting point to use Python. To make python versatile and to be able to use it for many many other functionalities, It needs more libraries. 

To install libraries, the python installer comes with a basic package manager called ``pip``. ``pip`` is a recursive acronym for "Pip installs Python". This is the basic requirement to install python libraries and packages.

<hr>
This part below needs rework! Work in progress!
<!-- use this link for details: https://realpython.com/installing-python/-->
<hr>

Python Installer Program Those are installed by using ``pip`` and ``setuptools``. Also, ``easy_install`` is useful. Multiple installer environments are possible using ``virtualenv`` package.

Works in Windows.

### Using pip installer
It installs python libraries and packages. Along with ``setuptools`` and ``easy_install`` and ``virtualenv``, it works wonders. Sometimes the dependencies may not be met. Does not work when non-python software/libraries are needed.

Works in all Operating Systems.

### Installing from scratch
This involves compiling Python from the source code. Tedious work and not at all recommended due to the complexity of the process. Some libraries can be installed in this process.

This works in all operating systems.

### Using Linux/Unix installers
Linux and Unix have Python installed in them by default. Hence, the system installers like *apt* (Debian family), *yum* (Fedora Family), *brew* (MacOS) etc., are useful for installing the packages easily. One highly recommended way. However, since Python is used to make GUI and Software that run in Linux/Unix machines, installing conflicting libraries or upgrading libraries might break the system software / programs. So, it is recommended to proceed with a bit caution here, as the installation is easy, one might be bound to make mistakes here.

### Using Python Distribution Bundles
This is by far the simplest and cleanest way to install Python. Python is provided as a distribution bundle from companies **Continuum Analytics** and **Enthought**. Anaconda Python installer and Miniconda Python installer from **Continuum Analytics** are one of the best collections. The former one has a massive collection including a basic Python installation, core Python libraries, a vast collection of Python Libraries with required software, and the famous package manager, installer, and software installer ``conda``. The later one is a minimal version having ``conda``, basic Python installation, and core Python libraries for user-customized building.

This distribution bundle installs Python separately and helps in maintaining multiple versions of python seamlessly. Upgrading Python and its libraries are easiest. Besides, the installation is so simple, that in Linux and Unix, it installs a separate stand alone Python environment thereby not interfering with the system python. And so, it can be modified, tweaked, or removed easily without affecting the system.

**Enthought** also has a Python Distribution bundle called **Canopy**. In all aspects, it is similar to Anaconda and Miniconda. However, as of now, Canopy bundle is not available for Python 3. Canopy will be launched in Python 3 soon and thus it provides an alternative means to install and use Python.
