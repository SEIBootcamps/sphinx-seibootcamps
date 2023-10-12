============
Demo Lecture
============

Download Demo
-------------

To download the demo code for this lecture, run the following:

.. parsed-literal::
   :class: console

   $ `hbget demo --demo`:cmd:

Section Heading
===============

Slide Title
-----------

- This is a fake :t:`lecture`

- But it should show lots of feature of our Sphinx system

- It is also a test case for our builders/CSS stylesheets

- As you add features/CSS classes/etc, please add them here

Another Slide Title
-------------------

- It's Pretty Rare

- But You Can Have a Subsection!

Subsection
++++++++++

Like This

Another subsection
++++++++++++++++++

Hi

Basic Styling
=============

Typography
----------

Put blank lines between paragraphs.

Basic Styling
-------------

- For emphasis, use *italics*

- For more emphasis, use **bold**

- For link, use `Go to Google <http://google.com>`_

Citations
---------

Citations use single backticks: \`like this\`. Use for:

- variable names

  - eg: We can now set `x`

- file or path names

  - eg: Store this in `secrets.sh`

- class names

  - eg: Remember our `Cat` class?

- function or method names

  - eg: Never call `lets_play_global_thermonuclear_war`

**Do not use this for general emphasis, please!** Use bold or italics for that.

Code Literals
-------------

Code literals use double backticks: \`\`like this\`\`

These are for literal code blocks or literal coding values:

- things like ``x = 0``

- but not for just talking *about* a variable, function, etc.

  - use `citations` for that

- eg: call `set_color` like this: ``set_color('blue')``

Dashes
------

Use 3 dashes for an em dash---like this.

Two dashes makes an "en dash"--it's too short!

Superscripts and Subscripts
---------------------------

O(n\ `2`:sup:\ )

log\ `2`:sub:\ n

Line Breaks
-----------

As an example:

| You can force line breaks
| by doing this

Or, you can add a slide-only break |reveal-br|
like this.

Symbols
-------

- |nbsp|    NONBREAKING SPACE

- |rarr|    RIGHTWARDS ARROW

- |larr|    LEFTWARDS ARROW

- |lrarr|   BOTH ARROW

- |plus|    PLUS SIGN

- |times|   MULTIPLICATION SIGN

- |check|   CHECK MARK

- |approx|  ALMOST EQUAL TO

- |sub2|    SUBSCRIPT 2

- |super2|  SUPERSCRIPT 2


- |pycmd|   The command to run Python

And the same replacement, inside the console:

.. parsed-literal::
   :class: console

   $ |pycmd| `show_prompt.py`:cmd:

Lists
=====

Lists
-----

- Always put blank line between bulleted list items

- Otherwise bad things will happen!

  - You can have many levels

  - Just indent them

    - Useful for further explanations

  - Try to stick to 2

    - Our CSS only stylizes up to level 3

    - So stop here

- And back to level one

Complex Lists
-------------

- You can also have lists that are not "simple"

  This is where you have multiple paragraphs in a list

  - You can still nest these

    Like so

More about complex lists:

- This happens with things like code blocks

  .. code-block::

    x = 0

- See?

More about complex lists:

- Another case is

- Where you have a simple list

  - Containing a complex list

    This has a second paragraph

- The spacing should work out

Horizontal Lists
----------------

You can make short, side-by-side lists like this:

.. hlist::

   - one

   - two

   - three

   - four

You can specify # columns, too:

.. hlist::
   :columns: 3

   - one

   - two

   - three

   - four

   - five

   - six

Organization
============

Organization
------------

If your slide title is the same as the section title, like this,
the handouts won't repeat it. So do this for things like the "Goals"
slide in a "Goals" section.

New Slides
----------

When you want slide break that shouldn't cause a new
heading in the handouts, |reveal-br| use the `newslide` directive.

This is a new slide with the same title, but on the handouts, it
just flows.

Note: slide content isn't contained in `newslide`,
it just appears after it.

This is a new slide with a new title, but on the handouts, it just
flows.

A new slide with an addition to the title.

You can also use newslide to get background colors

Images
======

Images
------

Add images like so:

.. image:: porcupine.jpg
   :width: 50%

It's good to set a width on it --- otherwise, these are huge on the handouts.

To make an image smaller on handouts, size it with ems:

.. image:: porcupine.jpg
   :width: 10em

(since ems are so much bigger on slides than handouts)

This is especially good for things like book cover images,
since we want them to appear big on slides for visual pop,
but they can appear much smaller on handouts.

For images without good definition, you can add a border:

.. image:: porcupine.jpg
   :width: 50%
   :class: image-border

Literal Blocks
==============

Test

Literal Blocks
--------------

To show literal text blocks, use the explicit ``code-block`` directive

.. code-block::

   Hello! *not italics*

Parsed Literal
--------------

You can use parsed literal for literal blocks that still parse for
style stuff.

.. parsed-literal::

   Hello *italics* and `citation` and `red`:red:

Console
-------

We use a special class on parsed literal for showing shell commands:

.. parsed-literal::
   :class: console

   $ `echo "this is a command"`:cmd:
   this is a command

   $ `echo`:cmd:  `# comment`:comment:

.. parsed-literal::
   :class: console

   Hello

Code Blocks
===========

Code Blocks
-----------

Ask for a code block like so

.. code-block:: python

   if name == "joel":
         print("hi")

.. code-block:: html

   <a href="yo.html">&copy; <!-- comment --></a>

(also: js, sql, xml, and many others---see "pygments" library)

Emphasizing Lines
-----------------

Can emphasize lines:

.. code-block:: python
   :emphasize-lines: 1, 3-4, 6-

   if name == "joel":
       print("hi")
       print("there")
       print("joel")
       print("joel")
       print("joel")
       print("joel")

