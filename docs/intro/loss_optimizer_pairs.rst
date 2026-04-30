Loss / Optimizer Pairs
======================

Each loss function has a canonical optimizer and a predefined hyperparameter
search space. Mismatched pairs will raise an error at startup.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - ``loss``
     - ``optimizer``
     - Key hyperparameters
   * - ``AUCMLoss``
     - ``PESG``
     - ``lr``, ``epoch_decay``, ``weight_decay``, ``momentum``, ``margin``
   * - ``CompositionalAUCLoss``
     - ``PDSCA``
     - ``lr``, ``epoch_decay``, ``weight_decay``, ``margin``, ``k``
   * - ``APLoss``
     - ``SOAP``
     - ``lr``, ``epoch_decay``, ``momentum``, ``weight_decay``, ``gamma``, ``margin``
   * - ``pAUC_CVaR_Loss``
     - ``SOPA``
     - ``lr``, ``epoch_decay``, ``weight_decay``, ``margin``, ``beta``, ``eta``
   * - ``pAUC_DRO_Loss``
     - ``SOPAs``
     - ``lr``, ``epoch_decay``, ``momentum``, ``weight_decay``, ``gamma``, ``margin``, ``Lambda``
   * - ``tpAUC_KL_Loss``
     - ``SOTAs``
     - ``lr``, ``epoch_decay``, ``momentum``, ``weight_decay``, ``tau``, ``gammas``, ``margin``, ``Lambda``
   * - ``NDCGLoss``
     - ``SONG``
     - ``lr``, ``epoch_decay``, ``momentum``, ``weight_decay``, ``gamma0``, ``gamma1``, ``eta0``, ``margin``, ``sigmoid_alpha``
   * - ``CrossEntropyLoss``
     - ``SGD``
     - ``lr``, ``epoch_decay``, ``momentum``, ``weight_decay``
   * - ``CrossEntropyLoss``
     - ``Adam``
     - ``lr``, ``epoch_decay``, ``weight_decay``

Choosing a Pair
---------------

Use this guide to select the right loss for your task:

- **AUROC maximization** — use ``AUCMLoss`` + ``PESG`` (most common for imbalanced binary classification)
- **AUPRC / AP maximization** — use ``APLoss`` + ``SOAP``
- **One-way partial AUC** (restrict FPR) — use ``pAUCLoss`` with ``mode: 1w`` + ``SOPAs``
- **Two-way partial AUC** (restrict both FPR and TPR) — use ``pAUCLoss`` with ``mode: 2w`` + ``SOTAs``
- **Ranking (NDCG)** — use ``NDCGLoss`` + ``SONG``
- **Baseline** — use ``CrossEntropyLoss`` + ``SGD`` or ``Adam``

.. seealso::

   See :doc:`../recipes/index` for ready-to-use config files for each pair.
