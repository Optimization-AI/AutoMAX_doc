``autopartial``
===============

.. py:class:: autopartial(autofunc, /, *args, **kwds)

   A :func:`functools.partial`-like wrapper that accepts
   :class:`~ConfigSpace.hyperparameters.Hyperparameter` arguments and
   automatically builds a :class:`~ConfigSpace.ConfigurationSpace` covering
   all of them.

   When called with a SMAC3 ``Configuration`` object (and an optional prefix
   string), it resolves every hyperparameter to its sampled value and invokes
   the wrapped callable.

   :param autofunc: The function or class to wrap.  May itself be an
       ``autopartial`` instance, in which case configuration spaces are merged.
   :type autofunc: callable
   :param args: Positional hyperparameters — each must be a
       :class:`~ConfigSpace.hyperparameters.Hyperparameter` or an
       ``autopartial`` instance.
   :param kwds: Keyword hyperparameters — same constraint as *args*.

   :raises TypeError: If *autofunc* is not callable.
   :raises ValueError: If any argument is not a
       :class:`~ConfigSpace.hyperparameters.Hyperparameter` or ``autopartial``.

   .. rubric:: Usage pattern

   .. code-block:: python

      from ConfigSpace.hyperparameters import UniformFloatHyperparameter
      from src.core import autopartial

      lr_hp     = UniformFloatHyperparameter("lr", 1e-4, 0.1, log=True)
      margin_hp = UniformFloatHyperparameter("margin", 0.5, 1.5)

      wrapped_optimizer = autopartial(MyOptimizer, lr=lr_hp, margin=margin_hp)

      # wrapped_optimizer.cs  →  ConfigurationSpace with lr and margin
      # Call with a sampled configuration:
      optimizer = wrapped_optimizer(some_smac_config)

   .. rubric:: Nesting autopartial instances

   ``autopartial`` instances can be nested.  The inner configuration spaces
   are merged into the outer one using a colon-delimited prefix:

   .. code-block:: python

      inner = autopartial(dict, lr=lr_hp)
      outer = autopartial(MyTrainer, optimizer_kwargs=inner)
      # outer.cs contains "optimizer_kwargs:lr"

   .. rubric:: Attributes

   .. list-table::
      :header-rows: 1
      :widths: 20 80

      * - Attribute
        - Description
      * - ``autofunc``
        - The underlying callable.
      * - ``args``
        - Tuple of positional ``Hyperparameter`` / ``autopartial`` objects.
      * - ``kwds``
        - Dict of keyword ``Hyperparameter`` / ``autopartial`` objects.
      * - ``cs``
        - The assembled :class:`~ConfigSpace.ConfigurationSpace`.

   .. rubric:: Methods

   .. py:method:: __call__(space, prefix="")

      Resolve all hyperparameters from *space* and call ``autofunc``.

      :param space: A SMAC3 / ConfigSpace ``Configuration`` object.
      :param prefix: Namespace prefix used when this instance is nested inside
          another ``autopartial``.
      :type prefix: str
      :returns: The return value of ``autofunc(*resolved_args, **resolved_kwds)``.
