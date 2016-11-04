### Web App that checks the primality of numbers in a given interval
Python & Flask

At the main index will be displayed numbers from 0 to 1000(exclusive), each containing a hyperlink, that will lead to a page saying whether the number is prime or not.

Each page contains at most 1000 numbers. An user can iterate through all the pages with the buttons in the bottom-center of the page or, give a *Start Number* and an *End Number" to show all the numbers from that interval.

NOTE: *End Number* is not included in the interval displayed.

Giving as input an interval containing more than 1000 numbers, the website will display only the first 1000 from *Start Number*.

The input is checked such that there are always two positive integers, *Start Number* being less than *End Number*, so that the
interval contains at least one number. IF *Start Number* is EQUAL with *End Number*, then the page will automatically increment the *End Number*, such that we will have a valid interval : *Start Number* -> *Start Number*+1


I used the **Sieve of Eratosthenes** in order to check if some number is prime or not. It is implemented such that if the primality of a number is checked once, the result is stored and reused in the next querries.



