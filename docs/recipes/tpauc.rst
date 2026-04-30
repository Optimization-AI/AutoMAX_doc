Two-way pAUC — pAUCLoss (2w) + SOTAs
======================================

Optimizes two-way partial AUC — restricting both the FPR and TPR ranges.
Suitable for medical screening where both false positives and false negatives
must be tightly controlled.

Config
------

.. code-block:: yaml
   :caption: recipes/automax/config_tpauc.yaml

   dataset:
     name: cifar10
     eval_splits: [val, test]
     kwargs:
       imratio: 0.02

   model:
     name: resnet18
     pretrained: false
     num_classes: 1
     in_channels: 3

   metrics:
     - AUROC
   metric_kwargs:
     - max_fpr: 0.3
       min_tpr: 0.7

   training:
     project_name: libauc
     experiment_name: resnet18_tpauc_cifar10
     SEED: 2026
     epochs: 60
     batch_size: 128
     eval_batch_size: 256
     sampling_rate: 0.5
     num_workers: 0
     decay_epochs: [0.5, 0.75]
     loss: pAUCLoss
     loss_kwargs:
       mode: 2w
     optimizer: SOTAs
     output_path: ./output
     resume_from_checkpoint: false
     save_checkpoint_every: 5

   automax:
     deterministic: true
     n_trials: 5
     SEED: 42
     name: resnet18_tpauc_cifar10
     output_directory: ./automax_output
     overwrite: true

Run
---

.. code-block:: bash

   python -m src.ui.auto_trainer \
     --config_file recipes/automax/config_tpauc.yaml

.. note::

   ``max_fpr: 0.3`` and ``min_tpr: 0.7`` define the rectangular region
   of the ROC curve being optimized — FPR ∈ [0, 0.3] and TPR ∈ [0.7, 1.0].
