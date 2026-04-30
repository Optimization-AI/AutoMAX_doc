Recipes
=======

Ready-to-use config files for common tasks, located in ``recipes/automax/``.

.. list-table::
   :header-rows: 1
   :widths: 30 25 45

   * - Recipe
     - Loss / Optimizer
     - When to use
   * - :doc:`auroc`
     - ``AUCMLoss`` / ``PESG``
     - AUROC maximization — standard imbalanced binary classification
   * - :doc:`auprc`
     - ``APLoss`` / ``SOAP``
     - AUPRC / AP maximization — when precision-recall tradeoff matters
   * - :doc:`opauc`
     - ``pAUCLoss (1w)`` / ``SOPAs``
     - One-way pAUC — restrict FPR to a specific range
   * - :doc:`tpauc`
     - ``pAUCLoss (2w)`` / ``SOTAs``
     - Two-way pAUC — restrict both FPR and TPR ranges

.. toctree::
   :hidden:

   auroc
   auprc
   opauc
   tpauc
