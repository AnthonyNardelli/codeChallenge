# codeChallenge

## Teravision interview

## Django Project

This project serves an endpoint(/api/flattener) that accepts two methods GET and POST

The POST method accepts in the body a Key called "items" with the list you want to flatten
Ex.
{
"Items: [1, 2, [3, 4, [5, 6], 7], 8]
}

The GET method returns all results saved in the POST method
