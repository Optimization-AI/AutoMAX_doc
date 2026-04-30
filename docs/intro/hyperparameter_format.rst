Hyperparameter Definition Format
=================================

When specifying ``optimizer_kwargs`` or ``loss_kwargs``, each value can be
written in one of two ways.

Scalar Constant
---------------

The value is fixed and **not** searched by AutoMAX:

.. code-block:: yaml

   optimizer_kwargs:
     lr: 0.01

Search Space Dict
-----------------

The value is sampled by AutoMAX during the search:

.. code-block:: yaml

   optimizer_kwargs:
     lr:
       val: [0.0001, 0.1]   # tuple → uniform range; list → categorical; scalar → constant
       default: 0.001        # starting/default value
       log: true             # sample on log scale (numeric ranges only)

Sub-fields
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 25 60

   * - Sub-field
     - Type
     - Description
   * - ``val``
     - scalar / tuple / list
     - **Scalar:** constant value, never searched.
       **Tuple** ``(low, high)``: uniform range.
       **List:** categorical choices.
   * - ``default``
     - scalar
     - Default/starting value. Falls back to lower bound for ranges,
       first element for lists.
   * - ``log``
     - bool
     - Sample the range on a log scale. Ignored for categorical values.

Examples
--------

Fix a learning rate and narrow the margin search space:

.. code-block:: yaml

   training:
     optimizer_kwargs:
       lr: 0.05                   # fixed — not searched

     loss_kwargs:
       margin:
         val: [0.8, 1.0]          # categorical: try 0.8 or 1.0
         default: 1.0

Search learning rate on a log scale:

.. code-block:: yaml

   training:
     optimizer_kwargs:
       lr:
         val: [0.0001, 0.1]       # uniform in log space
         default: 0.001
         log: true
       momentum:
         val: [0.0, 0.9, 0.99]    # categorical: try 3 values
         default: 0.9
