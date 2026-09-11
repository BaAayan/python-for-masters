# python-for-masters
Contains my MBIT python projects

Answer for Question 1 - Explanation of the two identified bugs

Bug 1 — UnboundLocalError
Assigning to calls anywhere inside wrapper makes Python treat calls as a local variable for the whole function. So when the list comprehension tries to read calls on its right-hand side, it's looking for that local version — which hasn't been set yet — instead of the outer calls from decorator. That's what triggers the error.

Bug 2 — shared state across instances
calls = [] is created just once, when the decorator is first applied. That one list then gets reused by every call to the function — even calls coming from different instances — so all instances end up sharing (and competing for) the same rate limit instead of each getting their own. The fix is to track calls per instance, e.g. using a dictionary keyed by the instance.
