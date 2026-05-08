Quick Start
===========

Get up and running with AutoMAX in three steps.

Step 1 — Install
----------------

.. code-block:: bash

   conda create -n AutoMAX python=3.10
   conda activate AutoMAX
   conda install gxx_linux-64 gcc_linux-64 swig
   pip install -r requirements.txt

Step 2 — Write a config
------------------------

Create a ``config.yaml`` file:

.. code-block:: yaml

   dataset:
     name: cifar10
     eval_splits: [val, test]
     kwargs:
       imratio: 0.1

   model:
     name: resnet18
     num_classes: 1

   metrics:
     - AUROC

   training:
     experiment_name: my_first_run
     loss: AUCMLoss
     optimizer: PESG

   automax:
     name: my_first_run
     n_trials: 5

Step 3 — Run AutoMAX
---------------------

.. code-block:: bash

   python -m src.ui.auto_trainer --config_file config.yaml

You can override any ``training`` field directly on the command line:

.. code-block:: bash

   python -m src.ui.auto_trainer --config_file config.yaml --epochs 50 --seed 0

Entry Points
------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Command
     - Use case
   * - ``src.auto_trainer``
     - AutoTune on standard image datasets (MedMNIST, CIFAR, CheXpert, …)
   * - ``src.auto_transformers_trainer``
     - AutoTune with Transformer backbones (e.g. RIP-Dataset)