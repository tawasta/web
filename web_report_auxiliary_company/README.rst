.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============================
Web report – Auxiliary company
==============================

::

    Use an other company, Auxiliary Company, in sales, purchases, invoices and pickings.
    This company is set as the company for their respective PDF prints.

    Sending emails from sale, invoice and purchase are set to use Auxiliary company.
    But remember to modify their email templates to have a sender properly set.

    Auxiliary company goes to the created deliveries of sales and also to the receipts
    created from purchases. Invoices and bills inherit auxiliary company from sales
    and purchases. This inheritance is in place only when a new invoice or picking
    is created and auxiliary company can be changed afterwards.

Configuration
=============
::

    Sales, purchases and invoices needs to be enabled to use this module.

Usage
=====
::

    Go to a sales, purchase or picking and set its auxiliary company.
    See how the PDF prints change when this is done. This does not
    interfere with the business logic.

Known issues / Roadmap
======================
::

    There might exist a company value that this module does not take
    into account, but possible cases has been tested. Further development
    is done if issues are found.

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