Add Captions
------------

.. code-block:: python
   :caption: example.py

   if name == "joel":
       print("hi")

It's our style to use this for the filenames of demo files
or if some explanation is needed of where this code is coming from.

.. code-block:: python
   :caption: example.py

   if name == "joel":
       print("hi")

Literal Includes
----------------

Whenever possible, don't inline code --- it's too easy for it to have bugs!

Instead, keep the code in a separate file, so we can test it and include as
demo code

.. literalinclude:: demo-demo/demo-include.py

Can use caption/name like for code blocks:

.. literalinclude:: demo-demo/demo-include.py
   :caption: A Demo

Better, if caption is there but blank, it gets file name

.. literalinclude:: demo-demo/demo-include.py
   :caption:

Finding Things
--------------

Can only include certain lines and can emphasize:

.. literalinclude:: demo-demo/demo-include.py
   :lines: 1, 2, 14-15
   :emphasize-lines: 3

Better is to find things with `pyobject`

.. literalinclude:: demo-demo/demo-include.py
   :pyobject: Cat

Can also use `start-after` and `end-before` to match text:

.. literalinclude:: demo-demo/demo-include.py
   :start-after: Do other stuff

.. literalinclude:: demo-demo/demo-include.py
   :lines: 3-
   :end-before: Do other stuff

This lets us show only one method on a class:

.. literalinclude:: demo-demo/demo-include.py
   :pyobject: Cat.meow
   :prepend: class Cat:  # ...

This is used when we want to highlight part of a longer class.

Or, if we want to pull the method out to show it simply:

.. literalinclude:: demo-demo/demo-include.py
   :pyobject: Cat.meow
   :dedent: 4

(The `dedent` removes four leading spaces)

Don't Use `code`
----------------

There's also a `code` directive that works for Sphinx but it
appears to be undocumented. We style it the same, but don't use it---use
`code-block`, instead.

Notes, Sidebars, Hints, etc.
============================

Admonition
----------

Notes, warnings, and hints are all subclasses of the `admonition` directive.

.. admonition:: They all require titles!

   You can put anything inside of 'em and they **only appear in handouts.**

Notes
-----

Notes are blue.

.. note:: This is a note.

   It goes on.

   And on.

Use notes for sidebar-style information.

.. note:: Other Stuff In Notes

   You can put anything ou want in a note.

   .. code-block:: python

      if name == "joel":
          print("hi")

Warnings
--------

Use warnings to catch students' attention and warn them about gotchas.

.. warning:: This is a warning.

   Make sure you run this command in the correct directory.

Hints
-----

Hints are special; their content is hidden behind an expanding toggle.

.. hint:: Using a certain data structure will make this problem easier

   You could solve this in other ways, but using a linked list (or a
   doubly-linked list) is often a good way to solve this problem. You can do so by
   making the list "circular" --- having the last item in the linked list point back
   to the first item.

   This will let you traverse the list, removing items until one remains.

All Admonitions
---------------

.. attention::

   Attention

.. caution::

   Caution

.. danger::

   Danger

.. error::

   Error

.. important::

   Important

.. note::

   Note

.. tip::

   Tip

.. warning::

   Warning

.. hint::

   Hint

Containers
==========

Containers
----------

The `container` directive just adds a div.

.. container::

   Boring!

This is useful if you want to put a class on it:

.. container:: someclass

   Now I have `someclass` on my `div`

Comparing Things
================

Comparing Things
----------------

Instead of just one thing:

.. code-block:: js

   if (name == "joel")
       console.log("hi");

Side-by-side comparisons are useful:

.. container:: compare

   .. code-block:: js

      if (name == "joel")
        console.log("hi");

   .. code-block:: python

      if name == "joel":
           print("hi")

.. container:: compare

   .. container::

      The spacing should look right even if we lead with compare, or
      if the compares are textual.

   .. container::

      .. code-block:: python

         if name == "joel":
             print("hi")

      .. code-block:: python

         if name == "joel2":
             print("hi")

You can compare an arbitrary #  of things:

.. container:: compare

   .. container::

      Hi

   .. container::

      - A list

      - Of things

   .. code-block:: python

      print('Hello, world!')

Definition Lists
================

Definition Lists
----------------

A Definition List
  Is useful for things like

Glossary Terms
  And stuff like that

Also Works
  When the things are multi-paragraph

  like here.

Should Look Ok
  Even if some thing are not multi-paragraph

Tables
======

Standard Table
--------------

====================== =========== =========== =========== ============ ============
Data Structure         Get         Add         Delete      Iterate      Memory
====================== =========== =========== =========== ============ ============
Tree                   `O(n)`:red: O(1)        O(1)        O(1)         `*`:green:
Binary Search Tree     O(log n)    `O(n)`:red: `O(n)`:red: O(1)         `*`:green:
Dictionary (Hash Map)  O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
Set (Hash Map)         O(1)        O(1)        O(1)        `O(n)`:red:  `**`:orange:
OSet (HashMap+DLL)      O(1)       O(1)        O(1)        O(1)         `***`:red:
ODict (HashMap+DLL)     O(1)       O(1)        O(1)        O(1)         `***`:red:
====================== =========== =========== =========== ============ ============

List Table
----------

.. list-table:: Frozen delights
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

Quotes
======

Quote
-----

Always use the explicit `epigraph` directive

.. epigraph::

   A rose is a rose is a rose.

   -- Gertrude Stein

.. epigraph::

   I like green eggs and ham.

   I really do. I'm Sam I Am.

   -- Sam I Am

Do not add quotes --- our CSS will do that for you
