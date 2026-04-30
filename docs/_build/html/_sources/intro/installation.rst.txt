Installation
============

Requirements
------------

- Python 3.10
- A C++ compiler and SWIG (required by SMAC3's underlying components)
- CUDA-capable GPU recommended for training

From Source
-----------

.. code-block:: bash

   git clone https://github.com/Optimization-AI/AutoMAX.git
   cd AutoMAX
   conda create -n AutoMAX python=3.10
   conda activate AutoMAX
   conda install gxx_linux-64 gcc_linux-64 swig
   pip install -r requirements.txt

Core Dependencies
-----------------

.. code-block:: text

   libauc
   smac
   omegaconf
   torch
   torchvision
   medmnist

.. warning::

   **Windows users:** Set ``num_workers: 0`` in your config to avoid
   DataLoader multiprocessing issues on Windows.

Verifying the Install
---------------------

.. code-block:: bash

   python -c "import libauc; print(libauc.__version__)"
   python -m src.ui.run_trainer --config_file recipes/libauc_trainer/config_auc.yaml
