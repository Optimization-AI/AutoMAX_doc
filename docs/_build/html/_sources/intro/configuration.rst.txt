Configuration Reference
=======================

AutoMAX is driven by a single YAML file passed via ``--config_file``.
It has five top-level sections:

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Section
     - Required
     - Purpose
   * - ``dataset``
     - ✅ yes
     - Dataset name, splits, and loading kwargs
   * - ``model``
     - ✅ yes
     - Architecture and checkpoint settings
   * - ``metrics``
     - no
     - Evaluation metrics — defaults to ``[AUROC]``
   * - ``training``
     - ✅ yes
     - Loss, optimizer, schedule, and checkpointing
   * - ``automax``
     - ✅ yes
     - Hyperparameter search configuration

----

``dataset``
-----------

.. code-block:: yaml

   dataset:
     name: cifar10
     eval_splits: [val, test]
     kwargs:
       imratio: 0.1

.. list-table::
   :header-rows: 1
   :widths: 20 15 12 53

   * - Field
     - Type
     - Required
     - Description
   * - ``name``
     - string
     - ✅ yes
     - Dataset identifier passed to ``load_dataset()``
   * - ``eval_splits``
     - list[string]
     - no
     - Splits evaluated each epoch. Default: ``[val]``
   * - ``kwargs``
     - mapping
     - no
     - Extra arguments forwarded to ``load_dataset()``

``kwargs`` sub-fields:

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Field
     - Type
     - Description
   * - ``imratio``
     - float
     - Positive-class imbalance ratio (e.g. ``0.1`` = 10% positive samples)

----

``model``
---------

.. code-block:: yaml

   model:
     name: resnet18
     pretrained: false
     pretrained_path: /path/to/checkpoint.pth
     num_classes: 1
     in_channels: 3

.. list-table::
   :header-rows: 1
   :widths: 22 15 12 15 36

   * - Field
     - Type
     - Required
     - Default
     - Description
   * - ``name``
     - string
     - ✅ yes
     - —
     - Architecture identifier passed to ``build_model()``
   * - ``pretrained``
     - bool
     - no
     - ``false``
     - Whether to load pretrained weights
   * - ``pretrained_path``
     - string
     - no
     - —
     - Path to a ``.pth`` checkpoint. Required if ``pretrained: true``
   * - ``num_classes``
     - int
     - ✅ yes
     - —
     - Number of output classes. Use ``1`` for binary classification
   * - ``in_channels``
     - int
     - no
     - ``3``
     - Number of input channels

----

``metrics``
-----------

A list of metric names computed on every evaluation split after each epoch.
The **first entry** is used as the AutoMAX optimization target.

.. code-block:: yaml

   metrics:
     - AUROC

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Value
     - Description
   * - ``AUROC``
     - Area Under the ROC Curve
   * - ``AUPRC``
     - Area Under the Precision-Recall Curve
   * - ``ACC``
     - Accuracy at threshold 0.5

If omitted, defaults to ``[AUROC]``.

For partial AUC variants, supply ``metric_kwargs`` alongside ``metrics``:

.. code-block:: yaml

   metrics:
     - AUROC
   metric_kwargs:
     - max_fpr: 0.3       # one-way pAUC: FPR in [0, 0.3]
     - min_tpr: 0.7       # two-way pAUC: TPR in [0.7, 1.0]

----

``training``
------------

.. code-block:: yaml

   training:
     project_name: libauc
     experiment_name: AUCMLoss_cifar10

     epochs: 100
     batch_size: 128
     eval_batch_size: 256
     sampling_rate: 0.2
     num_workers: 0
     SEED: 123

     loss: AUCMLoss
     optimizer: PESG

     decay_epochs: [0.5, 0.75]

     output_path: ./output
     resume_from_checkpoint: false
     save_checkpoint_every: 10

Experiment tracking
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 12 15 48

   * - Field
     - Required
     - Default
     - Description
   * - ``project_name``
     - no
     - ``libauc``
     - Top-level project name for run tracking
   * - ``experiment_name``
     - ✅ yes
     - —
     - Unique name for this run

Core training parameters
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 12 15 45

   * - Field
     - Type
     - Default
     - Description
   * - ``epochs``
     - int
     - ``50``
     - Total training epochs
   * - ``batch_size``
     - int
     - ``128``
     - Training mini-batch size
   * - ``eval_batch_size``
     - int
     - ``128``
     - Batch size used during evaluation
   * - ``sampling_rate``
     - float
     - ``0.5``
     - Positive-sample ratio for ``DualSampler``
   * - ``num_workers``
     - int
     - ``2``
     - DataLoader worker processes. Use ``0`` on Windows
   * - ``SEED``
     - int
     - ``42``
     - Global random seed for reproducibility

Loss and optimizer
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 12 63

   * - Field
     - Required
     - Description
   * - ``loss``
     - ✅ yes
     - Loss function name. See :doc:`loss_optimizer_pairs`
   * - ``optimizer``
     - ✅ yes
     - Optimizer name. Must be compatible with the chosen loss
   * - ``loss_kwargs``
     - no
     - Override individual loss hyperparameters (merged over defaults)
   * - ``optimizer_kwargs``
     - no
     - Override individual optimizer hyperparameters (merged over defaults)

``loss_kwargs`` and ``optimizer_kwargs`` accept the same hyperparameter
definition format as the search spaces. See :doc:`hyperparameter_format`.

.. code-block:: yaml

   training:
     optimizer_kwargs:
       lr: 0.05                   # scalar → fixed constant
     loss_kwargs:
       margin:
         val: [0.8, 1.0]          # narrow the categorical choices
         default: 1.0

Learning rate schedule
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 15 15 45

   * - Field
     - Type
     - Default
     - Description
   * - ``decay_epochs``
     - list[float]
     - ``[]``
     - Epoch fractions at which LR is decayed. E.g. ``[0.5, 0.75]``
       decays at 50% and 75% of training.

Checkpointing
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 12 15 43

   * - Field
     - Type
     - Default
     - Description
   * - ``output_path``
     - string
     - ``./output``
     - Directory for checkpoints and results
   * - ``resume_from_checkpoint``
     - bool
     - ``true``
     - Resume from latest checkpoint in ``output_path``
   * - ``save_checkpoint_every``
     - int
     - ``5``
     - Save a ``.pt`` checkpoint every N epochs

----

``automax``
-----------

.. code-block:: yaml

   automax:
     name: n5_AUCMLoss_cifar10
     n_trials: 5
     SEED: 42
     deterministic: true
     output_directory: ./automax_output
     overwrite: true

.. list-table::
   :header-rows: 1
   :widths: 25 12 12 15 36

   * - Field
     - Type
     - Required
     - Default
     - Description
   * - ``name``
     - string
     - ✅ yes
     - —
     - Unique identifier for this search run
   * - ``n_trials``
     - int
     - no
     - ``5``
     - Number of hyperparameter configurations to evaluate
   * - ``SEED``
     - int
     - no
     - ``42``
     - Random seed for the hyperparameter sampler
   * - ``deterministic``
     - bool
     - no
     - ``true``
     - Enforce fully deterministic training across trials
   * - ``output_directory``
     - string
     - no
     - ``./automax_output``
     - Directory for search results and trial logs
   * - ``overwrite``
     - bool
     - no
     - ``true``
     - Overwrite an existing search run with the same ``name``

.. note::

   The field is ``output_directory`` in code (``AutoMAXConfigration``), but
   some example YAMLs use ``output_path``. Always use ``output_directory`` to
   ensure the value is correctly read.
