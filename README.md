# bitcoin_scripts

A couple small command line utilities to show current Bitcoin price and fee
statistics.

## Requirements

Python 3.6+ (f-strings 🙌)

I've only tested this on Ubuntu 18.04, but I see no reason why it won't work on
any other OS.

## Use

You can simply download the python scripts and run them as is, there are no
external depedencies.
Alternatively, if you've checked out or downloaded the repository, you may run
`make install` to have the files copied to `~/.local/bin/`, marked as
executable, and renamed (to drop the `.py` extension). You can remove the
scripts from `~/.local/bin/` by running `make uninstall`.

## btc_price.py

Shows the current price, as well as the days' low and high prices.

The prices are printed to the terminal along a sort of number line, with the
current price shown proportionally between the low and high.

Ex.
```
user@computer:~$ btc_price 
$9416.21|--------$9470.01----------------------------------------------|$9764.00
```

The price data is fetched from the `Coinbase Pro` API.

## btc_fees.py

Shows a table relating bitcoin transaction fees to current estimated
confirmation times. The data is retrieved from the `bitcoinfees.earn.com` API.
The table attempts to show the cheapest transaction fee to meet the
corresponding time frame.

Ex.
```
user@computer:~$ btc_fees 

Est Conf Time | Fee (sat/B)
-------------------------------
  Next Block  | 195+
  1  hr       | 179+
  4  hr       | 1+
  12 hr       | 1+
  1 Day       | 1+
  3 Day       | 1+
  7 Day       | 1+

```

## Contributing

If there's anything you'd like to contribute, pull requests are welcome.

Thanks!
