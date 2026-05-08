AUPRC — APLoss + SOAP
======================

Optimizes Average Precision (proxy for AUPRC) using the stochastic AP
optimizer. Best when precision-recall tradeoff matters more than ROC.

Config
------

.. code-block:: yaml
   :caption: recipes/config_auprc.yaml

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
     - AUPRC

   training:
     project_name: libauc
     experiment_name: resnet18_APLoss_cifar10
     SEED: 2026
     epochs: 60
     batch_size: 128
     eval_batch_size: 256
     sampling_rate: 0.5
     num_workers: 0
     decay_epochs: [0.5, 0.75]
     loss: APLoss
     optimizer: SOAP
     output_path: ./output
     resume_from_checkpoint: false
     save_checkpoint_every: 5

   automax:
     deterministic: true
     n_trials: 5
     SEED: 42
     name: resnet18_APLoss_cifar10
     output_directory: ./automax_output
     overwrite: true

Run
---

.. code-block:: bash

   python -m src.auto_trainer \
     --config_file recipes/config_auprc.yaml
