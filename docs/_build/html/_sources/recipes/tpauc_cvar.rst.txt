Two-way pAUC CVaR — tpAUC_CVaR_loss + STACO
============================================

Optimizes two-way partial AUC using a CVaR (Conditional Value-at-Risk)
surrogate loss, paired with the STACO optimizer. The CVaR formulation
provides a more robust upper bound on the pAUC loss, particularly useful
when the score distribution has heavy tails.

Config
------

.. code-block:: yaml
   :caption: recipes/config_tpauc_cvar.yaml

   dataset:
     name: cifar10
     eval_splits: [val, test]
     kwargs:
       imratio: 0.2

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
     experiment_name: resnet18_tpAUC_CVaR_loss_cifar10
     SEED: 2026

     epochs: 60
     batch_size: 128
     eval_batch_size: 256
     sampling_rate: 0.5
     num_workers: 0
     decay_epochs: [0.5, 0.75]

     loss: tpAUC_CVaR_loss
     loss_kwargs:
       surr_loss: squared_hinge
     optimizer: STACO

     output_path: ./output
     resume_from_checkpoint: false
     save_checkpoint_every: 10

   automax:
     deterministic: true
     n_trials: 5
     SEED: 42
     name: resnet18_tpAUC_CVaR_loss_cifar10
     output_directory: ./automax_output
     overwrite: true

Run
---

.. code-block:: bash

   python -m src.auto_trainer \
     --config_file recipes/config_tpauc_cvar.yaml

.. note::

   ``max_fpr: 0.3`` and ``min_tpr: 0.7`` define the rectangular region of
   the ROC curve being optimized — FPR ∈ [0, 0.3] and TPR ∈ [0.7, 1.0].
   The ``squared_hinge`` surrogate loss is the default for CVaR-based pAUC
   optimization; it can be swapped for other surrogate losses supported by
   LibAUC.
