AUROC — AUCMLoss + PESG
========================

The canonical setup for binary imbalanced classification. ``AUCMLoss``
with ``PESG`` directly maximizes AUROC using a minimax formulation.

Config
------

.. code-block:: yaml
   :caption: recipes/automax/config_auc.yaml

   dataset:
     name: cifar10
     eval_splits: [val, test]
     kwargs:
       imratio: 0.1

   model:
     name: resnet18
     pretrained: false
     num_classes: 1
     in_channels: 3

   metrics:
     - AUROC

   training:
     project_name: libauc
     experiment_name: resnet18_AUCMLoss_cifar10
     SEED: 2026
     epochs: 100
     batch_size: 128
     eval_batch_size: 256
     sampling_rate: 0.2
     num_workers: 0
     decay_epochs: [0.5, 0.75]
     loss: AUCMLoss
     optimizer: PESG
     output_path: ./output
     resume_from_checkpoint: false
     save_checkpoint_every: 5

   automax:
     deterministic: true
     n_trials: 5
     SEED: 42
     name: resnet18_AUCMLoss_cifar10
     output_directory: ./automax_output
     overwrite: true

Run
---

.. code-block:: bash

   python -m src.ui.auto_trainer \
     --config_file recipes/automax/config_auc.yaml

Available dataset variants
--------------------------

.. code-block:: bash

   # PneumoniaMNIST
   python -m src.ui.auto_trainer \
     --config_file recipes/automax/config_auc_PneumoniaMNIST.yaml

   # BreastMNIST
   python -m src.ui.auto_trainer \
     --config_file recipes/automax/config_auc_BreastMNIST.yaml

   # CheXpert (chest X-ray, multi-label)
   python -m src.ui.auto_trainer \
     --config_file recipes/automax/config_auc_CheXpert.yaml

   # RIP-Dataset (Transformer backbone)
   python -m src.ui.auto_transformers_trainer \
     --config_file recipes/automax/config_auc_RIP.yaml

Hyperparameter search space
---------------------------

AutoMAX tunes the following parameters for ``AUCMLoss`` + ``PESG``:

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Parameter
     - Source
     - Type
     - Notes
   * - ``lr``
     - optimizer
     - log-uniform range
     - Learning rate
   * - ``epoch_decay``
     - optimizer
     - range
     - LR decay factor applied at ``decay_epochs``
   * - ``weight_decay``
     - optimizer
     - log-uniform range
     - L2 regularization
   * - ``momentum``
     - optimizer
     - categorical
     - Momentum coefficient
   * - ``margin``
     - loss
     - categorical
     - Surrogate loss margin
